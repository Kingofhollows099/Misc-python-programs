import requests
from datetime import date, datetime
import json
import os
import traceback

try:
    year = date.today().year #Set current year

    url = "https://www.thebluealliance.com/api/v3"

    with open('Blue ALliance scrobbler\API_KEY.txt', 'r') as file: #Get api key from API_KEY.txt
        api_key = file.read()

    headers = {"X-TBA-Auth-Key": api_key}


    def writeData(fileName, data): #Write data to a file
        with open(fileName, 'w') as file:
            json.dump(data, file, indent=4)

    def readData(fileName): #Read data from a file
        with open(fileName, 'r') as file:
            data = json.load(file)
        return data
    def log(message): #Log message to console
        print(f"[{datetime.today()}] {message}")
        with open('Blue alliance scrobbler\log.log', 'a') as file:
            file.write(f"[{datetime.now()}] {message}\n")
    
    log("-------- Program start --------")
            
    #TODO: update seasonOVer to actually be accurate
    seasonOver = True if 1==2 else False

    #Initialize json if need be.
    if os.path.exists('Blue alliance scrobbler\Data.json') == False: #Check if Data.json exists
        log("Data.json does not exist. Creating new file.")
        writeData('Blue alliance scrobbler\Data.json', {"years": {}, "teams": {}}) #Write empty data to Data.json

    data = readData('Blue alliance scrobbler\Data.json') #Read events from Events.json
    yearData = data["years"]



    if str(year - 2) not in yearData:
        yearData[year - 2] = requests.get(f"{url}/events/{year - 2}", headers=headers).json()
        log(f"Fetched {year - 2} season data from API.")
    else:
        log(f"{year - 2} season already in Data.json. API request not sent.")

    if str(year - 1) not in yearData:
        yearData[year - 1] = requests.get(f"{url}/events/{year - 1}", headers=headers).json()
        log(f"Fetched {year - 1} season data from API.")
    else:
        log(f"{year - 1} season already in Data.json. API request not sent.")

    if str(year) not in yearData:
        log(f"Fetched {year} season data from API.")
        yearData[year] = requests.get(f"{url}/events/{year}", headers=headers).json()
    elif str(year) in yearData and seasonOver == False:
        log(f"{year} season already in Data.json, but season is not yet over. Proceeding with update.")
        log(f"Deleting old {year} season data from Data.json.")
        data["years"].pop(str(year))
        yearData[year] = requests.get(f"{url}/events/{year}", headers=headers).json()
    else:
        log(f"{year} season already in Data.json. API request not sent.")

    #Save Data
    data["years"] = yearData #Update years in data
    writeData('Blue alliance scrobbler\Data.json', data) #Write events to Data.json
    log("-------- Program finished --------\n\n")

except Exception as e:
    error_message = traceback.format_exc()
    log("An error occurred:\n" + error_message)
    log("-------- Program finished with error --------\n\n")