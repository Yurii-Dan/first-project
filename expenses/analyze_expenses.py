import csv
from collections import defaultdict
from datetime import datetime
import os

# Шлях до файлу
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'expenses.csv')

# Введення періоду
start_str = input("Введіть початкову дату (рррр-мм-дд): ")
end_str = input("Введіть кінцеву дату (рррр-мм-дд): ")

try:
    start_date = datetime.strptime(start_str, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_str, "%Y-%m-%d").date()
except ValueError:
    print("❌ Неправильний формат дати!")
    exit()
    
# Підсумки по категоріях і днях
category_totals = defaultdict(float)
daily_totals = defaultdict(float)

with open(file_path, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) != 3:
            continue

        name, cost_str, date_str = row
        try:
            cost = float(cost_str)
            date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        except ValueError:
            continue
        if start_date <= date.date() <= end_date:
            category_totals[name] += cost
            daily_totals[date.date()] += cost

if not daily_totals:
    print("⚠️ У заданому періоді немає витрат.")
    exit()

# Вивід
print(f"\n🗓 Витрати з {start_date} по {end_date}:")
print("📊 Витрати по категоріях:")
for category, total in category_totals.items():
    print(f"- {category}: {total:.2f} грн")

print("\n📆 Витрати по днях:")
for day, total in sorted(daily_totals.items()):
    print(f"- {day}: {total:.2f} грн")
    
total_sum = sum(daily_totals.values())
print(f"\n🔸 Загальна сума: {total_sum:.2f} грн")

