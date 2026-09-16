# Assignment 2 - Case Study

# Stage 3 Lab Activities

## SmartCare Domain Modelling

**AI OFF -> AI ON -> COMPARE -> VERIFY | 1 hour**

## A - Requirements Review

**Highlight nouns, verbs and business rules in SmartCare v0.2.**

### Nouns / Domain Concepts

- Patient
- Practitioner
- Appointment
- Patient record
- Practitioner availability
- Appointment status
- Appointment history

### Verbs / Behaviours

- Create patient records
- Locate patient records
- Create and locate practitioner records
- Create appointments
- Prevent duplicate bookings
- Cancel appointments
- Record appointment status
- Maintain appointment history
- View practitioner availability
- Produce basic operational reports

### Business Rules

- An appointment is connected to a patient and a practitioner.
- The same practitioner should not be booked twice at the same time.
- An appointment can be cancelled.
- An appointment has a status.
- Appointment information needs to be kept for appointment history.
- Practitioner availability needs to be visible.

## B - Candidate Classes

**Record candidate concepts, supporting requirements, state and behaviour.**

| Candidate concept | Supporting requirements | State | Behaviour | Decision |
|---|---|---|---|---|
| Patient | FR-01, FR-02, FR-04 | Patient ID, name | Validate patient information | Include |
| Practitioner | FR-03, FR-04, FR-09 | Practitioner ID, name, specialty | Provide practitioner information | Include |
| Appointment | FR-04, FR-05, FR-06, FR-07, FR-08 | Patient, practitioner, date/time, status | Cancel and change appointment state | Include |
| Clinic | No specific FR requires it as a separate class | Not confirmed | Not confirmed | Do not include at this stage |
| Status | FR-07 | Appointment status | None required separately | Keep as an attribute of Appointment |
| Cancellation | FR-06 | Changes appointment status | Cancel appointment | Keep as behaviour of Appointment |

## C - CRC Cards

**Create CRC cards for Patient, Practitioner and Appointment.**

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

## D - UML Model

**Draw classes, attributes, operations, associations and multiplicities.**

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

### Relationships

- One Patient can have zero or many Appointments.
- Each Appointment has exactly one Patient.
- One Practitioner can have zero or many Appointments.
- Each Appointment has exactly one Practitioner.
- Patient and Appointment have an association.
- Practitioner and Appointment have an association.

## E - AI Design Review

**Ask AI to suggest classes and relationships using only confirmed requirements; require supporting requirement IDs.**

### Prompt used

I asked Microsoft Copilot:

"Use only the confirmed SmartCare requirements and business rules below. Suggest candidate classes, responsibilities, collaborators and relationships for the SmartCare domain model. For every proposed class, responsibility and relationship, state which requirement ID supports it. Do not invent features, database concerns or UI details. Identify any uncertain proposals separately for human review."

I also provided the confirmed FR-01 to FR-10 and NFR-01 to NFR-05 requirements.

### Selected AI suggestions

Copilot suggested:

- Patient, Practitioner and Appointment as the core classes.
- PractitionerAvailability as a separate class.
- AppointmentStatus as a separate class.
- AppointmentHistoryEntry as a separate class.
- Report or ReportingService for operational reports.
- AppointmentManager, PatientManager and PractitionerManager classes.
- Associations between Patient, Practitioner and Appointment.

Copilot also identified AppointmentHistoryEntry, PractitionerAvailability and ReportingService as areas that required human review because the requirements did not fully define their structure.

## F - Compare and Decide

**Record at least one accepted, modified and rejected AI suggestion.**

| AI suggestion | Decision | Supporting evidence | Final action |
|---|---|---|---|
| Use Patient, Practitioner and Appointment as the core classes | Accepted | These concepts are directly supported by FR-01 to FR-09 and match the main SmartCare domain concepts. | Keep the three classes in the model. |
| Create a separate PractitionerAvailability class | Modified | FR-09 requires visibility of practitioner availability, but it does not require availability to be a separate class. | Represent availability using Practitioner and Appointment information for now. |
| Add AppointmentManager, PatientManager and PractitionerManager | Rejected | The current requirements do not require separate Manager classes and the existing domain classes can represent the required responsibilities at this stage. | Do not add the Manager classes. |
| Create AppointmentStatus as a separate class | Rejected | FR-07 requires appointment status to be recorded but does not require a separate class. | Keep status as an attribute of Appointment. |
| Create AppointmentHistoryEntry as a separate class | Modified | FR-08 requires appointment history, but it does not specify that separate history-entry objects are required. | Keep the required appointment state in Appointment and leave a separate history class for later clarification. |

## G - Python Skeletons

**Create simple Patient, Practitioner and Appointment class skeletons.**

The Python class skeletons were created in `smartcare_v03.py`.

The file contains:

- `Patient` with `patient_id`, `name` and a `validate()` placeholder.
- `Practitioner` with `practitioner_id`, `name` and `specialty`.
- `Appointment` with `patient`, `practitioner`, `date_time`, `status` and a `cancel()` placeholder.

The methods use `pass` where full behaviour has not been implemented yet.

## H - Consistency Check

**Check model-code consistency; do not implement full behaviour yet.**

I compared the UML model with `smartcare_v03.py`.

- The class names match: Patient, Practitioner and Appointment.
- Patient has the modelled `patient_id` and `name` attributes.
- Practitioner has the modelled `practitioner_id`, `name` and `specialty` attributes.
- Appointment has the modelled `patient`, `practitioner`, `date_time` and `status` attributes.
- Patient includes the `validate()` operation from the model.
- Appointment includes the `cancel()` operation from the model.
- The Patient and Practitioner relationships are represented by the `patient` and `practitioner` attributes in Appointment.
- No unsupported Manager, Reporting, Database or Notification classes were added.
- Full behaviour has not been implemented yet.

## Reflection

**What modelling decision was hardest? Where did AI over-design? What evidence supported your final choices?**

The hardest modelling decision was deciding when something should be its own class instead of an attribute or behaviour of another class. For example, appointment status and practitioner availability are both important to the system, but the requirements do not say that they need to be separate classes.

The Copilot review helped by suggesting different ways the model could be structured, but it also over-designed parts of the system. It suggested classes such as AppointmentManager, PatientManager, PractitionerManager, AppointmentHistoryEntry and ReportingService. Some of these could become useful in a larger system, but they are not all necessary for the current SmartCare domain model.

I kept Patient, Practitioner and Appointment as the main classes because they are directly supported by the confirmed requirements. I kept status as part of Appointment and represented practitioner availability using Practitioner and Appointment information rather than adding extra classes.

The final choices were based on the confirmed requirement IDs and the SmartCare problem rather than accepting the AI suggestions automatically. This kept the model simple while still representing the required information, responsibilities and relationships.