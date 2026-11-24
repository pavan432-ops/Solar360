
import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(100)

OUTPUT_DIR = Path(r"C:\Users\user\Solar360\02_Datasets")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TOTAL_LEADS = 3000

lead_sources = [
    "Website",
    "Phone",
    "Marketing Campaign",
    "Referral"
]

lead_statuses = [
    "New",
    "Assigned",
    "Contacted",
    "Qualified",
    "Converted",
    "Lost"
]

start_date = date(2025, 1, 1)
end_date = date(2026, 11, 16)
date_range = (end_date - start_date).days

file_path = OUTPUT_DIR / "leads_generated.csv"

with file_path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "customer_id",
        "lead_source",
        "lead_status",
        "follow_up_date",
        "created_at",
        "executive_id"
    ])

    for i in range(TOTAL_LEADS):
        customer_id = random.randint(1, 2000)
        lead_source = random.choice(lead_sources)
        lead_status = random.choice(lead_statuses)
        executive_id = random.randint(1, 3)

        created_date = start_date + timedelta(
            days=random.randint(0, date_range)
        )

        if lead_status == "Lost":
            follow_up_date = ""
        else:
            follow_up_date = (
                created_date + timedelta(days=random.randint(1, 30))
            ).isoformat()

        writer.writerow([
            customer_id,
            lead_source,
            lead_status,
            follow_up_date,
            created_date.isoformat(),
            executive_id
        ])

print("Leads dataset generated successfully.")
print(f"Total generated records: {TOTAL_LEADS}")
print(f"File location: {file_path}")
