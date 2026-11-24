# Solar360 – User Acceptance Testing (UAT) Report

## 1. Project Information

| Field | Details |
|---|---|
| Project | Solar360 – Customer & Installation Management Platform |
| Backend | FastAPI |
| Database | MySQL |
| Dashboard | Streamlit |
| Environment | Local Development |
| Test Data | Synthetic / Fictional |
| Status | Draft – UAT Partially Completed |

## 2. UAT Objective

Validate customer and lead management workflows, API integration, database persistence, and dashboard data updates.

## 3. UAT Test Scenarios

| Test ID | Scenario | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| UAT-001 | Register customer 2004 | Customer created | Customer created successfully | Passed |
| UAT-002 | Register customer 2005 | Customer created | Customer created successfully | Passed |
| UAT-003 | Update customer 2005 | Customer updated | Customer updated successfully | Passed |
| UAT-004 | Create lead 3008 | Lead created | Lead created successfully | Passed |
| UAT-005 | Update lead 3008 | Lead updated | Lead updated successfully | Passed |
| UAT-006 | Verify customer KPI | Count reflects new records | Dashboard displayed 2,004 | Passed |
| UAT-007 | Verify lead KPI | Count reflects new record | Dashboard displayed 3,008 | Passed |
| UAT-008 | Verify lead status chart | Updated status displayed | Change to Contacted visible | Passed |
| UAT-009 | Verify lead source chart | Updated source displayed | Change to Referral visible | Passed |
| UAT-010 | Verify quotation reporting | Data displayed correctly | Not yet verified | Not Tested |
| UAT-011 | Verify inspection reporting | Data displayed correctly | Not yet verified | Not Tested |
| UAT-012 | Verify installation reporting | Data displayed correctly | Not yet verified | Not Tested |
| UAT-013 | Verify support reporting | Data displayed correctly | Not yet verified | Not Tested |
| UAT-014 | Verify feedback reporting | Data displayed correctly | Not yet verified | Not Tested |

## 4. Summary

- Customer creation and update workflows passed.
- Lead creation and update workflows passed.
- API-created records were reflected in the MySQL-backed dashboard.
- Lead status and source chart updates were verified.
- Remaining reporting scenarios require validation.

## 5. Acceptance Criteria

- Customer and lead API workflows operate successfully.
- Data persists correctly in MySQL.
- Dashboard KPIs reflect database changes.
- Reporting sections display expected information.
- Outstanding defects are documented.

## 6. Sign-off

| Role | Status |
|---|---|
| Business Analyst | Pending |
| Developer | Pending |
| UAT Reviewer | Pending |

Note: Solar360 is a fictional portfolio case study using synthetic data. This report does not claim production deployment or real business approval.
