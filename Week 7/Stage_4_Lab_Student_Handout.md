# Assignment 2-Case Study

# Stage 4 Lab Activities

## Implementing the SmartCare Domain Layer

**DESIGN FIRST -> AI PAIR PROGRAMMING -> REVIEW -> VERIFY | 1hour**

## A - Revisit Approved UML

Confirm responsibilities, attributes and relationships before coding.

I reviewed my approved Week 6 UML before starting the code.

The main classes were:

- Patient with patient_id, name and validate()
- Practitioner with practitioner_id, name and specialty
- Appointment with patient, practitioner, date_time, status and cancel()

Appointment is linked to one Patient and one Practitioner.

## B - Implement Patient: AI OFF

Implement Patient with type hints and basic validation.

I implemented Patient with string type hints for `patient_id` and `name`.

The `validate()` method checks if the patient name is empty and raises a `ValueError` if it is.

## C - Implement Practitioner: AI OFF

Implement Practitioner with identifier, name and specialty; no database logic.

I implemented Practitioner with:

- practitioner_id
- name
- specialty

I used string type hints and did not add any database logic.

## D - Implement Appointment: AI ON

Give AI the approved Appointment UML, business rules and explicit constraints. Ask it to implement only Appointment and agreed enum/exception.

I used Microsoft Copilot as a pair programmer.

I gave Copilot my approved Appointment design and told it to only implement Appointment with an AppointmentStatus enum.

Copilot suggested:

- an AppointmentStatus enum with SCHEDULED, CANCELLED and COMPLETED
- a cancel() method with validation
- using ValueError for invalid status changes
- a mark_completed() method
- using datetime for date_time
- an unused Optional import

I reviewed these suggestions before using them.

## E - Review Generated Code

Check model consistency, unsupported features, public state mutation, unnecessary inheritance, invented dependencies and error handling.

I reviewed the Copilot code against my Week 6 design.

**Accepted:**

- AppointmentStatus enum
- cancel() status check
- ValueError for an invalid cancellation

**Modified:**

- I kept date_time as a string instead of changing it to datetime.
- I changed status to `_status` and used a property so it is not directly changed from outside Appointment.

**Rejected:**

- `mark_completed()` because it was not in my approved UML.
- the unused `Optional` import.
- extra datetime code because it was not needed.

No database, UI, notification, service or inheritance code was added.

## F - Manual Behaviour Checks

Create valid objects, test invalid input, cancel a scheduled appointment and attempt an illegal repeated transition.

I ran the program and got:

    Initial status: Scheduled
    After cancellation: Cancelled
    Repeated cancellation: Appointment cannot be cancelled again
    Invalid patient: Patient name cannot be empty

The valid appointment was created successfully.

The appointment changed from Scheduled to Cancelled.

Trying to cancel the same appointment again raised an error.

The empty patient name was also rejected.

## G - Refactor

Remove unnecessary code and make implementation simpler and design-consistent.

I removed the extra parts suggested by Copilot that were not needed.

I kept the implementation close to my Week 6 design and only added the parts needed for Week 7.

## H - AI Engineering Log

Record prompt, generated contribution, decisions and verification evidence.

**Prompt used:**

Act as a Python pair programmer.

I am working on the SmartCare Clinic Appointment Booking System.

My approved Week 6 Appointment design is:

Appointment
- patient: Patient
- practitioner: Practitioner
- date_time
- status
- cancel()

Patient and Practitioner are already implemented.

Implement only the Appointment class from this approved design.

Use type hints and an AppointmentStatus enum with:
- SCHEDULED
- CANCELLED
- COMPLETED

Business rules and constraints:
- A new appointment starts as SCHEDULED.
- A scheduled appointment can be cancelled.
- A cancelled appointment remains as an object.
- An appointment should not be cancelled more than once.
- Appointment should control its own status changes.
- Do not add database code.
- Do not add UI code.
- Do not add notification or service classes.
- Do not add inheritance.
- Keep the code simple and suitable for a first-year Python student.

Explain any implementation decision that is not directly shown in the UML.

**Generated contribution:**

Copilot generated an Appointment class with an AppointmentStatus enum, cancellation checks, ValueError handling, a mark_completed() method and datetime for date_time.

**Decisions:**

I kept the enum, cancellation check and ValueError.

I rejected mark_completed() because it was not in my approved UML.

I kept date_time simple instead of changing it to datetime.

I also protected the status using `_status` and a property.

**Verification evidence:**

I tested a valid appointment, cancelling it, cancelling it again and an empty patient name. The program gave the expected results.

## Suggested AI prompt

Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML. Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add database, UI, notification or service classes. Protect status transitions and explain any decision not directly visible in the UML.

## Reflection

Which AI-generated part did you modify or reject? Why? How did the approved design constrain the AI?

I rejected the `mark_completed()` method because it was not part of my approved Week 6 UML. I also did not use the datetime and Optional parts because they were not needed.

The approved design helped keep the AI focused on Appointment and stopped extra classes or features from being added. I only kept the parts that matched the SmartCare design and Week 7 requirements.