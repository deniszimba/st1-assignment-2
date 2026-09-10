# Assignment 2 – Case Study Lab

# Stage 2 Lab Activities

## SmartCare Requirements Engineering

**AI OFF -> AI ON -> VERIFY | 1 hour**

## Learning objectives

- Analyse the SmartCare client brief.
- Identify stakeholders and scope.
- Write functional and non-functional requirements.
- Develop user stories and Given-When-Then acceptance criteria.
- Use AI to critique requirements without allowing it to invent stakeholder needs.
- Produce SmartCare Requirements Specification v1.0.

## Part A - Client Brief: AI OFF

SmartCare uses spreadsheets and paper records. Staff report duplicate bookings, difficulty finding patient information, inconsistent appointment status and limited appointment history. Management wants a small, maintainable patient, practitioner and appointment system.

## Part B - Stakeholders and Scope: AI OFF

**Identify at least four stakeholders. Create In Scope and Out of Scope lists. Label uncertain features as provisional rather than confirmed.**

### Stakeholders

| Stakeholder | Need |
|---|---|
| Patients | Have their patient records and appointments managed accurately. |
| Clinic staff | Find patient information and manage appointments, cancellations and appointment status. |
| Practitioners | Have their availability and appointments managed accurately. |
| Clinic management | Have reliable appointment information and basic operational reports while keeping the system manageable. |

### In Scope

- Patient management
- Practitioner management
- Appointment management
- Finding patient records
- Managing practitioner availability
- Cancelling appointments
- Recording appointment status
- Maintaining appointment history
- Basic operational reports

### Out of Scope

- Complex hospital information system
- AI treatment or diagnosis recommendations
- Online payments
- Facial recognition
- Insurance processing

### Provisional

- Which staff roles can create, update or cancel appointments
- Whether practitioners need to view their own schedules
- Exactly what patient and practitioner information must be stored
- How long appointment history should be retained
- Exact information required in operational reports

## Part C - Functional Requirements: AI OFF

**Write 8-12 numbered functional requirements using FR-01, FR-02 and so on. Each should describe one observable capability.**

**FR-01:** The system shall allow patient records to be created.

**FR-02:** The system shall allow patient records to be located.

**FR-03:** The system shall allow practitioner records to be created and located.

**FR-04:** The system shall allow appointments to be created for a patient and practitioner.

**FR-05:** The system shall prevent duplicate appointment bookings for the same practitioner at the same time.

**FR-06:** The system shall allow an appointment to be cancelled.

**FR-07:** The system shall record the status of an appointment.

**FR-08:** The system shall maintain an appointment history.

**FR-09:** The system shall provide visibility of practitioner availability.

**FR-10:** The system shall produce basic operational reports.

## Part D - Non-Functional Requirements: AI OFF

**Write 4-6 numbered non-functional requirements covering appropriate qualities such as reliability, maintainability, usability, data integrity or testability.**

**NFR-01:** The system shall maintain consistent patient and appointment information to reduce incorrect or conflicting records.

**NFR-02:** The system shall be maintainable and manageable for a small community clinic.

**NFR-03:** The system shall provide clear and understandable functions for managing patients, practitioners and appointments.

**NFR-04:** Core appointment management functions shall be independently testable.

**NFR-05:** The system shall reliably retain appointment information and history while the application is in use.

## Part E - User Stories and Acceptance Criteria: AI OFF

**Write 4-6 user stories. For at least three, create Given-When-Then acceptance criteria including one negative or failure scenario.**

### User Stories

**US-01:** As a clinic staff member, I want to find a patient record, so that I can access the patient's information when managing an appointment.

**US-02:** As a clinic staff member, I want to create an appointment for a patient and practitioner, so that the appointment can be recorded.

**US-03:** As a clinic staff member, I want duplicate practitioner bookings to be prevented, so that a practitioner is not booked twice at the same time.

**US-04:** As a clinic staff member, I want to cancel an appointment, so that the appointment status remains accurate when a booking is cancelled.

**US-05:** As clinic management, I want basic operational reports, so that I can view useful information about clinic appointments.

### Acceptance Criteria

#### US-01 - Find a patient record

**GIVEN** a patient record exists in the system  
**WHEN** a clinic staff member searches for that patient  
**THEN** the system displays the matching patient record

#### US-02 - Create an appointment

**GIVEN** a patient and practitioner exist and the appointment time is available  
**WHEN** a clinic staff member creates an appointment  
**THEN** the system records the appointment for the patient and practitioner

#### US-03 - Prevent a duplicate appointment - Failure Scenario

**GIVEN** a practitioner already has an appointment at a particular time  
**WHEN** a clinic staff member tries to create another appointment for the same practitioner at the same time  
**THEN** the system rejects the duplicate booking

## Part F - AI Requirements Review: AI ON

**Prompt:**

Act as a software requirements reviewer. Review the SmartCare requirements for ambiguity, inconsistency, missing clarification questions and testability. Do NOT invent new client requirements. For every suggestion, state whether it is based on evidence or is only a question/assumption requiring validation.

### Selected AI review suggestions

Microsoft Copilot was used to review the requirements.

1. FR-03 uses the word "managed", which is unclear because it does not say whether this means create, view, update or delete.
2. FR-05 is unclear about whether "same time" means an exact time or overlapping appointment times.
3. FR-06 does not identify who is allowed to cancel an appointment.
4. FR-07 does not define the possible appointment status values.
5. FR-10 does not define what information should appear in basic operational reports.

## Part G - VERIFY the AI Review

**Classify each significant AI suggestion as Accepted, Modified, Rejected, or Unverified. Explain the evidence used.**

| AI suggestion | Classification | Evidence / reason |
|---|---|---|
| Clarify what "manage practitioner records" means in FR-03. | Accepted | The word "managed" is broad and does not describe one clear observable capability. FR-03 was changed to make the actions clearer. |
| Clarify what "same time" means in FR-05. | Unverified | The case study confirms duplicate bookings are a problem, but it does not say whether conflicts are based on exact times or overlapping appointment periods. |
| Clarify who can cancel appointments in FR-06. | Unverified | Manual cancellation is identified as a problem, but the case study does not state which user role should be allowed to cancel appointments. |
| Define the appointment status values used in FR-07. | Unverified | Inconsistent appointment status is identified as a problem, but the required status values are not provided. |
| Clarify the content of the operational reports in FR-10. | Unverified | The case study says basic operational reports are needed, but it does not specify the information that should be included. |

## Part H - Finalise SmartCare v0.2

**Submit stakeholder analysis, scope, 8-12 FRs, 4-6 NFRs, 4-6 user stories, acceptance criteria, assumptions/open questions and selected AI review evidence.**

The completed SmartCare v0.2 requirements are recorded in `Stage_2_SmartCare_v02_Requirements_Template.md`.

The final specification contains:

- Stakeholder analysis
- In Scope and Out of Scope lists
- Provisional requirements
- 10 functional requirements
- 5 non-functional requirements
- 5 user stories
- 3 Given-When-Then acceptance criteria
- A negative/failure acceptance criterion
- Assumptions and open questions
- Selected Microsoft Copilot AI review evidence

## Reflection

**In 150-250 words: What did AI notice that you missed? What did AI invent or overreach on? Which requirement changed after review? Why must requirements have evidence?**

The AI review helped me notice that some of my requirements used words that were too broad or unclear. One example was FR-03, where I originally wrote that practitioner records should be "managed". Copilot pointed out that this did not clearly say what the system needed to do. I changed the requirement so that it now states that practitioner records can be created and located.

The AI also identified questions that could not be answered from the case study, such as who is allowed to cancel appointments, what appointment status values should be used and what information should appear in operational reports. I kept these as unverified questions instead of making assumptions.

Some of the AI suggestions also asked about details such as overlapping appointment times. Although these could be important, the case study does not provide enough evidence to decide the exact rule.

This review showed me why requirements need evidence. AI can identify gaps and possible problems, but it cannot decide what the client wants when that information has not been provided. Those details need to be confirmed before they become requirements.