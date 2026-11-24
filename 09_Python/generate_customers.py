
import csv
import random
from pathlib import Path

random.seed(42)

OUTPUT_DIR = Path(r"C:\Users\user\Solar360\02_Datasets")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

first_names = [
    "Aarav", "Aditya", "Arjun", "Rahul", "Kiran",
    "Priya", "Sneha", "Ananya", "Divya", "Kavya",
    "Rohan", "Vikram", "Meera", "Pooja", "Sanjay"
]

last_names = [
    "Sharma", "Reddy", "Kumar", "Patel", "Rao",
    "Verma", "Singh", "Gupta", "Nair", "Das"
]

cities = [
    ("Hyderabad", "Telangana"),
    ("Vijayawada", "Andhra Pradesh"),
    ("Visakhapatnam", "Andhra Pradesh"),
    ("Bengaluru", "Karnataka"),
    ("Chennai", "Tamil Nadu"),
    ("Pune", "Maharashtra"),
    ("Mumbai", "Maharashtra"),
    ("Ahmedabad", "Gujarat"),
    ("Jaipur", "Rajasthan"),
    ("Kochi", "Kerala")
]

file_path = OUTPUT_DIR / "customers_generated.csv"

with file_path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "customer_name",
        "phone",
        "email",
        "city",
        "state"
    ])

    for i in range(6, 2001):
        first = random.choice(first_names)
        last = random.choice(last_names)
        city, state = random.choice(cities)

        writer.writerow([
            f"{first} {last}",
            f"98765{i:05d}",
            f"customer{i}@example.com",
            city,
            state
        ])

print("Customer dataset generated successfully.")
print("Total generated records: 1995")
print(f"File location: {file_path}")
