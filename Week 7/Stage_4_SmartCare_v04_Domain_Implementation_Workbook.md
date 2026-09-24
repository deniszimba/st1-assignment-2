# SmartCare v0.4 - Domain Implementation Workbook

## Week 7 student resource

## 1. UML-to-Code Trace

| UML element | Python element | Implemented? | Notes |
|---|---|---|---|
| Patient | `class Patient` | Yes | Uses patient_id and name |
| Patient.validate() | `validate()` | Yes | Checks for an empty patient name |
| Practitioner | `class Practitioner` | Yes | Uses practitioner_id, name and specialty |
| Appointment | `class Appointment` | Yes | Links Patient and Practitioner |
| Appointment.patient | `self.patient` | Yes | Stores the Patient object |
| Appointment.practitioner | `self.practitioner` | Yes | Stores the Practitioner object |
| Appointment.date_time | `self.date_time` | Yes | Stored as a string |
| Appointment.status | `_status` and `status` property | Yes | Status is controlled by Appointment |
| Appointment.cancel() | `cancel()` | Yes | Changes Scheduled to Cancelled |
| Appointment status values | `AppointmentStatus` enum | Yes | SCHEDULED, CANCELLED and COMPLETED |

## 2. Domain Invariants

| Class | Invariant / rule | How protected |
|---|---|---|
| Patient | Patient name cannot be empty | `validate()` raises a `ValueError` |
| Practitioner | Practitioner keeps its identifier, name and specialty together | Stored inside the Practitioner object |
| Appointment | A new appointment starts as Scheduled | `_status` is set to `SCHEDULED` when created |
| Appointment | Only a Scheduled appointment can be cancelled | `cancel()` checks the current status first |
| Appointment | An appointment cannot be cancelled twice | A repeated cancellation raises `ValueError` |

## 3. Composition / Inheritance Decisions

| Relationship | Decision | Rationale |
|---|---|---|
| Appointment and Patient | Association/composition | Appointment has a Patient but is not a type of Patient |
| Appointment and Practitioner | Association/composition | Appointment has a Practitioner but is not a type of Practitioner |
| Patient and Practitioner | No inheritance | They have different responsibilities |
| Appointment and Patient | No inheritance | Appointment is not a type of Patient |
| Appointment and Practitioner | No inheritance | Appointment is not a type of Practitioner |

## 4. AI Pair-Programming Record

| AI contribution | Conforms? | Decision | Reason | Verification |
|---|---|---|---|---|
| AppointmentStatus enum | Yes | Accepted | Matches the Week 7 requirement for clear status values | Program starts with Scheduled status |
| Cancellation status check | Yes | Accepted | Matches the rule that Appointment controls cancellation | Cancellation changed Scheduled to Cancelled |
| `ValueError` for invalid cancellation | Yes | Accepted | Simple way to stop an invalid repeated cancellation | Second cancellation raised an error |
| `mark_completed()` method | No | Rejected | It was not in my approved Week 6 UML | Not included in final code |
| `datetime` for date_time | Partly | Modified | I kept date_time as a string to stay consistent with my existing design | Program ran correctly with the string value |
| `Optional` import | No | Rejected | It was not used | Removed from final code |
| Public status value | Partly | Modified | Status should be controlled by Appointment | Changed to `_status` with a property |

## 5. Updated UML

Insert updated UML only if implementation revealed a justified design change. Explain every change.

No updated UML was needed.

The main Week 6 design stayed the same with Patient, Practitioner and Appointment.

The Week 7 implementation added an `AppointmentStatus` enum and protected the appointment status in the code, but this did not change the main domain relationships or responsibilities.