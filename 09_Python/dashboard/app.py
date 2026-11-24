import sys
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

API_FOLDER = Path(__file__).resolve().parents[1] / "api"
sys.path.insert(0, str(API_FOLDER))

from database import get_db_connection

st.set_page_config(
    page_title="Solar360 | Management Dashboard",
    page_icon="☀️",
    layout="wide"
)

st.title("☀️ Solar360 Management Dashboard")
st.caption("Customer, Lead & Installation Performance | Portfolio Case Study")

@st.cache_data(ttl=60)
def load_data():
    connection = get_db_connection()
    if connection is None:
        raise ConnectionError("Unable to connect to the Solar360 database.")

    queries = {
        "customers": "SELECT * FROM customers",
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
    finally:
        connection.close()

    return data

try:
    data = load_data()
except Exception as error:
    st.error(f"Database connection or data loading failed: {error}")
    st.stop()

customers = data["customers"]
leads = data["leads"]
inspections = data["inspections"]
quotations = data["quotations"]
installations = data["installations"]
tickets = data["tickets"]
feedback = data["feedback"]

def count_status(df, column, status):
    if df.empty:
        return 0
    return int((df[column] == status).sum())

total_customers = len(customers)
total_leads = len(leads)
converted_leads = count_status(leads, "lead_status", "Converted")
lead_conversion = converted_leads / total_leads * 100 if total_leads else 0

total_installations = len(installations)
completed_installations = count_status(
    installations, "installation_status", "Completed"
)
installation_completion = (
    completed_installations / total_installations * 100
    if total_installations else 0
)

approved_amount = quotations.loc[
    quotations["quotation_status"] == "Approved", "quotation_amount"
].sum()

st.subheader("Executive Overview")

k1, k2, k3, k4 = st.columns(4)
k1.metric("Total Customers", f"{total_customers:,}")
k2.metric("Total Leads", f"{total_leads:,}")
k3.metric("Lead Conversion Rate", f"{lead_conversion:.1f}%")
k4.metric("Total Installations", f"{total_installations:,}")

k5, k6, k7, k8 = st.columns(4)
k5.metric("Completed Installations", f"{completed_installations:,}")
k6.metric("Installation Completion", f"{installation_completion:.1f}%")
k7.metric("Approved Quotation Value", f"₹{approved_amount:,.0f}")
k8.metric("Site Inspections", f"{len(inspections):,}")

st.divider()

st.subheader("Lead Performance")
c1, c2 = st.columns(2)

with c1:
    status_data = leads["lead_status"].value_counts().reset_index()
    status_data.columns = ["Lead Status", "Count"]
    fig = px.bar(
        status_data, x="Lead Status", y="Count",
        title="Leads by Status", text="Count"
    )
    st.plotly_chart(fig, use_container_width=True)

with c2:
    source_data = leads["lead_source"].value_counts().reset_index()
    source_data.columns = ["Lead Source", "Count"]
    fig = px.pie(
        source_data, names="Lead Source", values="Count",
        title="Lead Source Distribution", hole=0.4
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Site Inspection Analysis")
c1, c2 = st.columns(2)

with c1:
    inspection_status = inspections["inspection_status"].value_counts().reset_index()
    inspection_status.columns = ["Inspection Status", "Count"]
    fig = px.bar(
        inspection_status, x="Inspection Status", y="Count",
        title="Inspections by Status", text="Count"
    )
    st.plotly_chart(fig, use_container_width=True)

with c2:
    property_data = inspections["property_type"].value_counts().reset_index()
    property_data.columns = ["Property Type", "Count"]
    fig = px.pie(
        property_data, names="Property Type", values="Count",
        title="Inspections by Property Type", hole=0.4
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Quotation Analysis")
c1, c2 = st.columns(2)

with c1:
    quotation_status = quotations["quotation_status"].value_counts().reset_index()
    quotation_status.columns = ["Quotation Status", "Count"]
    fig = px.bar(
        quotation_status, x="Quotation Status", y="Count",
        title="Quotations by Status", text="Count"
    )
    st.plotly_chart(fig, use_container_width=True)

with c2:
    quotation_values = (
        quotations.groupby("quotation_status", as_index=False)["quotation_amount"]
        .sum()
    )
    fig = px.bar(
        quotation_values, x="quotation_status", y="quotation_amount",
        title="Quotation Value by Status",
        labels={
            "quotation_status": "Quotation Status",
            "quotation_amount": "Amount (₹)"
        }
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Installation Performance")
c1, c2 = st.columns(2)

with c1:
    installation_status = installations[
        "installation_status"
    ].value_counts().reset_index()
    installation_status.columns = ["Installation Status", "Count"]
    fig = px.bar(
        installation_status, x="Installation Status", y="Count",
        title="Installations by Status", text="Count"
    )
    st.plotly_chart(fig, use_container_width=True)

with c2:
    capacity_data = installations.merge(
        quotations[["quotation_id", "proposed_capacity_kw"]],
        on="quotation_id",
        how="left"
    )
    capacity_data = (
        capacity_data.groupby("installation_status", as_index=False)
        ["proposed_capacity_kw"].sum()
    )
    fig = px.bar(
        capacity_data, x="installation_status",
        y="proposed_capacity_kw",
        title="Proposed Solar Capacity by Installation Status",
        labels={
            "installation_status": "Installation Status",
            "proposed_capacity_kw": "Capacity (kW)"
        }
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Customer Support & Feedback")
c1, c2 = st.columns(2)

with c1:
    if not tickets.empty:
        ticket_status = tickets["ticket_status"].value_counts().reset_index()
        ticket_status.columns = ["Ticket Status", "Count"]
        fig = px.bar(
            ticket_status, x="Ticket Status", y="Count",
            title="Support Tickets by Status", text="Count"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No support ticket records available.")

with c2:
    if not feedback.empty:
        average_rating = feedback["rating"].mean()
        st.metric("Average Feedback Rating", f"{average_rating:.2f} / 5")
        feedback_data = feedback["feedback_category"].value_counts().reset_index()
        feedback_data.columns = ["Feedback Category", "Count"]
        fig = px.bar(
            feedback_data, x="Feedback Category", y="Count",
            title="Feedback by Category", text="Count"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No product feedback records available.")

st.divider()

st.subheader("Management Insights")

open_leads = count_status(leads, "lead_status", "New") + count_status(
    leads, "lead_status", "Assigned"
)
pending_inspections = count_status(
    inspections, "inspection_status", "Scheduled"
) + count_status(inspections, "inspection_status", "In Progress")
pending_installations = total_installations - completed_installations

st.write(f"- **New and assigned leads:** {open_leads:,}")
st.write(f"- **Scheduled or in-progress inspections:** {pending_inspections:,}")
st.write(f"- **Installations not marked completed:** {pending_installations:,}")

if not tickets.empty:
    unresolved = len(tickets[
        ~tickets["ticket_status"].isin(["Resolved", "Closed"])
    ])
    st.write(f"- **Support tickets not marked resolved or closed:** {unresolved:,}")

if not feedback.empty:
    st.write(
        f"- **Average customer feedback rating:** "
        f"{feedback['rating'].mean():.2f} out of 5"
    )

st.caption(
    "Data represents a fictional Solar360 portfolio case study. "
    "Support ticket and feedback datasets contain small samples; "
    "interpret those results cautiously. Approved quotation value is "
    "not the same as revenue collected."
)

if st.button("Refresh Dashboard"):
    st.cache_data.clear()
    st.rerun()
