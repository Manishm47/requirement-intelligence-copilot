def analyze_prompt(requirement):
    return f"""
You are a Lead Business Analyst.

Analyze the below requirement.

Requirement:
{requirement}

Create a Requirement Intelligence Report.

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


def refine_prompt(requirement):
    return f"""
You are a Senior Product Owner.

Improve this unclear requirement:

{requirement}

Create a development ready requirement specification.

Return ONLY:

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


def delivery_pack_prompt(requirement):
    return f"""
You are a Product Owner and QA Lead.

Using this refined requirement:

{requirement}

Generate SDLC delivery artifacts.

Return ONLY:

# 🚀 SDLC Artifact Pack


## 📘 BRD Summary

Include:
- Objective
- Scope
- Business Need
- Users


## 👤 User Stories + Acceptance Criteria

Format:

### US-ID Title

As a
I want
So that

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
