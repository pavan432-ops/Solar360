# Solar360 – API Specification

**Project:** Solar360 Customer and Installation Management Platform  
**Document Version:** 1.0  
**Status:** Draft  
**API Architecture:** REST API  
**Data Format:** JSON  
**Base URL:** `http://localhost:8000/api/v1`

---

## 1. Introduction

This document defines the proposed technical specifications for the Solar360 REST APIs.

It describes API endpoints, HTTP methods, request parameters, request bodies, response structures, validation rules and expected status codes.

The APIs will support communication between the following platform modules:

- Customer Management
- Lead Management
- Follow-up Management
- Site Inspection Management
- Quotation Management
- Installation Management
- Support Ticket Management
- Dashboard Reporting

**Note:** These APIs are proposed for the Solar360 portfolio case study. They have not yet been implemented.

## 2. API Standards

| Attribute | Specification |
|---|---|
| Architecture | REST |
| Protocol | HTTP / HTTPS |
| Data format | JSON |
| API version | v1 |
| Naming convention | Lowercase, plural resource names |
| Authentication | Bearer Token (proposed) |
| Database | MySQL |
| Date format | YYYY-MM-DD |
| Date-time format | ISO 8601 |
| Character encoding | UTF-8 |

## 3. Customer Management APIs

### API-001: Register Customer

- **Method:** POST
- **Endpoint:** `/customers`
- **Purpose:** Register a new customer.

Request Body:

```json
{
  "customer_name": "Rahul Sharma",
  "phone": "9876543210",
  "email": "rahul@example.com",
  "city": "Hyderabad",
  "state": "Telangana"
}
```

Expected Response: `201 Created`

```json
{
  "status": "success",
  "message": "Customer registered successfully",
  "data": {
    "customer_id": 2001,
    "customer_name": "Rahul Sharma",
    "phone": "9876543210"
  }
}
```

### API-002: Retrieve All Customers

- **Method:** GET
- **Endpoint:** `/customers`
- **Purpose:** Retrieve customer records.

Query Parameters:
- `page`: Page number.
- `limit`: Number of records.
- `city`: Filter by city.

Expected Response: `200 OK`

### API-003: Retrieve Customer by ID

- **Method:** GET
- **Endpoint:** `/customers/{customer_id}`
- **Purpose:** Retrieve an individual customer record.

Expected Response: `200 OK`

### API-004: Update Customer

- **Method:** PUT
- **Endpoint:** `/customers/{customer_id}`
- **Purpose:** Update customer information.

Request Body:

```json
{
  "customer_name": "Rahul Sharma",
  "phone": "9876543210",
  "email": "rahul.sharma@example.com",
  "city": "Hyderabad",
  "state": "Telangana"
}
```

Expected Response: `200 OK`

## 4. Lead Management APIs

### API-005: Create Lead

- **Method:** POST
- **Endpoint:** `/leads`
- **Purpose:** Create a new sales lead.

Request Body:

```json
{
  "customer_id": 2001,
  "lead_source": "Website",
  "lead_status": "New"
}
```

Expected Response: `201 Created`

### API-006: Retrieve All Leads

- **Method:** GET
- **Endpoint:** `/leads`
- **Purpose:** Retrieve lead records.

Query Parameters:
- `lead_status`
- `lead_source`
- `executive_id`
- `page`
- `limit`

Expected Response: `200 OK`

### API-007: Retrieve Lead by ID

- **Method:** GET
- **Endpoint:** `/leads/{lead_id}`
- **Purpose:** Retrieve lead information.

Expected Response: `200 OK`

### API-008: Update Lead

- **Method:** PUT
- **Endpoint:** `/leads/{lead_id}`
- **Purpose:** Update lead status and information.

Request Body:

```json
{
  "lead_status": "Contacted",
  "follow_up_date": "2026-11-25"
}
```

Expected Response: `200 OK`

### API-009: Assign Sales Executive

- **Method:** PUT
- **Endpoint:** `/leads/{lead_id}/assign`
- **Purpose:** Assign a lead to a sales executive.

Request Body:

```json
{
  "executive_id": 1,
  "follow_up_date": "2026-11-25"
}
```

Expected Response: `200 OK`

## 5. Follow-up Management APIs

### API-010: Record Follow-up

- **Method:** POST
- **Endpoint:** `/leads/{lead_id}/follow-ups`
- **Purpose:** Record customer communication and follow-up activity.

Request Body:

```json
{
  "executive_id": 1,
  "follow_up_type": "Call",
  "discussion_notes": "Customer is interested in a rooftop solar installation.",
  "follow_up_status": "Completed",
  "next_follow_up_date": "2026-11-28"
}
```

Expected Response: `201 Created`

### API-011: Retrieve Follow-up History

- **Method:** GET
- **Endpoint:** `/leads/{lead_id}/follow-ups`
- **Purpose:** Retrieve follow-up history for a lead.

Expected Response: `200 OK`

### API-012: Retrieve Overdue Follow-ups

- **Method:** GET
- **Endpoint:** `/follow-ups/overdue`
- **Purpose:** Identify leads with overdue follow-up dates.

Expected Response: `200 OK`

## 6. Site Inspection APIs

### API-013: Schedule Site Inspection

- **Method:** POST
- **Endpoint:** `/inspections`
- **Purpose:** Schedule a site inspection for a lead.

Request Body:

```json
{
  "lead_id": 1001,
  "inspection_date": "2026-11-28",
  "inspection_status": "Scheduled",
  "inspection_address": "Madhapur, Hyderabad"
}
```

Expected Response: `201 Created`

### API-014: Retrieve Inspections

- **Method:** GET
- **Endpoint:** `/inspections`
- **Purpose:** Retrieve inspection records.

Query Parameters:
- `inspection_status`
- `lead_id`
- `page`
- `limit`

Expected Response: `200 OK`

### API-015: Update Inspection

- **Method:** PUT
- **Endpoint:** `/inspections/{inspection_id}`
- **Purpose:** Update inspection details and status.

Expected Response: `200 OK`

## 7. Quotation Management APIs

### API-016: Create Quotation

- **Method:** POST
- **Endpoint:** `/quotations`
- **Purpose:** Create a quotation for a lead.

Request Body:

```json
{
  "lead_id": 1001,
  "proposed_capacity_kw": 5.0,
  "quotation_amount": 350000,
  "quotation_status": "Pending"
}
```

Expected Response: `201 Created`

### API-017: Update Quotation Decision

- **Method:** PUT
- **Endpoint:** `/quotations/{quotation_id}/status`
- **Purpose:** Record quotation approval or rejection.

Request Body:

```json
{
  "quotation_status": "Approved"
}
```

Expected Response: `200 OK`

## 8. Installation Management APIs

### API-018: Schedule Installation

- **Method:** POST
- **Endpoint:** `/installations`
- **Purpose:** Schedule installation against an approved quotation.

Request Body:

```json
{
  "quotation_id": 501,
  "scheduled_date": "2026-12-05",
  "installation_address": "Madhapur, Hyderabad",
  "installation_team": "Team A"
}
```

Expected Response: `201 Created`

### API-019: Retrieve Installations

- **Method:** GET
- **Endpoint:** `/installations`
- **Purpose:** Retrieve installation records.

Query Parameters:
- `installation_status`
- `installation_team`
- `scheduled_date`
- `page`
- `limit`

Expected Response: `200 OK`

### API-020: Update Installation Progress

- **Method:** PUT
- **Endpoint:** `/installations/{installation_id}`
- **Purpose:** Update installation progress and status.

Request Body:

```json
{
  "installation_status": "In Progress",
  "actual_start_date": "2026-12-05",
  "installation_notes": "Installation work started."
}
```

Expected Response: `200 OK`

## 9. Support Ticket APIs

### API-021: Create Support Ticket

- **Method:** POST
- **Endpoint:** `/tickets`
- **Purpose:** Register a customer complaint or support request.

Request Body:

```json
{
  "customer_id": 2001,
  "installation_id": 301,
  "ticket_category": "Installation Issue",
  "ticket_priority": "High",
  "ticket_description": "Customer reported an installation issue."
}
```

Expected Response: `201 Created`

### API-022: Retrieve Support Tickets

- **Method:** GET
- **Endpoint:** `/tickets`
- **Purpose:** Retrieve support ticket records.

Query Parameters:
- `ticket_status`
- `ticket_priority`
- `customer_id`
- `page`
- `limit`

Expected Response: `200 OK`

### API-023: Update Support Ticket

- **Method:** PUT
- **Endpoint:** `/tickets/{ticket_id}`
- **Purpose:** Update ticket status and resolution information.

Request Body:

```json
{
  "ticket_status": "Resolved",
  "resolution_date": "2026-12-08",
  "resolution_notes": "Issue resolved after technical inspection."
}
```

Expected Response: `200 OK`

## 10. Dashboard Reporting APIs

These APIs will provide data for the Solar360 management reporting interface.

The reporting interface and charts will be developed using Python and VS Code.

### API-024: Dashboard Summary

- **Method:** GET
- **Endpoint:** `/dashboard/summary`
- **Purpose:** Retrieve consolidated business KPIs.

Expected KPI fields:

- Total customers
- Total leads
- Converted leads
- Total site inspections
- Total installations
- Pending installations
- Open support tickets

Expected Response: `200 OK`

### API-025: Lead Performance

- **Method:** GET
- **Endpoint:** `/dashboard/lead-performance`
- **Purpose:** Retrieve lead performance data.

Expected data:
- Leads by status
- Leads by source
- Lead conversion rate
- Executive-wise lead distribution

Expected Response: `200 OK`

### API-026: Installation Performance

- **Method:** GET
- **Endpoint:** `/dashboard/installation-performance`
- **Purpose:** Retrieve installation performance data.

Expected data:
- Installations by status
- Team-wise installation performance
- Completed installations
- Pending installations
- Average installation completion duration

Expected Response: `200 OK`

### API-027: Support Performance

- **Method:** GET
- **Endpoint:** `/dashboard/support-performance`
- **Purpose:** Retrieve support performance data.

Expected data:
- Total support tickets
- Tickets by status
- Tickets by priority
- Average ticket resolution time

Expected Response: `200 OK`

## 11. Standard Response Structure

### 11.1 Successful Response

```json
{
  "status": "success",
  "message": "Request processed successfully",
  "data": {}
}
```

### 11.2 Error Response

```json
{
  "status": "error",
  "status_code": 400,
  "message": "Validation failed",
  "details": "Customer phone number is required"
}
```

## 12. HTTP Status Codes

| Status Code | Meaning | Usage |
|---|---|---|
| 200 | OK | Successful retrieval or update |
| 201 | Created | Resource created successfully |
| 400 | Bad Request | Invalid request data |
| 401 | Unauthorized | Authentication required or invalid |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Resource does not exist |
| 409 | Conflict | Duplicate or conflicting data |
| 422 | Unprocessable Entity | Business validation failure |
| 500 | Internal Server Error | Unexpected server error |

## 13. API Validation Rules

| Validation ID | Rule |
|---|---|
| VAL-001 | Customer phone number is mandatory and unique. |
| VAL-002 | Lead must reference an existing customer. |
| VAL-003 | Lead source must be valid. |
| VAL-004 | Assigned active leads must have a follow-up date. |
| VAL-005 | Sales executive ID must be valid. |
| VAL-006 | Follow-up must reference an existing lead. |
| VAL-007 | Inspection must reference an existing lead. |
| VAL-008 | Quotation must reference an existing lead. |
| VAL-009 | Installation requires an approved quotation. |
| VAL-010 | An installation quotation can be used only once. |
| VAL-011 | Resolved support tickets require a resolution date. |
| VAL-012 | Installation completion date cannot precede actual start date. |
| VAL-013 | Feedback ratings must be between 1 and 5. |

## 14. Authentication and Authorization

The proposed API will use token-based authentication.

Expected authorization requirements:

- Administrator: Full platform access.
- Sales Executive: Customer, lead and follow-up operations within assigned permissions.
- Inspection Team: Inspection operations.
- Installation Team: Installation operations.
- Support Executive: Support ticket operations.
- Management: Read-only access to management reports.

Unauthorized users must not access protected resources.

## 15. Pagination and Filtering

For list endpoints, pagination should be supported.

Example:

`GET /api/v1/leads?page=1&limit=20&lead_status=New`

Expected response structure:

```json
{
  "status": "success",
  "data": [],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total_records": 300,
    "total_pages": 15
  }
}
```

## 16. API Security Requirements

- Use HTTPS in production.
- Protect sensitive endpoints through authentication.
- Enforce role-based authorization.
- Validate and sanitize incoming data.
- Avoid exposing passwords, tokens or sensitive information in responses.
- Use secure error handling.
- Maintain audit records for important operations.

## 17. API Testing Requirements

The proposed APIs will be tested using Postman.

Testing will cover:

1. Successful API requests.
2. Invalid request data.
3. Missing mandatory fields.
4. Duplicate customer records.
5. Invalid customer and lead IDs.
6. Unauthorized access.
7. Invalid business operations.
8. HTTP status code validation.
9. Response body validation.
10. Data consistency between API operations and MySQL.

## 18. Assumptions and Limitations

- All endpoint definitions are proposed, not implemented.
- Request and response examples are illustrative.
- Authentication implementation is pending.
- API framework and deployment architecture are yet to be finalized.
- API testing will begin after endpoint implementation.
- Dashboard reporting will be developed separately using Python-based reporting tools in VS Code.
- All project data is synthetic.

## 19. Document Status

| Attribute | Details |
|---|---|
| Project | Solar360 |
| Document | API Specification |
| Version | 1.0 |
| Status | Draft |
| Prepared For | Solar360 Portfolio Case Study |
| Approval | Pending Review |
