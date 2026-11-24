
import sys
from pathlib import Path

import pandas as pd
import plotly.express as px

# --------------------------------------------------
# 1. DATABASE CONNECTION
# --------------------------------------------------

API_FOLDER = Path(__file__).resolve().parent / "api"
sys.path.insert(0, str(API_FOLDER))

from database import get_db_connection

# --------------------------------------------------
# 2. OUTPUT DIRECTORY
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

OUTPUT_FOLDER = (
    PROJECT_ROOT / "10_Diagrams" / "Dashboard_Charts"
)

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# 3. LOAD DATA FROM MYSQL
# --------------------------------------------------

print("Connecting to Solar360 database...")

connection = get_db_connection()

if connection is None:
    raise ConnectionError(
        "Unable to connect to Solar360 database."
    )

queries = {
    "leads": "SELECT * FROM leads",
    "inspections": "SELECT * FROM site_inspections",
    "quotations": "SELECT * FROM quotations",
    "installations": "SELECT * FROM installations",
    "tickets": "SELECT * FROM support_tickets",
    "feedback": "SELECT * FROM product_feedback"
}

data = {}

try:
    for name, query in queries.items():
        data[name] = pd.read_sql(query, connection)
        print(f"Loaded {name}: {len(data[name])} records")

finally:
    connection.close()

leads = data["leads"]
inspections = data["inspections"]
quotations = data["quotations"]
installations = data["installations"]
tickets = data["tickets"]
feedback = data["feedback"]

# --------------------------------------------------
# 4. COMMON CHART EXPORT FUNCTION
# --------------------------------------------------

def export_chart(fig, filename):

    output_path = OUTPUT_FOLDER / filename

    fig.write_image(
        str(output_path),
        width=1400,
        height=800,
        scale=2
    )

    print(f"Exported: {filename}")


# --------------------------------------------------
# 5. LEAD PERFORMANCE
# --------------------------------------------------

# Chart 1: Leads by Status

status_data = (
    leads["lead_status"]
    .value_counts()
    .reset_index()
)

status_data.columns = ["Lead Status", "Count"]

fig = px.bar(
    status_data,
    x="Lead Status",
    y="Count",
    title="Leads by Status",
    text="Count"
)

export_chart(
    fig,
    "01_Leads_by_Status.png"
)


# Chart 2: Lead Source Distribution

source_data = (
    leads["lead_source"]
    .value_counts()
    .reset_index()
)

source_data.columns = ["Lead Source", "Count"]

fig = px.pie(
    source_data,
    names="Lead Source",
    values="Count",
    title="Lead Source Distribution",
    hole=0.4
)

export_chart(
    fig,
    "02_Lead_Source_Distribution.png"
)


# --------------------------------------------------
# 6. SITE INSPECTION ANALYSIS
# --------------------------------------------------

# Chart 3: Inspections by Status

inspection_status = (
    inspections["inspection_status"]
    .value_counts()
    .reset_index()
)

inspection_status.columns = [
    "Inspection Status",
    "Count"
]

fig = px.bar(
    inspection_status,
    x="Inspection Status",
    y="Count",
    title="Inspections by Status",
    text="Count"
)

export_chart(
    fig,
    "03_Inspections_by_Status.png"
)


# Chart 4: Inspections by Property Type

property_data = (
    inspections["property_type"]
    .value_counts()
    .reset_index()
)

property_data.columns = [
    "Property Type",
    "Count"
]

fig = px.pie(
    property_data,
    names="Property Type",
    values="Count",
    title="Inspections by Property Type",
    hole=0.4
)

export_chart(
    fig,
    "04_Inspections_by_Property_Type.png"
)


# --------------------------------------------------
# 7. QUOTATION ANALYSIS
# --------------------------------------------------

# Chart 5: Quotations by Status

quotation_status = (
    quotations["quotation_status"]
    .value_counts()
    .reset_index()
)

quotation_status.columns = [
    "Quotation Status",
    "Count"
]

fig = px.bar(
    quotation_status,
    x="Quotation Status",
    y="Count",
    title="Quotations by Status",
    text="Count"
)

export_chart(
    fig,
    "05_Quotations_by_Status.png"
)


# Chart 6: Quotation Value by Status

quotation_values = (
    quotations.groupby(
        "quotation_status",
        as_index=False
    )["quotation_amount"].sum()
)

fig = px.bar(
    quotation_values,
    x="quotation_status",
    y="quotation_amount",
    title="Quotation Value by Status",
    labels={
        "quotation_status": "Quotation Status",
        "quotation_amount": "Amount (₹)"
    }
)

export_chart(
    fig,
    "06_Quotation_Value_by_Status.png"
)


# --------------------------------------------------
# 8. INSTALLATION PERFORMANCE
# --------------------------------------------------

# Chart 7: Installations by Status

installation_status = (
    installations["installation_status"]
    .value_counts()
    .reset_index()
)

installation_status.columns = [
    "Installation Status",
    "Count"
]

fig = px.bar(
    installation_status,
    x="Installation Status",
    y="Count",
    title="Installations by Status",
    text="Count"
)

export_chart(
    fig,
    "07_Installations_by_Status.png"
)


# Chart 8: Proposed Solar Capacity by Status

capacity_data = installations.merge(
    quotations[
        ["quotation_id", "proposed_capacity_kw"]
    ],
    on="quotation_id",
    how="left"
)

capacity_data = (
    capacity_data.groupby(
        "installation_status",
        as_index=False
    )["proposed_capacity_kw"].sum()
)

fig = px.bar(
    capacity_data,
    x="installation_status",
    y="proposed_capacity_kw",
    title="Proposed Solar Capacity by Installation Status",
    labels={
        "installation_status": "Installation Status",
        "proposed_capacity_kw": "Capacity (kW)"
    }
)

export_chart(
    fig,
    "08_Solar_Capacity_by_Status.png"
)


# --------------------------------------------------
# 9. CUSTOMER SUPPORT
# --------------------------------------------------

# Chart 9: Support Tickets by Status

if not tickets.empty:

    ticket_status = (
        tickets["ticket_status"]
        .value_counts()
        .reset_index()
    )

    ticket_status.columns = [
        "Ticket Status",
        "Count"
    ]

    fig = px.bar(
        ticket_status,
        x="Ticket Status",
        y="Count",
        title="Support Tickets by Status",
        text="Count"
    )

    export_chart(
        fig,
        "09_Support_Tickets_by_Status.png"
    )

else:
    print("Skipped: No support ticket records.")


# --------------------------------------------------
# 10. CUSTOMER FEEDBACK
# --------------------------------------------------

# Chart 10: Feedback by Category

if not feedback.empty:

    feedback_data = (
        feedback["feedback_category"]
        .value_counts()
        .reset_index()
    )

    feedback_data.columns = [
        "Feedback Category",
        "Count"
    ]

    fig = px.bar(
        feedback_data,
        x="Feedback Category",
        y="Count",
        title="Feedback by Category",
        text="Count"
    )

    export_chart(
        fig,
        "10_Feedback_by_Category.png"
    )

else:
    print("Skipped: No product feedback records.")


# --------------------------------------------------
# 11. COMPLETION SUMMARY
# --------------------------------------------------

exported_files = list(
    OUTPUT_FOLDER.glob("*.png")
)

print("\n================================")
print("SOLAR360 CHART EXPORT COMPLETED")
print("================================")

print(
    f"Total PNG charts available: {len(exported_files)}"
)

print(f"Output folder: {OUTPUT_FOLDER}")
