import requests
import random
import os
import json
import urllib3

urllib3.disable_warnings()

URL = "https://v2.jokeapi.dev/joke/Any?type=single"
FILENAME = "jokes_db.json"

def get_joke():
    try:
        response = requests.get(URL, timeout=5, verify=False)
        response.raise_for_status()
        data = response.json()
        joke = data.get("joke", "No joke found")
        
        # Сохранение в JSON
        jokes = []
        if os.path.exists(FILENAME):
            with open(FILENAME, "r", encoding="utf-8") as f:
                try: jokes = json.load(f)
                except: jokes = []
        jokes.append(joke)
        with open(FILENAME, "w", encoding="utf-8") as f:
            json.dump(jokes, f, ensure_ascii=False, indent=4)
        print(f"\n[ONLINE]\n{joke}")

    except:
        print("\n[OFFLINE] Loading from local JSON...")
        if os.path.exists(FILENAME):
            with open(FILENAME, "r", encoding="utf-8") as f:
                jokes = json.load(f)
                if jokes:
                    print(f"Random joke: {random.choice(jokes)}")
                else:
                    print("JSON file is empty.")
        else:
            print("Local JSON file not found.")

if __name__ == "__main__":
    get_joke()