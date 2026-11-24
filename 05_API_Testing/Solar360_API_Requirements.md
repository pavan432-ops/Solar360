# Solar360 – API Requirements

## 1. Purpose

This document defines the API requirements for the Solar360 Customer and Installation Management Platform.

The APIs will allow different platform modules to exchange information and perform operations related to customers, leads, follow-ups, site inspections, quotations, installations, and support tickets.

## 2. Scope

The API scope includes:

- Customer management
- Lead management
- Sales executive assignment
- Follow-up tracking
- Site inspection management
- Quotation management
- Installation tracking
- Support ticket management
- Management dashboard data

## 3. API Functional Requirements

### FR-API-001: Customer Management
The system shall provide APIs to:
- Register a new customer.
- Retrieve customer details using Customer ID.
- Update existing customer information.
- Retrieve customer records.

### FR-API-002: Lead Management
The system shall provide APIs to:
- Create a new lead.
- Retrieve lead details using Lead ID.
- Update lead information.
- Retrieve leads based on lead status.
- Assign leads to sales executives.

### FR-API-003: Follow-up Management
The system shall provide APIs to:
- Record customer follow-up activities.
- Retrieve follow-up history for a lead.
- Update the next follow-up date.
- Identify overdue follow-ups.

### FR-API-004: Site Inspection Management
The system shall provide APIs to:
- Schedule a site inspection.
- Retrieve inspection details.
- Update inspection status.
- Record inspection results.

### FR-API-005: Quotation Management
The system shall provide APIs to:
- Create a quotation.
- Retrieve quotation details.
- Update quotation information.
- Record quotation approval or rejection.

### FR-API-006: Installation Management
The system shall provide APIs to:
- Schedule an installation.
- Retrieve installation details.
- Update installation status.
- Record installation progress.
- Record installation completion.

### FR-API-007: Support Ticket Management
The system shall provide APIs to:
- Create a support ticket.
- Retrieve ticket details.
- Update ticket status.
- Record ticket resolution details.

### FR-API-008: Dashboard Reporting
The system shall provide APIs to retrieve:
- Total customers and leads.
- Lead status distribution.
- Follow-up performance.
- Site inspection status.
- Installation performance.
- Support ticket status.

## 4. API Business Validations

The APIs must enforce the following business rules before processing requests.

| Validation ID | Validation Requirement | Expected System Behaviour |
|---|---|---|
| API-VAL-001 | Customer phone number is mandatory. | Reject requests with a missing phone number. |
| API-VAL-002 | Customer phone number must be unique. | Reject duplicate customer phone numbers. |
| API-VAL-003 | Every lead must have a valid customer ID. | Reject leads linked to non-existing customers. |
| API-VAL-004 | Every lead must have a valid lead source. | Reject requests with missing or invalid lead sources. |
| API-VAL-005 | An assigned active lead must have a follow-up date. | Reject requests without a follow-up date. |
| API-VAL-006 | A lead must be assigned to a valid sales executive. | Reject invalid executive IDs. |
| API-VAL-007 | Site inspections must be linked to existing leads. | Reject invalid lead references. |
| API-VAL-008 | Installations require approved quotations. | Reject installation requests without quotation approval. |
| API-VAL-009 | A quotation must belong to an existing lead. | Reject invalid lead references. |
| API-VAL-010 | Resolved support tickets must have a resolution date. | Reject incomplete resolution requests. |
| API-VAL-011 | Installation completion date cannot precede the actual start date. | Reject invalid date sequences. |
| API-VAL-012 | Rating values must be between 1 and 5. | Reject ratings outside the permitted range. |

## 5. API Error Handling Requirements

The API must return appropriate HTTP status codes and meaningful error messages.

| HTTP Status Code | Description | Example Scenario |
|---|---|---|
| 200 OK | Request completed successfully. | Customer details retrieved. |
| 201 Created | New resource created successfully. | New customer registered. |
| 400 Bad Request | Request contains invalid or missing information. | Mandatory phone number missing. |
| 401 Unauthorized | User authentication is missing or invalid. | Invalid authentication token. |
| 403 Forbidden | User does not have permission. | Sales executive accessing restricted data. |
| 404 Not Found | Requested resource does not exist. | Customer ID not found. |
| 409 Conflict | Request conflicts with existing data. | Duplicate customer phone number. |
| 500 Internal Server Error | Unexpected server-side error. | Unexpected application failure. |

### 5.1 Standard Error Response

The API should return a consistent error response structure.

Example:

```json
{
  "status": "error",
  "status_code": 400,
  "message": "Validation failed",
  "details": "Customer phone number is required"
}


## 7. Proposed API Endpoint Catalogue

The Solar360 platform will follow a REST API approach. The following endpoints are proposed for the MVP.

| API ID | Module | HTTP Method | Endpoint | Purpose |
|---|---|---|---|---|
| API-001 | Customers | POST | /api/v1/customers | Register a customer |
| API-002 | Customers | GET | /api/v1/customers | Retrieve customer records |
| API-003 | Customers | GET | /api/v1/customers/{id} | Retrieve customer details |
| API-004 | Customers | PUT | /api/v1/customers/{id} | Update customer information |
| API-005 | Leads | POST | /api/v1/leads | Create a new lead |
| API-006 | Leads | GET | /api/v1/leads | Retrieve leads |
| API-007 | Leads | GET | /api/v1/leads/{id} | Retrieve lead details |
| API-008 | Leads | PUT | /api/v1/leads/{id} | Update lead information |
| API-009 | Leads | PUT | /api/v1/leads/{id}/assign | Assign a sales executive |
| API-010 | Follow-ups | POST | /api/v1/leads/{id}/follow-ups | Record a follow-up |
| API-011 | Follow-ups | GET | /api/v1/leads/{id}/follow-ups | Retrieve follow-up history |
| API-012 | Inspections | POST | /api/v1/inspections | Schedule an inspection |
| API-013 | Inspections | GET | /api/v1/inspections | Retrieve inspections |
| API-014 | Inspections | PUT | /api/v1/inspections/{id} | Update inspection details |
| API-015 | Quotations | POST | /api/v1/quotations | Create a quotation |
| API-016 | Quotations | PUT | /api/v1/quotations/{id}/status | Update quotation decision |
| API-017 | Installations | POST | /api/v1/installations | Schedule an installation |
| API-018 | Installations | GET | /api/v1/installations | Retrieve installations |
| API-019 | Installations | PUT | /api/v1/installations/{id} | Update installation progress |
| API-020 | Support | POST | /api/v1/tickets | Create a support ticket |
| API-021 | Support | GET | /api/v1/tickets | Retrieve support tickets |
| API-022 | Support | PUT | /api/v1/tickets/{id} | Update ticket information |
| API-023 | Dashboard | GET | /api/v1/dashboard/summary | Retrieve business KPI summary |
| API-024 | Dashboard | GET | /api/v1/dashboard/lead-performance | Retrieve lead performance data |
| API-025 | Dashboard | GET | /api/v1/dashboard/installation-performance | Retrieve installation performance data |

Note: These are proposed endpoint specifications for the portfolio case study, not implemented API routes.

## 8. API Request and Response Requirements

### 8.1 Request Requirements

- APIs must accept structured JSON request bodies where applicable.
- Mandatory fields must be validated.
- IDs must reference existing records.
- Date values must follow the ISO 8601 date format.
- Invalid requests must return appropriate error responses.

### 8.2 Sample Customer Registration Request

```json
{
  "customer_name": "Rahul Sharma",
  "phone": "9876543210",
  "email": "rahul@example.com",
  "city": "Hyderabad",
  "state": "Telangana"
}
```

### 8.3 Sample Successful Response

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

The sample customer information is illustrative and does not represent an actual customer.

## 9. API Access and User Roles

The platform will support role-based access.

| User Role | Expected Access |
|---|---|
| Administrator | Manage customers, leads, users and platform records |
| Sales Executive | View assigned leads and manage follow-ups |
| Inspection Team | View and update assigned site inspections |
| Installation Team | View assigned installations and update progress |
| Support Executive | Create and manage support tickets |
| Management | View business performance reports and KPIs |

Authentication and authorization must be applied before allowing access to protected operations.

## 10. API Integration Requirements

- Customer and lead modules must exchange customer information.
- Lead management must support sales executive assignment.
- Follow-up activities must be linked to their respective leads.
- Site inspections must be linked to valid leads.
- Quotations must be associated with the relevant lead.
- Installation records must reference approved quotations.
- Support tickets must be associated with valid customers.
- Dashboard APIs must provide consolidated information from relevant business modules.

## 11. Assumptions and Constraints

### Assumptions

- The platform will use REST-based APIs.
- JSON will be the standard data exchange format.
- MySQL will serve as the proposed relational database.
- APIs will support the requirements of the Solar360 MVP.
- User authentication and role-based authorization will be required.

### Constraints

- The API implementation is not yet completed.
- Authentication technology and deployment architecture are yet to be finalized.
- API performance must be validated through testing.
- Dashboard reporting will be developed using Python and VS Code rather than Power BI.

## 12. API Requirements Acceptance Criteria

The API requirements will be considered ready for development when:

1. All major business modules have defined API requirements.
2. Proposed endpoints and HTTP methods are documented.
3. Request and response structures are documented.
4. Business validations are defined.
5. Error handling requirements are documented.
6. User roles and access requirements are identified.
7. Integration dependencies between modules are documented.
8. Requirements are traceable to the BRD, FRD and user stories.

## 13. Document Status

| Attribute | Details |
|---|---|
| Project | Solar360 |
| Document | API Requirements |
| Version | 1.0 |
| Status | Draft |
| Prepared For | Solar360 Portfolio Case Study |
| Approval | Pending Review |