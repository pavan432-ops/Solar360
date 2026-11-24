
import csv
import random
from datetime import date, timedelta

random.seed(42)

OUTPUT_FILE = (
    r"C:\Users\user\Solar360\02_Datasets"
    r"\support_tickets_generated.csv"
)

TOTAL_RECORDS = 795

categories = [
    "Installation",
    "Technical Issue",
    "Maintenance",
    "Billing",
    "Other"
]

priorities = ["Low", "Medium", "High", "Critical"]

statuses = [
    "Open",
    "In Progress",
    "On Hold",
    "Resolved",
    "Closed"
]

start_date = date(2025, 1, 1)
end_date = date(2026, 11, 16)
date_range = (end_date - start_date).days

rows = []

for _ in range(TOTAL_RECORDS):
    customer_id = random.randint(1, 2000)

    # Link some tickets to an existing installation.
    installation_id = (
        random.randint(1, 301)
        if random.random() < 0.60
        else ""
    )

    category = random.choice(categories)
    priority = random.choices(
        priorities,
        weights=[20, 45, 25, 10]
    )[0]

    status = random.choices(
        statuses,
        weights=[25, 20, 10, 25, 20]
    )[0]

    created_at = start_date + timedelta(
        days=random.randint(0, date_range)
    )

    resolution_date = ""

    if status in ["Resolved", "Closed"]:
        resolution_date = (
            created_at
            + timedelta(days=random.randint(1, 30))
        ).isoformat()

    assigned_to = random.choice([1, 2, 3])

    rows.append({
        "customer_id": customer_id,
        "installation_id": installation_id,
        "ticket_category": category,
        "priority": priority,
        "ticket_status": status,
        "issue_description": (
            f"Synthetic {category.lower()} support issue"
        ),
        "assigned_to": assigned_to,
        "created_at": created_at.isoformat(),
        "resolution_date": resolution_date,
        "resolution_notes": (
            "Synthetic resolution details"
            if resolution_date else ""
        )
    })

with open(
    OUTPUT_FILE,
    "w",
    newline="",
    encoding="utf-8"
) as file:
    writer = csv.DictWriter(
        file,
        fieldnames=rows[0].keys()
    )
    writer.writeheader()
    writer.writerows(rows)

print("Support ticket dataset generated successfully.")
print(f"Total records: {len(rows)}")
print(f"Output file: {OUTPUT_FILE}")
