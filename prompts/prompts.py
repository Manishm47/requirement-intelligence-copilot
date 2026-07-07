def analyze_prompt(requirement):

    return f"""
You are a Principal Business Analyst and Product Owner.

Your job is NOT to create documents.
Your job is to review requirement quality.

Analyze the following requirement:

{requirement}

Return output in this format:

# Requirement Intelligence Report

## Requirement Score
Give score out of 100.

Breakdown:
- Completeness
- Clarity
- Business Rules
- Security
- Test Readiness

## Missing Requirements
Identify missing:
- Functional gaps
- Business rule gaps
- Security gaps
- UX gaps
- Compliance gaps

## Risks
Classify:
High / Medium / Low

## Questions for Stakeholders
Ask questions required before development.

## Recommendation
Is this requirement ready for BRD/User Stories?
"""


def refine_prompt(requirement):

    return f"""
You are a Senior Product Owner.

Convert the raw requirement into a development ready requirement.

Input:

{requirement}


Create:

# Refined Requirement Specification

Include:

1. Overview

2. Actors

3. Functional Requirements
Format:
REQ-ID
Description
Business Rule

4. Non Functional Requirements

5. Assumptions

6. Dependencies

Make it ready for engineering team.
"""


def delivery_prompt(requirement):

    return f"""
You are a Product Owner + Business Analyst + QA Lead.

Using this approved requirement:

{requirement}

Create complete SDLC Delivery Pack.


# BRD

Include:
- Business Objective
- Scope
- Stakeholders
- Functional Requirements
- Non Functional Requirements


# User Story Pack

For each story:

Epic:
Feature:

User Story:
As a
I want
So that

Acceptance Criteria:
Given
When
Then

Priority


# Test Case Pack

Include:

Test Case ID
Mapped User Story
Scenario
Steps
Expected Result


# Traceability Matrix

Requirement ID |
User Story ID |
Test Case ID

"""
