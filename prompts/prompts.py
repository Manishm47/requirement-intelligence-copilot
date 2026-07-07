# -----------------------------------------
# Requirement Analysis Prompt
# -----------------------------------------

def analyze_prompt(requirement):

    return f"""
You are a Lead Business Analyst and Product Owner.

Analyze the requirement or meeting transcript.

Requirement:
{requirement}

Generate a Requirement Intelligence Report.

Keep response concise but complete.

Use this exact format:


# 🔍 Requirement Intelligence Report


## Requirement Maturity

Stage:
(Concept / BA Review Ready / Development Ready)

Overall Readiness Score: XX/100


## Score Breakdown

| Area | Score | Reason |
|---|---|---|
| Completeness | /10 | |
| Clarity | /10 | |
| Business Rules | /10 | |
| Security | /10 | |
| User Experience | /10 | |
| Test Readiness | /10 | |


## Missing Requirement Gaps

| Gap ID | Area | Missing Information | Impact |
|---|---|---|---|


## Hidden Requirements Detected

List implicit requirements that business did not mention.


## Risk Analysis

| Risk | Severity | Recommendation |
|---|---|---|


## Questions for Stakeholders

| ID | Question | Purpose |
|---|---|---|


## Final Recommendation


End with:
ANALYSIS COMPLETE
"""


# -----------------------------------------
# Requirement Refinement Prompt
# -----------------------------------------

def refine_prompt(requirement):

    return f"""
You are a Senior Business Analyst.

Convert the unclear requirement into a complete development-ready requirement.

Requirement:
{requirement}


Generate refined specification.

Use this exact format:


# ✨ Refined Requirement Specification


## Requirement Summary


## Actors

| Actor | Responsibility |
|---|---|


## Functional Requirements

| Requirement ID | Requirement | Business Rule | Priority |
|---|---|---|---|


## Non Functional Requirements

| Category | Requirement |
|---|---|


## Exception Handling

| Scenario | Expected Handling |
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


# -----------------------------------------
# SDLC Artifact Generation Prompt
# -----------------------------------------

def delivery_pack_prompt(requirement):

    return f"""
You are a Product Owner, Business Analyst and QA Lead.

Generate SDLC delivery artifacts using the refined requirement.

Requirement:
{requirement}


Generate complete but concise artifacts.


# 🚀 SDLC Artifact Pack


# 📘 BRD


## Business Objective


## Scope


## Stakeholders

| Role | Responsibility |
|---|---|


## Business Requirements

| Requirement ID | Requirement | Priority |
|---|---|---|



# 👤 User Stories + Acceptance Criteria


Generate user stories.

Format:


## US-ID : Title

As a <user>

I want <functionality>

So that <business value>


Acceptance Criteria:

Given:

When:

Then:



# 🧪 Test Cases


| Test ID | Scenario | Preconditions | Steps | Expected Result |
|---|---|---|---|---|



# 🔗 Requirement Traceability Matrix


| Requirement ID | User Story ID | Test Case ID |
|---|---|---|


End with:

DELIVERY PACK COMPLETE
"""
