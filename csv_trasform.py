import os
import pandas as pd
from tqdm import tqdm
from openpyxl import load_workbook

def merge_xlsx_files(input_folder, output_file):
    """
    Объединяет XLSX-файлы, содержащие 'MIKS' или 'SHONX' в названии (регистронезависимо),
    исключая файлы с 'Квалификация', с проверкой на дубликаты.
    
    :param input_folder: Путь к папке с XLSX-файлами
    :param output_file: Путь к результирующему XLSX-файлу
    """
    # Собираем подходящие файлы
    xlsx_files = [
        f for f in os.listdir(input_folder) 
        if (f.lower().endswith('.xlsx') and
            any(keyword in f.upper() for keyword in ['MIKS', 'SHONX']) and
            'Квалификация' not in f)
    ]
    
    if not xlsx_files:
        print("Не найдено подходящих XLSX-файлов (MIKS/SHONX и без 'Квалификация').")
        return
    
    print(f"Найдено {len(xlsx_files)} файлов для обработки...")
    
    # Создаем пустой DataFrame и множество для отслеживания дубликатов
    merged_data = pd.DataFrame()
    seen_entries = set()
    duplicates_count = 0
    
    # Обрабатываем файлы с прогресс-баром
    for file in tqdm(xlsx_files, desc="Обработка файлов"):
        file_path = os.path.join(input_folder, file)
        try:
            df = pd.read_excel(file_path, sheet_name='Список участников')
            
                    
        except Exception as e:
            print(f"\nОшибка в файле {file}: {str(e)}")

    # Выводим статистику
    print(f"\nОбработано файлов: {len(xlsx_files)}")
    print(f"Найдено дубликатов: {duplicates_count}")
    print(f"Уникальных записей: {len(merged_data)}")
    
    # Сохраняем результат
    if not merged_data.empty:
        try:
            with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
                merged_data.to_excel(writer, sheet_name='Список участников', index=False)
            print(f"\nРезультат сохранен в {output_file}")
            print(f"Размер конечного файла: {os.path.getsize(output_file)/1024:.2f} KB")
        except Exception as e:
            print(f"\nОшибка при сохранении: {str(e)}")
    else:
        print("Нет данных для сохранения.")

if __name__ == "__main__":
    # Настройки
    input_folder = "C:/Users/MPyankov/Desktop/teat_analys/miks_driverstats"  # Замените на реальный путь
    output_file = "C:/Users/MPyankov/Desktop/teat_analys/output2.xlsx"  # Имя выходного файла
    
    # Проверяем существование папки
    if not os.path.exists(input_folder):
        print(f"Ошибка: папка '{input_folder}' не существует!")
    else:
        merge_xlsx_files(input_folder, output_file)