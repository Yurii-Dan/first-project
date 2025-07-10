import csv
from collections import defaultdict
from datetime import datetime
import matplotlib.pyplot as plt
import os
# Знаходимо шлях до поточної директорії (де лежить цей скрипт)
current_dir = os.path.dirname(__file__)
csv_path = os.path.join(current_dir, 'expenses.csv')

# 1. Зчитуємо дані з CSV
daily_totals = defaultdict(float)
category_totals = defaultdict(float)
with open(csv_path, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        name, cost_str, date_str = row
        try:
            date_obj = datetime.strptime(date_str.strip(), "%Y-%m-%d %H:%M")
            date_only = date_obj.date()
            daily_totals[date_only] += float(cost_str)
            category_totals[name.strip()] += float(cost_str)
        except ValueError:
            print("Пропущено рядок:", row)

# 2. Сортуємо дати та суми
dates = sorted(daily_totals.keys())
sums = [daily_totals[date] for date in dates]

# 3. Побудова графіка
plt.figure(figsize=(10, 5))
plt.plot(dates, sums, marker='o', linestyle='-', color='blue')
plt.title("Щоденні витрати")
plt.xlabel("Дата")
plt.ylabel("Сума (грн)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Побудова кругової діаграми
labels = category_totals.keys()
sizes = category_totals.values()

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Витрати за категоріями")
plt.axis('equal')  # Забезпечує круглу форму
plt.tight_layout()
plt.show()