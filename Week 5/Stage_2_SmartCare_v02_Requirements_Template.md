# SmartCare v0.2 - Requirements Specification Template

## 1. Problem and Scope

SmartCare Community Clinic currently uses spreadsheets, paper records and manual processes to manage patient information and appointments. This has caused problems including duplicate appointment bookings, difficulty locating patient records, inconsistent appointment status information, limited visibility of practitioner availability, manual cancellations, unreliable appointment history and difficulty producing basic operational reports.

The first version should be a simple and manageable system for a small clinic.

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

### Provisional / Requires Clarification

- Which staff roles can create, update or cancel appointments
- Whether practitioners need to view their own schedules
- Exactly what patient and practitioner information must be stored
- How long appointment history should be retained
- Exact information required in operational reports

## 2. Stakeholders

| Stakeholder | Need | Evidence |
|---|---|---|
| Patients | Have their records and appointments managed accurately. | The system is required to support patient and appointment management. |
| Clinic staff | Find patient information and manage appointments efficiently. | Staff currently report difficulty finding patient information, duplicate bookings and inconsistent appointment status. |
| Practitioners | Have their availability and appointments managed accurately. | Limited visibility of practitioner availability is identified as a current problem. |
| Clinic management | Have a manageable system with reliable appointment information and basic operational reports. | Management wants a small, maintainable system and the clinic has difficulty producing basic operational reports. |

## 3. Functional Requirements

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

**FR-11:** _________________________________________________

**FR-12:** _________________________________________________

## 4. Non-Functional Requirements

**NFR-01:** The system shall maintain consistent patient and appointment information to reduce incorrect or conflicting records.

**NFR-02:** The system shall be maintainable and manageable for a small community clinic.

**NFR-03:** The system shall provide clear and understandable functions for managing patients, practitioners and appointments.

**NFR-04:** Core appointment management functions shall be independently testable.

**NFR-05:** The system shall reliably retain appointment information and history while the application is in use.

**NFR-06:** ________________________________________________

## 5. User Stories

**US-01:** As a clinic staff member, I want to find a patient record, so that I can access the patient's information when managing an appointment.

**US-02:** As a clinic staff member, I want to create an appointment for a patient and practitioner, so that the appointment can be recorded.

**US-03:** As a clinic staff member, I want duplicate practitioner bookings to be prevented, so that a practitioner is not booked twice at the same time.

**US-04:** As a clinic staff member, I want to cancel an appointment, so that the appointment status remains accurate when a booking is cancelled.

**US-05:** As clinic management, I want basic operational reports, so that I can view useful information about clinic appointments.

**US-06:** As a __________, I want __________, so that __________.

## 6. Acceptance Criteria

### US-01 - Find a patient record

**GIVEN** a patient record exists in the system  
**WHEN** a clinic staff member searches for that patient  
**THEN** the system displays the matching patient record

### US-02 - Create an appointment

**GIVEN** a patient and practitioner exist and the appointment time is available  
**WHEN** a clinic staff member creates an appointment  
**THEN** the system records the appointment for the patient and practitioner

### US-03 - Prevent a duplicate appointment

**GIVEN** a practitioner already has an appointment at a particular time  
**WHEN** a clinic staff member tries to create another appointment for the same practitioner at the same time  
**THEN** the system rejects the duplicate booking

## 7. Assumptions and Open Questions

- Which staff roles should be allowed to create, update and cancel appointments?
- What information must be stored for each patient?
- What information must be stored for each practitioner?
- Do practitioners need to view their own appointment schedules?
- What appointment statuses are required?
- Should cancelled appointments remain permanently in appointment history?
- What information should be included in basic operational reports?
- Are there any specific performance or response-time requirements?
- Does "same time" for duplicate bookings mean the exact same appointment time or overlapping appointment periods?

## 8. AI Requirements Review Record

| AI suggestion | Evidence? | Decision | Reason | Verification |
|---|---|---|---|---|
| Clarify what "manage practitioner records" means in FR-03. | Yes | Accepted | "Managed" is vague and does not describe one clear observable capability. | FR-03 was changed to state that practitioner records can be created and located. |
| Clarify what "same time" means in FR-05. | Partial | Unverified | Duplicate bookings are a stated problem, but the exact rule for appointment conflicts is not provided. | Added as an open question requiring client clarification. |
| Clarify who can cancel appointments in FR-06. | Partial | Unverified | Manual cancellation is a stated problem, but the authorised user role is not specified. | Already recorded as an open question requiring client clarification. |
| Define the possible appointment status values in FR-07. | Partial | Unverified | Inconsistent appointment status is a stated problem, but the required status values are not specified. | Already recorded as an open question requiring client clarification. |
| Clarify what information is required in operational reports for FR-10. | Partial | Unverified | Basic operational reports are required, but their contents are not defined. | Already recorded as an open question requiring client clarification. |