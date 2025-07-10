import csv
from datetime import datetime
import os
# Дізнаємось шлях до папки, де лежить сам скрипт
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'expenses.csv')
expenses = []

while True:
    entry = input("Введіть витрати (назва сума), або 'stop' для завершення: ")
    if entry.lower() == "stop":
        break

    parts = entry.split()
    if len(parts) < 2:
        print("❗ Помилка: введіть назву і суму через пробіл")
        continue

    name = " ".join(parts[:-1])
    try:
        cost = float(parts[-1])
    except ValueError:
        print("❗ Помилка: сума повинна бути числом")
        continue

    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    expenses.append((name, cost, date))

    # Запис рядка у CSV
    with open(file_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([name, cost, date])

print("\n🔸 Витрати:")
total = 0
for name, cost, date in expenses:
    print(f"- {name}: {cost:.2f} грн | {date}")
    total += cost

print(f"\n🔹 Загальна сума: {total:.2f} грн")
