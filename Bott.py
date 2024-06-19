import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_latest_earthquake():
    url = "https://deprem.afad.gov.tr/last-earthquakes.html"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve data: {response.status_code}")
        return None

    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table")
    if not table:
        print("Failed to find the table in the HTML")
        return None

    rows = table.find_all("tr")[1:]  

    if not rows:
        print("No rows found in the table")
        return None

    latest_earthquake = None
    for row in rows:  
        cells = row.find_all("td")

        if len(cells) >= 7:  
            date = cells[0].text.strip()
            latitude = cells[1].text.strip()
            longitude = cells[2].text.strip()
            depth = cells[3].text.strip()
            magnitude = cells[5].text.strip()
            location = cells[6].text.strip()

            try:
                magnitude_control = float(magnitude)
            except ValueError:
                continue  
            if magnitude_control > 2:  
                formatted_entry = f"{date} - {location} - Magnitude: {magnitude} - Depth: {depth} km"
                latest_earthquake = formatted_entry
                break  

    if not latest_earthquake:
        print("No earthquake found with magnitude greater than 2")

    return latest_earthquake

def send_to_slack(message):
    slack_token = os.getenv("SLACK_TOKEN")
    if not slack_token:
        print("SLACK_TOKEN is not set in the environment variables.")
        return

    channel = "#bot"  

    url = f"https://slack.com/api/chat.postMessage"
    headers = {
        "Authorization": f"Bearer {slack_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "channel": channel,
        "text": message
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200 and response.json()["ok"]:
        print("Message successfully sent to Slack")
    else:
        print(f"Failed to send message to Slack: {response.status_code}, {response.text}")


result = fetch_latest_earthquake()

if result:
    send_to_slack(result)
else:
    send_to_slack("No data available")

#hah