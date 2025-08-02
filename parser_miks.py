from bs4 import BeautifulSoup
import requests
import os

# Путь к сохранённому HTML
HTML_FILE = "RaceMann.html"
BASE_URL = "https://miks.racemann.com"

# Папка для сохранения
DOWNLOAD_DIR = "miks_driverstats"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

with open(HTML_FILE, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "lxml")

# Ищем элементы списка гонок
race_items = soup.select("li[data-race-id]")

miks_races = []

for item in race_items:
    race_name = item.select_one(".race-list-name")
    if race_name and "MIKS" and "SHONX" and "Shonx" and not "Квалификация" in race_name.text.upper():
        race_id = item["data-race-id"]
        title = race_name.text.strip().replace(" ", "_").replace("/", "-")
        miks_races.append((race_id, title))

print(f"[+] Найдено MIKS гонок: {len(miks_races)}")

for race_id, title in miks_races:
    download_url = f"{BASE_URL}/DriverStat/driverslistcsv/{race_id}?allGroups=false&allStages=false"
    try:
        response = requests.get(download_url)
        response.raise_for_status()

        filename = os.path.join(DOWNLOAD_DIR, f"{title}_{race_id}.xlsx")
        with open(filename, "wb") as f:
            f.write(response.content)

        print(f"[✓] Скачан: {filename}")
    except Exception as e:
        print(f"[!] Ошибка при скачивании для {race_id}: {e}")