# SmartCare v0.3 - Domain Model Workbook

**Week 6 student resource**

## Requirement-to-Concept Trace

| Requirement | Concept | State / behaviour | Decision |
|---|---|---|---|
| FR-01: Create patient records | Patient | Patient ID and name | Include Patient as a class |
| FR-02: Locate patient records | Patient | Patient ID and name | Patient needs information that can identify a record |
| FR-03: Create and locate practitioner records | Practitioner | Practitioner ID, name and specialty | Include Practitioner as a class |
| FR-04: Create appointments for a patient and practitioner | Appointment | Patient, practitioner and date/time | Include Appointment as a class |
| FR-05: Prevent duplicate practitioner bookings at the same time | Appointment | Practitioner and date/time | Keep this as appointment-related behaviour |
| FR-06: Cancel an appointment | Appointment | Status and cancel behaviour | Cancellation belongs to Appointment |
| FR-07: Record appointment status | Appointment | Status | Store status as an Appointment attribute |
| FR-08: Maintain appointment history | Appointment | Appointment details and status | Appointment contains the information needed for appointment history |
| FR-09: Provide visibility of practitioner availability | Practitioner / Appointment | Practitioner and appointment date/time | Availability depends on the practitioner and their appointments |
| FR-10: Produce basic operational reports | Existing domain information | Patient, practitioner and appointment information | Do not add a Report class because a separate class is not supported by the current requirements |

## CRC Cards

### Patient

| Responsibilities | Collaborators |
|---|---|
| Store patient identity and state | Appointment |
| Provide patient details | Appointment |
| Perform basic validation of patient information | Appointment |

### Practitioner

| Responsibilities | Collaborators |
|---|---|
| Store practitioner identity and state | Appointment |
| Store practitioner specialty | Appointment |
| Provide practitioner details | Appointment |

### Appointment

| Responsibilities | Collaborators |
|---|---|
| Store the patient and practitioner for the appointment | Patient, Practitioner |
| Store appointment date/time and status | Patient, Practitioner |
| Cancel an appointment by changing its status | Patient, Practitioner |
| Keep the appointment state needed for appointment history | Patient, Practitioner |

### Optional class

**Clinic**

| Responsibilities | Collaborators |
|---|---|
| No clear responsibility supported by the current requirements | None |

**Decision:** I did not include Clinic in the current domain model because Patient, Practitioner and Appointment are enough to represent the confirmed SmartCare requirements at this stage.

## UML Class Diagram

**Insert/draw UML here. Include defensible relationships and multiplicities.**

    +-----------------------+
    | Patient               |
    +-----------------------+
    | patient_id            |
    | name                  |
    +-----------------------+
    | validate()            |
    +-----------------------+
               1
               |
               | 0..*
               |
    +-----------------------+
    | Appointment           |
    +-----------------------+
    | patient               |
    | practitioner          |
    | date_time             |
    | status                |
    +-----------------------+
    | cancel()              |
    +-----------------------+
               |
               | 0..*
               |
               1
    +-----------------------+
    | Practitioner          |
    +-----------------------+
    | practitioner_id       |
    | name                  |
    | specialty             |
    +-----------------------+

### Relationships and Multiplicities

- A Patient can have zero or many Appointments (0..*).
- Each Appointment has exactly one Patient (1).
- A Practitioner can have zero or many Appointments (0..*).
- Each Appointment has exactly one Practitioner (1).
- Patient and Appointment have an association.
- Practitioner and Appointment also have an association.

## Design Rationale

**Explain class selection, responsibility allocation and key relationships.**

I selected Patient, Practitioner and Appointment because they are the main concepts supported by the SmartCare requirements. Patient stores the patient's identity and information, Practitioner stores the practitioner's identity and specialty, and Appointment connects a patient and practitioner at a particular date and time.

I kept each responsibility with the class it relates to. For example, appointment status and cancellation belong to Appointment because cancelling changes the state of an appointment. Patient and Practitioner mainly store information about themselves.

The relationships are associations. A patient can have zero or many appointments and a practitioner can also have zero or many appointments. Each appointment has exactly one patient and one practitioner. I did not use inheritance because an Appointment is not a type of Patient or Practitioner.

I also did not add extra Manager, Controller, Database or Notification classes because the current requirements do not support them. Keeping the model simple makes it easier to understand and keeps the design connected to the requirements.

## AI Design Review Record

| AI suggestion | Evidence | Decision | Reason | Model change |
|---|---|---|---|---|
| Use Patient, Practitioner and Appointment as the core classes | FR-01 to FR-09 | Accepted | These classes directly represent the main SmartCare domain concepts and confirmed requirements. | No change needed because these classes were already in the human model. |
| Create a separate PractitionerAvailability class | FR-09 | Modified | Practitioner availability is required, but FR-09 does not say that it must be represented by a separate class. | Keep availability represented through Practitioner and Appointment information for now. |
| Add AppointmentManager, PatientManager and PractitionerManager | No requirement specifically requires separate Manager classes | Rejected | The Manager classes add unnecessary complexity to the current domain model. | Do not add the Manager classes. |
| Create AppointmentStatus as a separate class | FR-07 | Rejected | Appointment status is required, but it can be represented as an attribute of Appointment. | Keep `status` as an Appointment attribute. |
| Create AppointmentHistoryEntry as a separate class | FR-08, NFR-05 | Modified | Appointment history is required, but the requirements do not specify that separate history-entry objects are needed. | Keep the required appointment state in Appointment and leave a separate history class for later clarification. |