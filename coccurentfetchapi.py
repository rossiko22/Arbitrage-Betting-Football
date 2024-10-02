import requests
import json
import concurrent.futures
import time

with open("leagues/leagues.txt", "r") as file:
    content = file.read()

API_KEY = "place_api_here"
REGION = "eu,us2,us,uk,au"
MARKET = "h2h"
SPORT = json.loads(content)
ODDS_FORMAT = "decimal"
DATE_FORMAT = "iso"
COMMENCE_FROM = "2024-09-20T00:00:00Z" #Change this accordingly
COMMENCE_TO = "2024-10-02T00:00:00Z" #Change this accordingly


def fetch_data(sport):
    url = (f"https://api.the-odds-api.com/v4/sports/{sport}/odds/?apiKey={API_KEY}&regions={REGION}&markets={MARKET}"
    f"&commenceTimeFrom={COMMENCE_FROM}&commenceTimeTo={COMMENCE_TO}")
    response = requests.get(url)
    return sport, response.json()

def save_data(sport, data):
    file_path = f"datatxt/{sport}.txt"
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks to the executor
        future_to_sport = {executor.submit(fetch_data, sport): sport for sport in SPORT}
        
        for future in concurrent.futures.as_completed(future_to_sport):
            sport = future_to_sport[future]
            try:
                time.sleep(2)
                sport, data = future.result()
                save_data(sport, data)
                print(f"Data for {sport} saved successfully.")
            except Exception as e:
                print(f"An error occurred for {sport}: {e}")

if __name__ == "__main__":
    main()
