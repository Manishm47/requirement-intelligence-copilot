def analyze_prompt(requirement):
    return f"""
You are a Lead Business Analyst.

Analyze this requirement:

{requirement}

Create Requirement Intelligence Report.

Include:

# 🔍 Requirement Intelligence Report

## Requirement Score
Give score out of 100

## Score Breakdown

- Completeness
- Clarity
- Business Rules
- Security
- User Experience
- Test Readiness


## Missing Requirements

Create table:

| Area | Missing Detail | Impact |
|---|---|---|


## Risks

Create table:

| Risk | Severity | Recommendation |
|---|---|---|


## Questions for Stakeholders

Create important BA clarification questions.

Keep output concise but complete.
"""


def refine_prompt(requirement):
    return f"""
You are a Senior Product Owner.

Improve this requirement:

{requirement}

Create:

# ✨ Refined Requirement Specification


## Requirement Summary


## Actors


## Functional Requirements

| ID | Requirement | Business Rule | Priority |
|---|---|---|---|


## Non Functional Requirements


## Assumptions


## Out Of Scope


## Open Questions


After this create:


# 📘 BRD Summary


# 👤 User Stories + Acceptance Criteria


# 🧪 Test Cases


Create complete development ready output.
"""
