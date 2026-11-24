
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from mysql.connector import IntegrityError
from database import get_db_connection

router = APIRouter(prefix="/api/v1/customers", tags=["Customers"])


# Request validation model
class CustomerCreate(BaseModel):
    customer_name: str = Field(min_length=1, max_length=100)
    phone: str = Field(min_length=1, max_length=15)
    email: Optional[str] = Field(default=None, max_length=100)
    city: Optional[str] = Field(default=None, max_length=50)
    state: Optional[str] = Field(default=None, max_length=50)


class CustomerUpdate(CustomerCreate):
    pass


# 1. Register a customer
@router.post("/", status_code=201)
def create_customer(customer: CustomerCreate):
    connection = get_db_connection()

    if connection is None:
        raise HTTPException(status_code=503, detail="Database unavailable")

    cursor = connection.cursor(dictionary=True)

    try:
        query = """
            INSERT INTO customers
            (customer_name, phone, email, city, state)
            VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            customer.customer_name,
            customer.phone,
            customer.email,
            customer.city,
            customer.state
        )

        cursor.execute(query, values)
        connection.commit()

        return {
            "message": "Customer registered successfully",
            "customer_id": cursor.lastrowid
        }

    except IntegrityError:
        connection.rollback()
        raise HTTPException(
            status_code=409,
            detail="Customer phone number already exists"
        )

    finally:
        cursor.close()
        connection.close()


# 2. Retrieve all customers
@router.get("/")
def get_customers():
    connection = get_db_connection()

    if connection is None:
        raise HTTPException(status_code=503, detail="Database unavailable")

    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM customers ORDER BY customer_id")
        return cursor.fetchall()

    finally:
        cursor.close()
        connection.close()


# 3. Retrieve customer by ID
@router.get("/{customer_id}")
def get_customer(customer_id: int):
    connection = get_db_connection()

    if connection is None:
        raise HTTPException(status_code=503, detail="Database unavailable")

    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute(
            "SELECT * FROM customers WHERE customer_id = %s",
            (customer_id,)
        )

        customer = cursor.fetchone()

        if customer is None:
            raise HTTPException(status_code=404, detail="Customer not found")

        return customer

    finally:
        cursor.close()
        connection.close()


# 4. Update customer
@router.put("/{customer_id}")
def update_customer(customer_id: int, customer: CustomerUpdate):
    connection = get_db_connection()

    if connection is None:
        raise HTTPException(status_code=503, detail="Database unavailable")

    cursor = connection.cursor()

    try:
        query = """
            UPDATE customers
            SET customer_name = %s,
                phone = %s,
                email = %s,
                city = %s,
                state = %s
            WHERE customer_id = %s
        """

        values = (
            customer.customer_name,
            customer.phone,
            customer.email,
            customer.city,
            customer.state,
            customer_id
        )

        cursor.execute(query, values)

        if cursor.rowcount == 0:
            check_cursor = connection.cursor()
            check_cursor.execute(
                "SELECT customer_id FROM customers WHERE customer_id = %s",
                (customer_id,)
            )
            exists = check_cursor.fetchone()
            check_cursor.close()

            if not exists:
                raise HTTPException(
                    status_code=404,
                    detail="Customer not found"
                )

        connection.commit()

        return {"message": "Customer updated successfully"}

    except IntegrityError:
        connection.rollback()
        raise HTTPException(
            status_code=409,
            detail="Customer phone number already exists"
        )

    finally:
        cursor.close()
        connection.close()
