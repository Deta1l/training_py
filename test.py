import os
import pandas as pd
from tqdm import tqdm
from openpyxl import load_workbook
from bs4 import BeautifulSoup
import requests

def download_races():
    """Скачивает файлы гонок с названиями"""
    HTML_FILE = "RaceMann.html"
    BASE_URL = "https://miks.racemann.com"
    DOWNLOAD_DIR = "miks_driverstats"
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    with open(HTML_FILE, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "lxml")

    race_items = soup.select("li[data-race-id]")
    miks_races = []

    for item in race_items:
        race_name = item.select_one(".race-list-name")
        if race_name and any(keyword in race_name.text.upper() for keyword in ["MIKS", "SHONX"]) and "КВАЛИФИКАЦИЯ" not in race_name.text.upper():
            race_id = item["data-race-id"]
            title = race_name.text.strip().replace(" ", "_").replace("/", "-")
            miks_races.append((race_id, title))

    print(f"[+] Найдено MIKS/SHONX гонок: {len(miks_races)}")

    for race_id, title in miks_races:
        download_url = f"{BASE_URL}/DriverStat/driverslistcsv/{race_id}?allGroups=false&allStages=false"
        try:
            response = requests.get(download_url)
            response.raise_for_status()

            filename = os.path.join(DOWNLOAD_DIR, f"{title}_{race_id}.xlsx")
            with open(filename, "wb") as f:
                f.write(response.content)

            # Добавляем название гонки в скачанный файл
            add_title_to_excel(filename, title)
            
            print(f"[✓] Скачан и обработан: {filename}")
        except Exception as e:
            print(f"[!] Ошибка при скачивании для {race_id}: {e}")

def add_title_to_excel(filepath, title):
    """Добавляет столбец с названием гонки в файл"""
    try:
        df = pd.read_excel(filepath, sheet_name='Список участников')
        df['Название_гонки'] = title  # Добавляем новый столбец
        
        # Сохраняем обратно в тот же файл
        with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Список участников', index=False)
    except Exception as e:
        print(f"Ошибка при добавлении названия в {filepath}: {e}")

def merge_xlsx_files(input_folder, output_file):
    """Объединяет файлы с добавленными названиями гонок"""
    xlsx_files = [
        f for f in os.listdir(input_folder) 
        if (f.lower().endswith('.xlsx') and
            any(keyword in f.upper() for keyword in ['MIKS', 'SHONX']) and
            'Квалификация' not in f)
    ]
    
    if not xlsx_files:
        print("Не найдено подходящих XLSX-файлов.")
        return
    
    merged_data = pd.DataFrame()
    
    for file in tqdm(xlsx_files, desc="Объединение файлов"):
        file_path = os.path.join(input_folder, file)
        try:
            df = pd.read_excel(file_path, sheet_name='Список участников')
            merged_data = pd.concat([merged_data, df], ignore_index=True)
        except Exception as e:
            print(f"\nОшибка в файле {file}: {str(e)}")

    if not merged_data.empty:
        try:
            with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
                merged_data.to_excel(writer, sheet_name='Список участников', index=False)
            print(f"\nОбъединенный файл сохранен: {output_file}")
        except Exception as e:
            print(f"\nОшибка при сохранении: {str(e)}")
    else:
        print("Нет данных для сохранения.")

if __name__ == "__main__":
    # 1. Скачиваем файлы гонок
    download_races()
    
    # 2. Объединяем скачанные файлы
    input_folder = "miks_driverstats"
    output_file = "C:/Users/MPyankov/Desktop/teat_analys/output3.xlsx"
    
    if os.path.exists(input_folder):
        merge_xlsx_files(input_folder, output_file)
    else:
        print(f"Папка {input_folder} не существует!")