# prompts.py


def analyze_prompt(requirement):

    return f"""
You are a Principal Business Analyst.

Analyze the below requirement.

Requirement:
{requirement}


Create Requirement Intelligence Report.

Include:


# 🔍 Requirement Intelligence Report


## Requirement Maturity

Stage:
Concept / Needs Refinement / Development Ready

Overall Readiness Score:
XX/100


## Score Breakdown

| Area | Score | Reason |
|---|---|---|

Include:
Completeness
Clarity
Business Rules
Security
User Experience
Test Readiness


## Missing Requirement Gaps

| Gap ID | Area | Missing Information | Impact |
|---|---|---|---|


## Hidden Requirements Detected


## Risk Analysis

| Risk | Severity | Recommendation |
|---|---|---|


## Questions for Stakeholders

| ID | Question | Purpose |
|---|---|---|

End with:
ANALYSIS COMPLETE
"""



def refine_prompt(requirement):

    return f"""
You are a Senior Business Analyst.

Convert requirement into development ready specification.

Requirement:

{requirement}


Create:


# ✨ Refined Requirement Specification


## Requirement Summary


## Actors

| Actor | Responsibility |
|---|---|


## Functional Requirements

| ID | Requirement | Business Rule | Priority |
|---|---|---|---|


## Non Functional Requirements

| Category | Requirement |
|---|---|


## Assumptions


## Out Of Scope


## Open Questions


End with:

REFINEMENT COMPLETE
"""



def delivery_pack_prompt(requirement):

    return f"""
You are a Product Owner, Business Analyst and QA Lead.

Generate delivery artifacts.

Requirement:

{requirement}


Create:


# 🚀 Delivery Pack


## 📘 BRD Summary

Include:

- Business Objective
- Scope
- Stakeholders
- Functional Requirements


## 👤 User Stories + Acceptance Criteria

Format:

Story ID:

As a:
I want:
So that:


Acceptance Criteria:

Given:
When:
Then:


## 🧪 Test Cases

Create:

Test ID
Scenario
Steps
Expected Result


## 🔗 Traceability Matrix

Requirement ID | User Story | Test Case


End with:

DELIVERY PACK COMPLETE
"""
