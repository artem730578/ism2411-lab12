# csv_practice.py
# Author : Artem Chernyshev
# Module 12 Lab: Read a Sales CSV, Write a Cleaned Report

import csv
from datetime import datetime

SALES_FILE = "data/sales.csv" 
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"

print("-- Exercise 1 --")
with open(SALES_FILE, "r") as f:
    print(f"Opened {SALES_FILE}.")

print ("-- Exercise 2 --")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("-- Exercise 3 --")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    header = next(reader)          # take the header row out first
    print("Header:", header)
    for row in reader:             # loop starts at the first data row
        print(row)

print("-- Exercise 4 --")
total_revenue = 0
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)                       # skip header
    for row in reader:
        product = row[0]
        price = float(row[1])          # text -> decimal number
        qty = int(row[2])              # text -> whole number
        line_total = price * qty
        total_revenue += line_total
        print(f"{product}: {qty} units x ${price:.2f} = ${line_total:.2f}")
print(f"Total revenue: ${total_revenue:.2f}")


print("-- Exercise 5 --")
original_count = 0
written_count = 0
with open(SALES_FILE, "r") as f_in, open(CLEANED_FILE, "w", newline="") as f_out:
    reader = csv.reader(f_in)
    writer = csv.writer(f_out)
    next(reader)                                   # skip input header
    writer.writerow(["Product", "Price", "Qty", "Total"])   # output header
    for row in reader:
        original_count += 1
        price = float(row[1])
        qty = int(row[2])
        line_total = price * qty
        if line_total > 100:                       # keep only big orders
            writer.writerow([row[0], price, qty, round(line_total, 2)])
            written_count += 1
print(f"Wrote {written_count} of {original_count} rows to {CLEANED_FILE}")


print("-- Exercise 6 --")
dict_total = 0
with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)                 # each row becomes a dict
    for row in reader:
        line_total = float(row["price"]) * int(row["quantity"])
        dict_total += line_total
        print(f"{row['product']}: ${line_total:.2f}")
print(f"Total revenue: ${dict_total:.2f}")
# csv.reader uses positions like row[1], which is short but breaks if columns move.
# csv.DictReader uses column names like row["price"], which is clearer and safer.

print("-- Exercise 7 --")
summary = {}
with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        line_total = float(row["price"]) * int(row["quantity"])
        summary[product] = summary.get(product, 0) + line_total
for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")


print("-- Exercise 8 --")
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(LOG_FILE, "a") as log:               # "a" = append, keeps old lines
    log.write(f"{now} - Total revenue: ${total_revenue:.2f}\n")
print(f"Logged this run to {LOG_FILE}")