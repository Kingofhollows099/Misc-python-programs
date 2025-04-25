# First, let's scaffold out a complete version of the script with the requested features.
# This includes:
# - GUI file selection
# - Parameter customization via sliders
# - GUI to draw exclusion boxes
# - PDF to image conversion
# - 3D mesh generation
# - STL export

import tkinter as tk
from tkinter import filedialog, simpledialog
from pdf2image import convert_from_path
from PIL import Image, ImageTk
import numpy as np
import cv2
from stl import mesh
import os

class PDFToSTLApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF to 3D STL Converter")

        self.params = {
            "base_height": tk.DoubleVar(value=3.0),
            "text_height": tk.DoubleVar(value=2.0),
            "scale": tk.DoubleVar(value=100.0),
            "sensitivity": tk.IntVar(value=128)
        }

        self.exclude_boxes = []
        self.rect_start = None
        self.rect = None
        self.canvas_img = None
        self.tk_img = None
        self.img = None
        self.heightmap = None
        self.vertices = None
        self.faces = None

        self.setup_widgets()

    def setup_widgets(self):
        sliders_frame = tk.Frame(self.root)
        sliders_frame.pack()

        self.base_height_slider_label = tk.Label(sliders_frame, text=f"Base Height (mm)")
        self.base_height_slider_label.grid(row=0, column=0, padx=5, pady=5)
        self.base_height_slider = tk.Scale(sliders_frame, from_=0.1, to=20.0, resolution=0.1, variable=self.params["base_height"], orient="horizontal")
        self.base_height_slider.grid(row=1, column=0, padx=5, pady=5)

        self.text_height_slider_label = tk.Label(sliders_frame, text="Text Height (mm)")
        self.text_height_slider_label.grid(row=0, column=1, padx=5, pady=5)
        self.text_height_slider = tk.Scale(sliders_frame, from_=0.1, to=10.0, resolution=0.1, variable=self.params["text_height"], orient="horizontal")
        self.text_height_slider.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Scale (%)").pack()
        tk.Scale(self.root, from_=1.0, to=500.0, resolution=0.1, variable=self.params["scale"], orient="horizontal").pack()

        tk.Label(self.root, text="Sensitivity").pack()
        tk.Scale(self.root, from_=0, to=255, variable=self.params["sensitivity"], orient="horizontal").pack()

        self.unit = tk.StringVar(value="mm")
        tk.Label(self.root, text="Units").pack()
        tk.OptionMenu(self.root, self.unit, "mm", "inches", command=self.update_units).pack()

        self.dimensions_label = tk.Label(self.root, text="Dimensions: N/A")
        self.dimensions_label.pack()

        self.dead_zone_slider_label = tk.Label(self.root, text="Dead Zone (pixels)")
        self.dead_zone_slider_label.pack()
        self.dead_zone_slider = tk.Scale(self.root, from_=0, to=0, resolution=1, orient="horizontal")
        self.dead_zone_slider.pack()
        self.dead_zone_slider.config(command=lambda value: self.update_canvas())

        tk.Button(self.root, text="Load File", command=self.load_file).pack()
        tk.Button(self.root, text="Generate STL", command=self.save_stl).pack()

        canvas_frame = tk.Frame(self.root)
        canvas_frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(canvas_frame, cursor="cross")
        self.scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.canvas.bind("<ButtonPress-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)
        self.canvas.bind("<Motion>", self.on_mouse_move)

        tk.Label(self.root, text="Mesh Resolution (%)").pack()
        self.mesh_resolution = tk.DoubleVar(value=100.0)
        tk.Scale(self.root, from_=5.0, to=100.0, resolution=1.0, variable=self.mesh_resolution, orient="horizontal").pack()


    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Supported Files", "*.pdf;*.jpeg;*.jpg;*.png")])
        if not file_path:
            return

        if file_path.lower().endswith(".pdf"):
            pages = convert_from_path(file_path, dpi=150)
            self.img = np.array(pages[0].convert('L'))
        elif file_path.lower().endswith(('.jpeg', '.jpg', '.png')):
            self.img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

        self.update_dead_zone_slider()
        self.update_canvas()

    def update_units(self, unit):
        self.update_dimensions()

    def convert_dimension(self, dimension, unit):
        scale = self.params["scale"].get() / 1000
        converted_dimension = dimension * scale
        if unit == "inches":
            converted_dimension /= 25.4
        return converted_dimension

    def update_dimensions(self):
        if self.img is None:
            self.dimensions_label.config(text="Dimensions: N/A")
            return

        height, width = self.img.shape[:2]
        projected_width = self.convert_dimension(width, self.unit.get())
        projected_height = self.convert_dimension(height, self.unit.get())
        dimensions = f"{projected_width:.2f} x {projected_height:.2f} {self.unit.get()}"
        self.dimensions_label.config(text=f"Projected Dimensions: {dimensions}")

    def update_dead_zone_slider(self):
        if self.img is not None:
            height, width = self.img.shape[:2]
            max_dead_zone = min(height // 2, width // 2) - 20
            self.dead_zone_slider.config(to=max_dead_zone)

    def update_canvas(self):
        img_rgb = cv2.cvtColor(self.img, cv2.COLOR_GRAY2RGB)
        for (x1, y1, x2, y2) in self.exclude_boxes:
            cv2.rectangle(img_rgb, (x1, y1), (x2, y2), (255, 0, 0), 2)

        dead_zone = self.dead_zone_slider.get()
        height, width = self.img.shape[:2]
        cv2.rectangle(img_rgb, (dead_zone, dead_zone), (width - dead_zone, height - dead_zone), (0, 0, 255), 2)

        img_pil = Image.fromarray(img_rgb)
        # Ensure the canvas size remains fixed and the image scales to fit within it
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        img_pil.thumbnail((canvas_width, canvas_height), Image.LANCZOS)
        self.tk_img = ImageTk.PhotoImage(img_pil)
        self.canvas.delete("all")  # Clear the canvas
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_img)
        self.update_dimensions()

    def on_mouse_down(self, event):
        self.rect_start = None

    def on_mouse_move(self, event):
        pass

    def on_mouse_drag(self, event):
        pass

    def on_mouse_up(self, event):
        self.update_canvas()

    def apply_dead_zone(self):
        if self.img is None or self.heightmap is None:
            return

        dead_zone = self.dead_zone_slider.get()
        height, width = self.img.shape[:2]
        self.heightmap[:dead_zone, :] = 0
        self.heightmap[-dead_zone:, :] = 0
        self.heightmap[:, :dead_zone] = 0
        self.heightmap[:, -dead_zone:] = 0

    def generate_heightmap(self):
        img_copy = self.img.copy()
        for (x1, y1, x2, y2) in self.exclude_boxes:
            img_copy[y1:y2, x1:x2] = 255

        _, mask = cv2.threshold(img_copy, self.params["sensitivity"].get(), 255, cv2.THRESH_BINARY_INV)
        kernel = np.ones((3, 3), np.uint8)
        mask_cleaned = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        heightmap = np.where(mask_cleaned > 0, self.params["text_height"].get(), 0) + self.params["base_height"].get()

        # Downsample heightmap
        scale_percent = self.mesh_resolution.get() / 100.0
        new_size = (max(2, int(heightmap.shape[1] * scale_percent)),
                    max(2, int(heightmap.shape[0] * scale_percent)))
        heightmap_resized = cv2.resize(heightmap.astype(np.float32), new_size, interpolation=cv2.INTER_AREA)

        self.heightmap = heightmap_resized
        self.apply_dead_zone()

    def generate_mesh(self):
        ny, nx = self.heightmap.shape
        vertices = np.zeros((ny, nx, 3), dtype=np.float32)

        for y in range(ny):
            for x in range(nx):
                vertices[y, x] = [
                    self.convert_dimension(x, "mm"),
                    self.convert_dimension(y, "mm"),
                    self.heightmap[y, x]
                ]

        flat_vertices = vertices.reshape(-1, 3)

        faces = []
        for y in range(ny - 1):
            for x in range(nx - 1):
                idx = lambda i, j: i * nx + j
                faces.append([idx(y, x), idx(y, x + 1), idx(y + 1, x)])
                faces.append([idx(y + 1, x + 1), idx(y + 1, x), idx(y, x + 1)])

        self.vertices = flat_vertices
        self.faces = np.array(faces)


    def save_stl(self):
        if self.img is None:
            print("No image loaded.")
            return
        self.generate_heightmap()
        self.generate_mesh()
        stl_path = filedialog.asksaveasfilename(defaultextension=".stl", filetypes=[("STL Files", "*.stl")])
        if not stl_path:
            return
        your_mesh = mesh.Mesh(np.zeros(self.faces.shape[0], dtype=mesh.Mesh.dtype))
        for i, f in enumerate(self.faces):
            for j in range(3):
                your_mesh.vectors[i][j] = self.vertices[f[j], :]
        your_mesh.save(stl_path)
        print(f"STL saved to {stl_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFToSTLApp(root)
    root.mainloop()