# Solar360 – Use Case Specification

**Project:** Solar360 Energy Solutions – Customer & Installation Management Platform  
**Document:** Use Case Specification  
**Version:** 1.0 (Draft)  
**Date:** 17 November 2026  
**Data note:** This is a fictional portfolio case study. All example records are synthetic.

## 1. Purpose

This document describes how the main users are expected to interact with the proposed Solar360 platform. It translates the approved-in-progress business requirements and To-Be process into practical system use cases.

## 2. Actors

| Actor | Responsibility |
|---|---|
| Customer | Submits an enquiry, provides property details, reviews a quotation and gives feedback |
| Sales Executive | Creates and manages leads, contacts customers and records follow-ups |
| Site Executive | Schedules and records site inspections |
| Operations Executive | Prepares quotations and plans installation work |
| Support Executive | Creates, assigns and resolves customer support tickets |
| Manager | Reviews operational reports and performance KPIs |
| Solar360 Platform | Validates data, maintains records and generates reminders and reports |

## 3. Use Case List

| Use Case ID | Use Case | Primary Actor | Related Requirement |
|---|---|---|---|
| UC-01 | Register or update customer | Sales Executive | FR001, FR002 |
| UC-02 | Create and assign lead | Sales Executive | FR003, FR004, FR005 |
| UC-03 | Record customer follow-up | Sales Executive | FR006 |
| UC-04 | Identify overdue follow-ups | Solar360 Platform | FR007 |
| UC-05 | Schedule and record site inspection | Site Executive | FR009, FR010 |
| UC-06 | Prepare and record quotation decision | Operations Executive | BR008 |
| UC-07 | Schedule and track installation | Operations Executive | FR011, FR012 |
| UC-08 | Manage support ticket | Support Executive | FR013, FR014 |
| UC-09 | View business performance dashboard | Manager | FR015 |

## 4. Detailed Use Cases

### UC-01 – Register or Update Customer

- **Primary actor:** Sales Executive
- **Preconditions:** The user is authenticated and has permission to manage customer records.
- **Trigger:** A customer submits a new enquiry or provides updated details.
- **Main flow:**
  1. The sales executive opens the customer registration screen.
  2. The executive enters the customer's name, mandatory phone number and available contact/location details.
  3. The platform validates mandatory fields and checks the phone number for an existing customer record.
  4. If no duplicate is found, the platform saves the customer record and generates a unique customer ID.
  5. The platform confirms that the record has been saved.
- **Alternative flow:** If the phone number already exists, the platform displays the existing customer record and allows the user to review/update it instead of creating a duplicate.
- **Postconditions:** A customer record is available for lead creation.
- **Business rules:** BR012; customer phone number must be unique in the proposed data model.

### UC-02 – Create and Assign Lead

- **Primary actor:** Sales Executive
- **Preconditions:** A customer record exists.
- **Trigger:** A new sales enquiry is received.
- **Main flow:**
  1. The executive selects the customer and creates a lead.
  2. The executive selects the lead source.
  3. The platform generates a unique Lead ID.
  4. The executive assigns the lead to an active sales executive.
  5. The executive sets the initial follow-up date.
  6. The platform saves the lead and assignment.
- **Alternative flow:** If a possible duplicate lead is identified, the platform alerts the user to review the existing lead before proceeding.
- **Postconditions:** The lead is stored with a unique ID, source, status and owner.
- **Business rules:** BR001, BR002, BR003 and BR004.

### UC-03 – Record Customer Follow-up

- **Primary actor:** Assigned Sales Executive
- **Preconditions:** The lead exists and is assigned to the executive.
- **Trigger:** The executive contacts the customer.
- **Main flow:**
  1. The executive opens the assigned lead.
  2. The executive records the follow-up date, type, discussion notes and outcome.
  3. The executive enters the next follow-up date when another contact is required.
  4. The platform saves the follow-up history and updates the lead's next follow-up date.
- **Alternative flow:** If the customer cannot be reached, the executive records the attempt and selects the appropriate follow-up outcome.
- **Postconditions:** The interaction is available in the lead's follow-up history.

### UC-04 – Identify Overdue Follow-ups

- **Primary actor:** Solar360 Platform
- **Supporting actor:** Sales Executive
- **Preconditions:** Assigned leads have follow-up dates.
- **Trigger:** The platform checks follow-up dates against the current date.
- **Main flow:**
  1. The platform identifies assigned leads whose follow-up date has passed and whose status is still active.
  2. The platform displays these leads in an overdue follow-up list.
  3. The platform makes the overdue items visible to the responsible executive.
  4. The executive reviews and acts on the overdue leads.
- **Postconditions:** Overdue follow-ups are visible for action.
- **Note:** Reminder delivery channel and reminder timing require stakeholder confirmation.

### UC-05 – Schedule and Record Site Inspection

- **Primary actor:** Site Executive
- **Preconditions:** A qualified lead is available for inspection.
- **Trigger:** The sales team requests a site inspection.
- **Main flow:**
  1. The site executive opens the qualified lead.
  2. The executive selects an inspection date and assigns an inspector.
  3. The platform saves the inspection schedule.
  4. The inspector conducts the site visit.
  5. The inspector records property type, roof type, available roof area, proposed capacity and inspection notes.
  6. The inspector updates the inspection status.
- **Postconditions:** Inspection schedule and findings are stored against the lead.
- **Business rules:** BR006 and BR007.

### UC-06 – Prepare and Record Quotation Decision

- **Primary actor:** Operations Executive
- **Supporting actor:** Customer
- **Preconditions:** Site inspection details are available.
- **Trigger:** Inspection findings are ready for commercial review.
- **Main flow:**
  1. The operations executive reviews inspection findings.
  2. The executive prepares the quotation amount and proposed system capacity.
  3. The quotation is saved and sent to the customer.
  4. The customer reviews and communicates a decision.
  5. The executive records the quotation status and decision date.
- **Alternative flow:** If the customer rejects the quotation or requests changes, the executive records the rejection or prepares a revised quotation according to the agreed business process.
- **Postconditions:** The quotation has a recorded status and decision history.
- **Business rule:** BR008 – installation can be created only after quotation approval.

### UC-07 – Schedule and Track Installation

- **Primary actor:** Operations Executive
- **Preconditions:** An approved quotation exists.
- **Trigger:** The customer accepts the quotation and installation planning begins.
- **Main flow:**
  1. The operations executive selects the approved quotation.
  2. The executive enters the installation address and scheduled date.
  3. The executive assigns an installation team.
  4. The platform validates that the quotation is approved and that no installation already exists for it.
  5. The platform creates the installation record.
  6. The operations executive updates progress, actual start date and completion date as work proceeds.
- **Alternative flow:** If the quotation is not approved, the platform prevents installation creation and displays a validation message.
- **Postconditions:** Installation status and schedule are available for operational tracking.
- **Business rules:** BR008 and BR009.

### UC-08 – Manage Support Ticket

- **Primary actor:** Support Executive
- **Preconditions:** A customer record exists.
- **Trigger:** A customer reports an issue or requests assistance.
- **Main flow:**
  1. The support executive creates a ticket against the customer.
  2. The executive selects category and priority and records the issue description.
  3. The executive optionally links the ticket to an installation.
  4. The ticket is assigned to an owner.
  5. The owner updates the ticket status and adds resolution notes.
  6. When resolved, the owner records the resolution date and closes the ticket according to the support process.
- **Postconditions:** Ticket status, ownership and resolution details are available for tracking.
- **Business rules:** BR010 and BR011.

### UC-09 – View Business Performance Dashboard

- **Primary actor:** Manager
- **Preconditions:** The manager has permission to view reports and relevant records have been captured.
- **Trigger:** The manager opens the reporting dashboard.
- **Main flow:**
  1. The manager opens the dashboard.
  2. The platform displays agreed operational KPIs.
  3. The manager reviews lead conversion, inspection progress, installation status and support-ticket performance.
  4. The manager filters or drills into available operational details.
- **Postconditions:** The manager can review current operational performance and identify areas requiring action.
- **Note:** KPI definitions, refresh frequency and access rules require stakeholder confirmation.

## 5. Assumptions and Items Requiring Confirmation

1. The platform will use role-based access for the actors listed above.
2. Customer phone number is treated as a unique identifier for the initial customer duplicate check; stakeholders must confirm whether additional matching fields are needed.
3. Reminder channel, timing and escalation rules are not yet defined.
4. The quotation revision/versioning process needs confirmation.
5. Installation cancellation, rescheduling and on-hold approval rules need confirmation.
6. Support response and resolution targets (SLAs) need confirmation.
7. Dashboard KPI formulas, date filters and refresh frequency need confirmation.
8. The use cases describe the proposed product behaviour; they do not claim that a deployed application currently implements these functions.

## 6. Traceability and Next Step

These use cases connect the To-Be process to the functional requirements and business rules. The next analysis activity is to convert the use cases into solution specifications, including screen-level fields, validations, status transitions and API requirements.

**Document status:** Draft – for stakeholder review.
