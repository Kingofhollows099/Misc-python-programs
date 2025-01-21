def calculate_scale(value, min_value, max_value):
    """
    Calculate a scale from 1 to 50 based on where the value lies within the given range.
    """
    value = max(value, min_value)  # Ensure the value is not below the minimum
    return round(((value - min_value) / (max_value - min_value)) * 49 + 1)

def visual_scale(scale, max_scale=50):
    """
    Generate a visual representation of the scale as a bar.
    """
    filled = "|" * scale
    empty = "-" * (max_scale - scale)
    return f"[{filled}{empty}]"

def calculate_offensive_scale(wins, losses):
    """
    Calculate a custom offensive capability scale based on wins and losses.
    Wins directly increase the score, while losses reduce it.
    """
    if wins == 0 and losses == 0:
        return 1  # Minimum scale if no matches

    A = 3.56087679501
    B = 11.685438514
    e = 2.718281828459045
    k = 0.29
    score = 50 + (1 + (wins / 50)) ** A - (1 + (losses / 50)) ** B + 1/(0.2 + e ** (-1 * (wins - 2)) * k)

    # Scale score to a range of 1 to 50, where 104 wins is maximum
    return calculate_scale(score, 0, 104)

def main():
    print("Enter the stats one by one.")

    # Speed input
    speed = float(input("Enter the speed in mph: "))
    speed_scale = calculate_scale(speed, 90, 600)

    # Offensive Capability input
    print("For Offensive Capability, enter the win-loss record as two integers (wins and losses):")
    wins = int(input("Wins: "))
    losses = int(input("Losses: "))
    offensive_scale = calculate_offensive_scale(wins, losses)

    # Survivability input
    survivability = float(input("Enter the survivability percentage (0-100%): "))
    survivability = max(survivability, 0)  # Ensure the survivability is not below 0
    survivability_scale = calculate_scale(survivability, 0, 100)

    # Print results
    print("\nCalculated Scales:")
    print(f"Speed: {speed_scale}/50 {visual_scale(speed_scale)}")
    print(f"Offensive: {offensive_scale}/50 {visual_scale(offensive_scale)}")
    print(f"Survival: {survivability_scale}/50 {visual_scale(survivability_scale)}")

if __name__ == "__main__":
    main()
