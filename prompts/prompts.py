# prompts/prompts.py


def analyze_prompt(requirement):
    return f"""
You are a Senior Business Analyst.

Analyze the requirement quality.

Keep the response concise but complete.

Provide output in this format:

# Requirement Intelligence Report

## Requirement Readiness Score
Score: X/100

## Assessment
- Completeness:
- Clarity:
- Ambiguity:
- Testability:

## Missing Information
List missing requirements or gaps.

## Risks
List business, technical, security, and delivery risks.

## Questions for Stakeholders
Provide important clarification questions.

Do not create BRD or user stories here.

Requirement:
{requirement}
"""


def refine_prompt(requirement):
    return f"""
You are an expert Product Owner and Senior Business Analyst.

Convert unclear requirement notes or meeting transcripts into a clean requirement specification.

Rules:
- Keep output concise.
- Avoid long paragraphs.
- Make it implementation ready.
- Add missing obvious requirements.
- Clearly mention assumptions.

Output format:

# Refined Requirement Specification

## 1. Objective
- Bullet points only.

## 2. Functional Requirements

Use format:

FR-ID | Requirement | Business Rule

Example:
FR-001 | User registration | Email must be unique

## 3. Non Functional Requirements

Cover:
- Security
- Performance
- Audit
- Availability

## 4. User Roles

Role | Responsibility

## 5. Assumptions

List assumptions.

## 6. Out of Scope

Mention excluded items.

Requirement:
{requirement}
"""


def delivery_pack_prompt(requirement):
    return f"""
You are a Product Owner creating delivery artifacts for Agile development.

Create a COMPLETE but SHORT delivery package.

Avoid unnecessary explanation.

Output format:

# Delivery Pack


# 1. BRD Summary

## Business Objective

## Scope

## Key Functional Requirements


# 2. User Stories & Acceptance Criteria

Format:

Epic:

User Story ID:

As a:
I want:
So that:

Acceptance Criteria:
Given
When
Then


# 3. Test Cases

Format:

Test Case ID:

Mapped User Story:

Scenario:

Steps:

Expected Result:


# 4. Requirement Traceability Matrix

Format:

Requirement ID | User Story ID | Test Case ID


# 5. Open Questions

List pending clarification questions.


Keep response concise and complete.

Requirement:
{requirement}
"""
