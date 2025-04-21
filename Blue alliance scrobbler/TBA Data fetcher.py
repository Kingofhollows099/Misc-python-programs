import requests
from datetime import date, datetime
import json
import os
import traceback
import time
from tqdm import tqdm

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

def numerate(data): #Numerate data
    out = {}
    for i in range(len(data)):
        out[i] = data[i]
    return out

def fetchData():
    """
    Fetches data from the Blue Alliance API and saves it to a JSON file.
    """
    try:
        year = date.today().year #Set current year

        url = "https://www.thebluealliance.com/api/v3"

        with open('Blue ALliance scrobbler\API_KEY.txt', 'r') as file: #Get api key from API_KEY.txt
            api_key = file.read()

        headers = {"X-TBA-Auth-Key": api_key}
        
        log("-------- Fetch start --------")
                
        #TODO: update seasonOVer to actually be accurate
        seasonOver = True if 1==2 else False

        #Initialize json if need be.
        if os.path.exists('Blue alliance scrobbler\Data.json') == False: #Check if Data.json exists
            log("Data.json does not exist. Creating new file.")
            writeData('Blue alliance scrobbler\Data.json', {"years": {}, "teams": {}}) #Write empty data to Data.json

        data = readData('Blue alliance scrobbler\Data.json') #Read events from Events.json
        yearData = data["years"]


        if str(year - 2) not in yearData:
            yearData[year - 2] = numerate(requests.get(f"{url}/events/{year - 2}", headers=headers).json())
            log(f"Fetched {year - 2} season data from API.")
            for event_key in tqdm(yearData[year - 2].keys(), desc=f"Year {year - 2} teams", total=len(yearData[year - 2])):
                event = yearData[year - 2][event_key]
                event["teams"] = requests.get(f"{url}/event/{event['key']}/teams", headers=headers).json()
                log(f"Gathered team data for event {event['key']} in year {year - 2}.")
                time.sleep(0.001) #Sleep for 1ms to avoid rate limiting
        else:
            log(f"{year - 2} season already in Data.json. API request not sent.")

        if str(year - 1) not in yearData:
            yearData[year - 1] = numerate(requests.get(f"{url}/events/{year - 1}", headers=headers).json())
            log(f"Fetched {year - 1} season data from API.")
            for event_key in tqdm(yearData[year - 1].keys(), desc=f"Year {year - 1} teams", total=len(yearData[year - 1])):
                event = yearData[year - 1][event_key]
                event["teams"] = requests.get(f"{url}/event/{event['key']}/teams", headers=headers).json()
                log(f"Gathered team data for event {event['key']} in year {year - 1}.")
                time.sleep(0.001) #Sleep for 1ms to avoid rate limiting
        else:
            log(f"{year - 1} season already in Data.json. API request not sent.")

        if str(year) not in yearData:
            yearData[year] = numerate(requests.get(f"{url}/events/{year}", headers=headers).json())
            log(f"Fetched {year} season data from API.")
            for event_key in tqdm(yearData[year].keys(), desc=f"Year {year} teams", total=len(yearData[year])):
                event = yearData[year][event_key]
                event["teams"] = requests.get(f"{url}/event/{event['key']}/teams", headers=headers).json()
                log(f"Gathered team data for event {event['key']} in year {year}.")
                time.sleep(0.001) #Sleep for 1ms to avoid rate limiting
        elif str(year) in yearData and seasonOver == False:
            log(f"{year} season already in Data.json, but season is not yet over. Proceeding with update.")
            log(f"Deleting old {year} season data from Data.json.")
            data["years"].pop(str(year))
            yearData[year] = numerate(requests.get(f"{url}/events/{year}", headers=headers).json())
            log(f"Fetched {year} season data from API.")
            for event_key in tqdm(yearData[year].keys(), desc=f"Year {year} teams", total=len(yearData[year])):
                event = yearData[year][event_key]
                event["teams"] = requests.get(f"{url}/event/{event['key']}/teams", headers=headers).json()
                log(f"Gathered team data for event {event['key']} in year {year}.")
                time.sleep(0.001) #Sleep for 1ms to avoid rate limiting
        else:
            log(f"{year} season already in Data.json. API request not sent.")


        #Save Data
        data["years"] = yearData #Update years in data
        writeData('Blue alliance scrobbler\Data.json', data) #Write events to Data.json
        log("-------- Fetch finished --------\n\n")

    except Exception as e:
        error_message = traceback.format_exc()
        log("An error occurred:\n" + error_message)
        log("-------- Fetch ended with error --------\n\n")

fetchData() #Fetch data from API
