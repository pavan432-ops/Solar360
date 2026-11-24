
import csv
import random
from datetime import date, datetime, timedelta
from pathlib import Path

random.seed(200)

OUTPUT_DIR = Path(r"C:\Users\user\Solar360\02_Datasets")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TOTAL_INSPECTIONS = 1500

inspection_statuses = [
    "Scheduled",
    "In Progress",
    "Completed",
    "Cancelled"
]

property_types = [
    "Residential",
    "Commercial",
    "Industrial"
]

roof_types = [
    "Concrete",
    "Metal Sheet",
    "Tiled",
    "Asbestos Sheet"
]

start_date = date(2025, 1, 1)
end_date = date(2026, 11, 16)
date_range = (end_date - start_date).days

file_path = OUTPUT_DIR / "inspections_generated.csv"

with file_path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "lead_id",
        "inspection_date",
        "inspection_status",
        "property_type",
        "roof_type",
        "available_roof_area",
        "proposed_capacity_kw",
        "inspection_notes",
        "inspected_by"
    ])

    for i in range(TOTAL_INSPECTIONS):
        lead_id = random.randint(1, 3006)
        inspection_status = random.choice(inspection_statuses)
        property_type = random.choice(property_types)
        roof_type = random.choice(roof_types)

        inspection_day = start_date + timedelta(
            days=random.randint(0, date_range)
        )

        inspection_datetime = datetime.combine(
            inspection_day,
            datetime.min.time()
        ) + timedelta(
            hours=random.randint(9, 16),
            minutes=random.choice([0, 15, 30, 45])
        )

        roof_area = round(random.uniform(500, 6000), 2)
        proposed_capacity = round(roof_area / random.uniform(220, 260), 2)

        writer.writerow([
            lead_id,
            inspection_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            inspection_status,
            property_type,
            roof_type,
            roof_area,
            proposed_capacity,
            f"{property_type} property inspection record {i + 1}",
            random.randint(1, 3)
        ])

print("Site Inspections dataset generated successfully.")
print(f"Total generated records: {TOTAL_INSPECTIONS}")
print(f"File location: {file_path}")
