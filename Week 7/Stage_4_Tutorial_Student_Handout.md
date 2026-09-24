# Assignment 2 – Case Study

## Stage 4 Tutorial Activities

### Object-Oriented Design Decisions

**Week 7 | 60 minutes**

## Activity 1 - Encapsulation Review

| Class | Protected state / invariant | Public operations |
|---|---|---|
| Patient | Patient ID and name should stay valid | `validate()` |
| Practitioner | Practitioner ID, name and specialty should stay valid | Access practitioner details |
| Appointment | Status should only change through valid transitions | `cancel()` |

## Activity 2 - Composition or Inheritance?

**Appointment and Patient**

Composition/association: ☑  
Inheritance: ☐

**Reason:** An Appointment has a Patient, but an Appointment is not a type of Patient.

**Appointment and Practitioner**

Composition/association: ☑  
Inheritance: ☐

**Reason:** An Appointment has a Practitioner, but it is not a type of Practitioner.

**Doctor and Practitioner (hypothetical)**

Composition/association: ☐  
Inheritance: ☑

**Reason:** A Doctor could be a type of Practitioner, so inheritance could make sense here.

**Clinic and Appointment**

Composition/association: ☑  
Inheritance: ☐

**Reason:** A Clinic can have appointments, but an Appointment is not a type of Clinic.

## Activity 3 - Responsibility Allocation

**Who decides whether SCHEDULED can become CANCELLED?**

The Appointment class should decide because it controls the appointment status.

**Who validates a patient name?**

The Patient class should validate the patient name because it is responsible for patient information.

**Should Appointment execute SQL? Why?**

No. Appointment should only handle appointment behaviour. Database logic should be kept separate.

**Should the UI decide whether a status transition is legal?**

No. The Appointment class should decide this so the rule is always checked in one place.

## Activity 4 - AI Code Critique

AI generates an Appointment class with public status mutation, SQL inside cancel(), a NotificationManager dependency and inheritance from PatientRecord. Identify at least five design problems and corrections.

1. The status should not be changed directly from outside the Appointment class. It should be changed through methods such as `cancel()`.

2. SQL should not be inside `cancel()` because database code should be separate from the domain class.

3. `NotificationManager` is not part of the approved SmartCare design, so it should not be added.

4. Appointment should not inherit from `PatientRecord` because an Appointment is not a type of PatientRecord.

5. The class should only include responsibilities that belong to Appointment and match the approved design.

## Exit question

**Why can code be object-oriented syntactically but still have poor object-oriented design?**

Code can use classes and objects but still have poor design if responsibilities are in the wrong place, data is not protected, or unnecessary dependencies and inheritance are added.