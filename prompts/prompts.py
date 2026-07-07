# -----------------------------------
# Requirement Analysis Prompt
# -----------------------------------

def analyze_prompt(requirement):

    return f"""
You are a Lead Business Analyst.

Analyze the below requirement.

Requirement:
{requirement}

Create a Requirement Intelligence Report.

Formatting Rules:
- Do not use HTML tags like <br>.
- Use clean Markdown formatting only.
- Use proper Markdown tables.
- Use bullet points instead of HTML line breaks.
- Keep answers concise but complete.
- Output must render correctly in Streamlit.

Return ONLY these sections:

# 🔍 Requirement Intelligence Report


## Requirement Maturity

Stage:

Overall Readiness Score: /100


## Score Breakdown

| Area | Score | Reason |
|---|---|---|
| Completeness | | |
| Clarity | | |
| Business Rules | | |
| Security | | |
| User Experience | | |
| Test Readiness | | |


## Missing Requirement Gaps

| Gap ID | Area | Missing Information | Impact |
|---|---|---|---|


## Hidden Requirements Detected

List hidden functional and technical needs.


## Risk Analysis

| Risk | Severity | Recommendation |
|---|---|---|


## Questions for Stakeholders

| Question ID | Question | Purpose |
|---|---|---|


End with:
ANALYSIS COMPLETE
"""



# -----------------------------------
# Requirement Refinement Prompt
# -----------------------------------

def refine_prompt(requirement):

    return f"""
You are a Senior Product Owner.

Improve this unclear requirement:

{requirement}

Create a development ready requirement specification.

Formatting Rules:
- Do not use HTML tags like <br>.
- Use clean Markdown formatting only.
- Keep tables readable.
- Do not put multiple sentences inside one table cell.
- For multiple business rules use bullet points.
- Keep output suitable for BA, PO and engineering teams.
- Output must render correctly in Streamlit.

Return ONLY:

# ✨ Refined Requirement Specification


## Requirement Summary

Provide clear business requirement summary.


## Actors

| Actor | Responsibility |
|---|---|


## Functional Requirements

| ID | Requirement | Priority |
|---|---|---|

After the table add:

### Business Rules

List business rules separately using bullets.


## Non Functional Requirements

| Category | Requirement |
|---|---|


## Assumptions

| ID | Assumption |
|---|---|


## Out Of Scope

| ID | Item |
|---|---|


## Open Questions

| ID | Question |
|---|---|


End with:
REFINEMENT COMPLETE
"""



# -----------------------------------
# Delivery Pack Prompt
# -----------------------------------

def delivery_pack_prompt(requirement):

    return f"""
You are a Product Owner and QA Lead.

Using this refined requirement:

{requirement}

Generate SDLC delivery artifacts.

Formatting Rules:
- Do not use HTML tags like <br>.
- Use clean Markdown formatting only.
- Keep tables readable.
- Use professional Agile delivery format.
- Output must render correctly in Streamlit.

Return ONLY:

# 🚀 SDLC Artifact Pack


## 📘 BRD Summary

Include:

- Objective
- Business Need
- Scope
- In Scope
- Out Of Scope
- Users


## 👤 User Stories + Acceptance Criteria

Format each story as:

### User Story ID + Title

As a [user]

I want [capability]

So that [business value]


Acceptance Criteria:

Given

When

Then



## 🧪 Test Cases

| Test ID | Scenario | Steps | Expected Result |
|---|---|---|---|



## 🔗 Requirement Traceability Matrix

| Requirement ID | User Story | Test Case |
|---|---|---|


End with:

DELIVERY PACK COMPLETE
"""
