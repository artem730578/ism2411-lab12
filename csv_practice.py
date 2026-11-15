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