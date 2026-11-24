
import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(300)

OUTPUT_DIR = Path(r"C:\Users\user\Solar360\02_Datasets")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TOTAL_QUOTATIONS = 1495

quotation_statuses = [
    "Draft",
    "Sent",
    "Approved",
    "Rejected",
    "Expired"
]

start_date = date(2025, 1, 1)
end_date = date(2026, 11, 16)
date_range = (end_date - start_date).days

file_path = OUTPUT_DIR / "quotations_generated.csv"

with file_path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "lead_id",
        "quotation_amount",
        "proposed_capacity_kw",
        "quotation_status",
        "prepared_by",
        "created_date",
        "sent_date",
        "decision_date",
        "quotation_notes"
    ])

    for i in range(TOTAL_QUOTATIONS):
        lead_id = random.randint(1, 3006)
        capacity = round(random.uniform(2, 25), 2)
        amount = round(capacity * random.uniform(65000, 85000), 2)
        status = random.choice(quotation_statuses)

        created_date = start_date + timedelta(
            days=random.randint(0, date_range)
        )

        sent_date = ""
        decision_date = ""

        if status in ["Sent", "Approved", "Rejected", "Expired"]:
            sent_date = (
                created_date + timedelta(days=random.randint(0, 5))
            ).isoformat()

        if status in ["Approved", "Rejected"]:
            decision_date = (
                date.fromisoformat(sent_date)
                + timedelta(days=random.randint(1, 15))
            ).isoformat()

        writer.writerow([
            lead_id,
            amount,
            capacity,
            status,
            random.randint(1, 3),
            created_date.isoformat(),
            sent_date,
            decision_date,
            f"Synthetic quotation record {i + 1}"
        ])

print("Quotations dataset generated successfully.")
print(f"Total generated records: {TOTAL_QUOTATIONS}")
print(f"File location: {file_path}")
