# Assignment 2 - Case Study

# Stage 3 Tutorial Activities

## From Requirements to Domain Models

**Week 6 | 60 minutes**

## Candidate Concepts

| Candidate | Class? | Reason |
|---|---|---|
| Patient | Yes | Patient is an important object in the system because patient records need to be created and located. |
| Practitioner | Yes | Practitioner is needed because appointments are linked to practitioners and their availability needs to be visible. |
| Appointment | Yes | Appointment is a main object because the system needs to create, cancel and keep track of appointments. |
| Name | No | Name is better stored as an attribute of a Patient or Practitioner rather than being its own class. |
| Clinic | Maybe | The system is for SmartCare Clinic, but the current requirements do not clearly show that Clinic needs to be a separate class. |
| Database | No | A database is an implementation detail and is not a domain concept from the confirmed requirements. |
| Cancellation | No | Cancellation is something that happens to an Appointment, so it can be handled as behaviour or a status of Appointment. |
| Status | No | Status can be stored as an attribute of Appointment rather than being a separate class. |

## CRC Cards

### Patient

| Responsibilities | Collaborators |
|---|---|
| Store patient information | Appointment |
| Provide patient details | |
| Support finding a patient record | |

### Practitioner

| Responsibilities | Collaborators |
|---|---|
| Store practitioner information | Appointment |
| Provide practitioner details | |
| Have availability used when appointments are made | |

### Appointment

| Responsibilities | Collaborators |
|---|---|
| Store appointment time and status | Patient |
| Link a patient with a practitioner | Practitioner |
| Allow an appointment to be cancelled | |
| Keep appointment information for history | |

## Relationship Reasoning

**Patient to Appointment: which relationship and why?**

Patient and Appointment should have an association. A patient can have multiple appointments, and each appointment is connected to one patient. The appointment is related to the patient but does not need to be treated as part of the Patient object itself.

**Practitioner to Appointment: what multiplicity?**

One Practitioner can have zero or many Appointments, while each Appointment has one Practitioner.

**Should Appointment inherit from Patient?**

No. An Appointment is not a type of Patient. They are separate classes that are associated with each other.

**Does Clinic need to own every object?**

No. The current requirements do not show that Clinic needs to own every Patient, Practitioner and Appointment. Patient, Practitioner and Appointment can be modelled as the main domain classes without making Clinic responsible for everything.

## AI Model Critique

**Critique AI proposals: PatientManager, PractitionerManager, AppointmentManager, ClinicController, NotificationManager, ScheduleEngine.**

The AI model looks over-designed for the current SmartCare requirements. PatientManager, PractitionerManager, AppointmentManager and ClinicController add extra classes that are not clearly needed for the simple domain model. The main concepts can currently be represented by Patient, Practitioner and Appointment.

NotificationManager is also not supported because notifications are not a confirmed requirement. ScheduleEngine could also add unnecessary complexity because the requirements only say that practitioner availability needs to be visible and duplicate bookings should be prevented.

I would keep the model simple and only add extra classes later if there is a confirmed requirement that needs them.