
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from mysql.connector import IntegrityError
from database import get_db_connection

router = APIRouter(prefix="/api/v1/leads", tags=["Leads"])


# Request validation model for creating a lead
class LeadCreate(BaseModel):
    customer_id: int = Field(gt=0)

    lead_source: str = Field(
        pattern="^(Website|Phone|Marketing Campaign|Referral)$"
    )

    lead_status: str = Field(
        default="New",
        pattern="^(New|Assigned|Contacted|Qualified|Converted|Lost)$"
    )

    follow_up_date: Optional[str] = None
    executive_id: Optional[int] = Field(default=None, gt=0)


# Request validation model for updating a lead
class LeadUpdate(BaseModel):
    lead_source: str = Field(
        pattern="^(Website|Phone|Marketing Campaign|Referral)$"
    )

    lead_status: str = Field(
        pattern="^(New|Assigned|Contacted|Qualified|Converted|Lost)$"
    )

    follow_up_date: Optional[str] = None
    executive_id: Optional[int] = Field(default=None, gt=0)


# 1. Create a lead
@router.post("/", status_code=201)
def create_lead(lead: LeadCreate):
    connection = get_db_connection()

    if connection is None:
        raise HTTPException(
            status_code=503,
            detail="Database unavailable"
        )

    cursor = connection.cursor()

    try:
        query = """
            INSERT INTO leads
            (customer_id, lead_source, lead_status, follow_up_date, executive_id)
            VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            lead.customer_id,
            lead.lead_source,
            lead.lead_status,
            lead.follow_up_date,
            lead.executive_id
        )

        cursor.execute(query, values)
        connection.commit()

        return {
            "message": "Lead created successfully",
            "lead_id": cursor.lastrowid
        }

    except IntegrityError:
        connection.rollback()
        raise HTTPException(
            status_code=400,
            detail="Invalid customer or sales executive reference"
        )

    finally:
        cursor.close()
        connection.close()


# 2. Retrieve all leads
@router.get("/")
def get_leads():
    connection = get_db_connection()

    if connection is None:
        raise HTTPException(
            status_code=503,
            detail="Database unavailable"
        )

    cursor = connection.cursor(dictionary=True)

    try:
        query = """
            SELECT
                lead_id,
                customer_id,
                lead_source,
                lead_status,
                follow_up_date,
                created_at,
                executive_id
            FROM leads
            ORDER BY lead_id
        """

        cursor.execute(query)
        return cursor.fetchall()

    finally:
        cursor.close()
        connection.close()


# 3. Retrieve lead by ID
@router.get("/{lead_id}")
def get_lead(lead_id: int):
    connection = get_db_connection()

    if connection is None:
        raise HTTPException(
            status_code=503,
            detail="Database unavailable"
        )

    cursor = connection.cursor(dictionary=True)

    try:
        query = """
            SELECT
                lead_id,
                customer_id,
                lead_source,
                lead_status,
                follow_up_date,
                created_at,
                executive_id
            FROM leads
            WHERE lead_id = %s
        """

        cursor.execute(query, (lead_id,))
        lead = cursor.fetchone()

        if lead is None:
            raise HTTPException(
                status_code=404,
                detail="Lead not found"
            )

        return lead

    finally:
        cursor.close()
        connection.close()


# 4. Update lead
@router.put("/{lead_id}")
def update_lead(lead_id: int, lead: LeadUpdate):
    connection = get_db_connection()

    if connection is None:
        raise HTTPException(
            status_code=503,
            detail="Database unavailable"
        )

    cursor = connection.cursor(dictionary=True)

    try:
        # Check whether the lead exists
        cursor.execute(
            "SELECT lead_id FROM leads WHERE lead_id = %s",
            (lead_id,)
        )

        existing_lead = cursor.fetchone()

        if existing_lead is None:
            raise HTTPException(
                status_code=404,
                detail="Lead not found"
            )

        # Update lead details
        query = """
            UPDATE leads
            SET
                lead_source = %s,
                lead_status = %s,
                follow_up_date = %s,
                executive_id = %s
            WHERE lead_id = %s
        """

        values = (
            lead.lead_source,
            lead.lead_status,
            lead.follow_up_date,
            lead.executive_id,
            lead_id
        )

        cursor.execute(query, values)
        connection.commit()

        return {
            "message": "Lead updated successfully",
            "lead_id": lead_id
        }

    except IntegrityError:
        connection.rollback()
        raise HTTPException(
            status_code=400,
            detail="Invalid sales executive reference"
        )

    finally:
        cursor.close()
        connection.close()
