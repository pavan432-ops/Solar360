$Path = "C:\Users\user\Solar360\06_Product_Testing_UAT\Solar360_UAT_Report.md"

$Content = @'
# Solar360 – User Acceptance Testing (UAT) Report

## 1. Project Information

| Field | Details |
|---|---|
| Project | Solar360 – Customer & Installation Management Platform |
| Testing Type | User Acceptance Testing |
| Environment | Local Development |
| Backend | FastAPI |
| Database | MySQL |
| Dashboard | Streamlit |
| Test Data | Synthetic / Fictional |
| Document Status | Draft – Pending Full UAT Execution |

## 2. UAT Objective

The objective is to validate whether Solar360 supports the expected business workflows for customer management, lead management, installation operations, support tracking and management reporting.

## 3. UAT Scope

- Customer registration and updates
- Lead creation and updates
- Customer and lead data persistence
- API and database integration
- Dashboard KPI updates
- Lead status and source reporting
- Installation and quotation reporting
- Support ticket and feedback reporting

## 4. UAT Test Scenarios

| Test ID | Test Scenario | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| UAT-001 | Register a new customer | Customer is created successfully | Customer ID 2004 created | Passed |
| UAT-002 | Register another customer | Second customer is created | Customer ID 2005 created | Passed |
| UAT-003 | Update customer details | Existing customer is updated | Customer 2005 updated successfully | Passed |
| UAT-004 | Create a new lead | Lead is created successfully | Lead ID 3008 created | Passed |
| UAT-005 | Update lead status and source | Existing lead is updated | Lead 3008 updated successfully | Passed |
| UAT-006 | Verify customer KPI | Dashboard reflects new customer records | Dashboard showed 2,004 customers | Passed |
| UAT-007 | Verify lead KPI | Dashboard reflects new lead record | Dashboard showed 3,008 leads | Passed |
| UAT-008 | Verify lead status chart | Updated lead status is reflected | Change to Contacted was visible | Passed |
| UAT-009 | Verify lead source chart | Updated lead source is reflected | Change to Referral was visible | Passed |
| UAT-010 | Verify installation reporting | Installation data is displayed correctly | Pending execution | Not Tested |
| UAT-011 | Verify quotation reporting | Quotation data is displayed correctly | Pending execution | Not Tested |
| UAT-012 | Verify support reporting | Support ticket data is displayed correctly | Pending execution | Not Tested |
| UAT-013 | Verify feedback reporting | Feedback data is displayed correctly | Pending execution | Not Tested |

## 5. UAT Summary

- Customer creation and update workflows were verified.
- Lead creation and update workflows were verified.
- FastAPI successfully persisted test records in MySQL.
- Streamlit reflected the updated customer and lead data.
- Lead status and source charts reflected the lead update.
- Remaining reporting scenarios require further validation.

## 6. Defect Management

Any issue identified during UAT must be recorded in the Solar360 Defect Register with:
- Defect ID
- Description
- Steps to reproduce
- Expected result
- Actual result
- Severity
- Priority
- Status

## 7. Acceptance Criteria

The solution can be considered ready for portfolio release when:
- Core customer and lead workflows operate successfully.
- API responses and database records are consistent.
- Dashboard KPIs reflect database changes.
- Reporting sections display the expected information.
- Critical and high-priority defects are resolved or documented.
- Project documentation is complete.

## 8. Final Sign-off

| Role | Name | Status |
|---|---|---|
| Business Analyst | Not Assigned | Pending |
| Developer | Not Assigned | Pending |
| UAT Reviewer | Not Assigned | Pending |

Note: This is a fictional portfolio case study. No real business user approval or production deployment is claimed.
'@

if (Test-Path $Path) {
    Write-Host "UAT report already exists. No file was overwritten."
} else {
    Set-Content -Path $Path -Value $Content -Encoding UTF8
    Write-Host "Solar360 UAT Report created successfully."
}