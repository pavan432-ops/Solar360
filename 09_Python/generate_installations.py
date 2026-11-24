
import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(400)

OUTPUT_DIR = Path(r"C:\Users\user\Solar360\02_Datasets")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TOTAL_INSTALLATIONS = 299

installation_statuses = [
    "Scheduled",
    "In Progress",
    "Completed",
    "On Hold",
    "Cancelled"
]

start_date = date(2025, 1, 1)
end_date = date(2026, 11, 16)
date_range = (end_date - start_date).days

teams = [
    "Installation Team A",
    "Installation Team B",
    "Installation Team C",
    "Installation Team D"
]

cities = [
    "Hyderabad",
    "Vijayawada",
    "Bengaluru",
    "Ahmedabad",
    "Chennai",
    "Pune",
    "Mumbai",
    "Delhi",
    "Jaipur",
    "Kochi"
]

file_path = OUTPUT_DIR / "installations_generated.csv"

with file_path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "quotation_id",
        "installation_status",
        "scheduled_date",
        "actual_start_date",
        "completion_date",
        "installation_address",
        "installation_team",
        "installation_notes"
    ])

    for i in range(TOTAL_INSTALLATIONS):
        installation_status = random.choice(installation_statuses)

        scheduled_date = start_date + timedelta(
            days=random.randint(0, date_range)
        )

        actual_start_date = ""
        completion_date = ""

        if installation_status in [
            "In Progress", "Completed", "On Hold"
        ]:
            actual_start_date = (
                scheduled_date + timedelta(days=random.randint(0, 7))
            ).isoformat()

        if installation_status == "Completed":
            completion_date = (
                date.fromisoformat(actual_start_date)
                + timedelta(days=random.randint(1, 15))
            ).isoformat()

        city = random.choice(cities)

        writer.writerow([
            "",  # Quotation ID will be assigned from approved quotations
            installation_status,
            scheduled_date.isoformat(),
            actual_start_date,
            completion_date,
            f"{random.randint(1, 999)}, Solar Street, {city}",
            random.choice(teams),
            f"Synthetic installation record {i + 1}"
        ])

print("Installation dataset template generated successfully.")
print(f"Total records: {TOTAL_INSTALLATIONS}")
print(f"File location: {file_path}")
