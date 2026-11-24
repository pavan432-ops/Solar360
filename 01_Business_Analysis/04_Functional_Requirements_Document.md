
# Solar360 – Functional Requirements Document (FRD)

## 1. Document Information

- Project Name: Solar360
- Company: Solar360 Energy Solutions (Fictional)
- Document Type: Functional Requirements Document
- Version: 1.0
- Status: Initial Draft
- Prepared By: Junior Product Analyst

## 2. Purpose

This document defines the functional requirements of the
Solar360 Customer and Installation Management Platform.

It describes the system features, expected behaviour and
business workflows required to address the identified
business problems.

## 3. User Roles

1. Administrator
2. Sales Executive
3. Site Engineer
4. Operations Manager
5. Support Executive
6. Customer

## 4. Functional Requirements

### 4.1 Customer Management

**FR001 – Customer Registration**

The system shall allow authorized users to register new
customers with their name, contact number, email and address.

**FR002 – Customer Record Management**

The system shall allow authorized users to view and update
customer information.

### 4.2 Lead Management

**FR003 – Lead Creation**

The system shall allow sales executives to create leads
with customer details, enquiry source and enquiry date.

**FR004 – Unique Lead Identification**

The system shall generate a unique Lead ID for every lead.

**FR005 – Lead Assignment**

The system shall allow authorized users to assign leads
to sales executives.

**FR006 – Follow-up Tracking**

The system shall allow sales executives to record follow-up
dates, notes and lead status.

**FR007 – Pending Follow-up Identification**

The system shall identify leads whose follow-up dates
have passed and whose status is still active.

**FR008 – Lead Status Management**

The system shall support lead statuses such as New,
Assigned, Contacted, Inspection Scheduled, Converted
and Lost.

### 4.3 Site Inspection Management

**FR009 – Inspection Scheduling**

The system shall allow authorized users to schedule
site inspections for eligible leads.

**FR010 – Inspection Status Tracking**

The system shall support Scheduled, Completed,
Rescheduled and Cancelled inspection statuses.

### 4.4 Installation Management

**FR011 – Installation Scheduling**

The system shall allow authorized users to schedule
installations after quotation approval.

**FR012 – Installation Progress Tracking**

The system shall allow operations users to update
installation statuses such as Scheduled, In Progress,
Completed and Delayed.

### 4.5 Customer Support

**FR013 – Support Ticket Creation**

The system shall allow support executives to create
customer support tickets.

**FR014 – Ticket Status Management**

The system shall support Open, In Progress and Resolved
ticket statuses.

### 4.6 Reporting and Analytics

**FR015 – Business Performance Dashboard**

The system shall provide management reports covering
lead conversion, inspection completion, installation
progress and support ticket resolution.

## 5. Non-Functional Requirements

**NFR001 – Access Control**

The platform shall restrict access based on authorized
user roles.

**NFR002 – Performance**

Dashboard pages should load within 3 seconds under
normal operating conditions. This is a proposed target.

**NFR003 – Data Protection**

Customer information shall be protected against
unauthorized access.

**NFR004 – Data Integrity**

The platform shall maintain unique identifiers and
valid relationships between customer, lead, inspection,
installation and support records.

**NFR005 – Auditability**

Important record changes should retain information
about the user and time of the change.

## 6. Business Rules Reference

The functional requirements shall follow the rules
defined in the Business Rules Register:

- BR001 to BR005: Lead Management
- BR006 to BR007: Site Inspection
- BR008 to BR009: Installation
- BR010 to BR011: Support
- BR012: Customer Management

## 7. Assumptions

- This is a fictional portfolio case study.
- All customer and operational data will be synthetic.
- Requirements are proposed and require stakeholder validation.
- Initial implementation will use free development tools.

## 8. Approval Status

- Business Owner: Pending
- Product Owner: Pending
- Development Team: Pending
- Document Status: Draft
