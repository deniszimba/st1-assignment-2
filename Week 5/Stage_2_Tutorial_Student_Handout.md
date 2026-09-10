# Assignment 2 Case Study

# Stage 2 Tutorial From Problems to Requirements

**Week 5 | 60 minutes**

## Learning goals

- Analyse stakeholders.
- Distinguish functional and non-functional requirements.
- Recognise ambiguity and unsupported requirements.
- Define scope.
- Develop user stories and acceptance criteria.
- Critique AI-generated requirements.

## Activity 1 - Stakeholder Map

| Stakeholder | Need | Potential conflict |
|---|---|---|
| Patients | Have their patient records and appointments managed accurately. | Patients may want flexible appointment times while practitioner availability is limited. |
| Receptionists / clinic staff | Find patient information and manage appointments, cancellations and appointment status. | Staff need to make changes while also keeping appointment information accurate and consistent. |
| Practitioners | Have their availability and appointments managed clearly. | Practitioner availability may conflict with appointment times requested by patients. |
| Clinic management | Have reliable appointment history and basic operational reports while keeping the system manageable. | Management may want useful reporting while the first version still needs to remain simple for a small clinic. |

## Activity 2 - Functional or Non-Functional?

**Functional** ☒  **Non-functional** ☐  
The system shall allow staff to cancel an appointment.

**Functional** ☐  **Non-functional** ☒  
The system should remain responsive for the course-scale dataset.

**Functional** ☒  **Non-functional** ☐  
The system shall retain cancelled appointments.

**Functional** ☐  **Non-functional** ☒  
Core business logic should be independently testable.

**Functional** ☒  **Non-functional** ☐  
The system shall search for a patient by ID.

## Activity 3 - Repair Ambiguous Requirements

**The system should be easy to use.**

**Problem:** "Easy to use" is vague and cannot be measured clearly.  
**Clarification question:** What tasks should staff be able to complete easily and how should ease of use be measured?

**Patient search should be fast.**

**Problem:** "Fast" does not give a measurable response time.  
**Clarification question:** What is the maximum acceptable time for a patient search result to appear?

**The system should securely manage data.**

**Problem:** "Securely" is too broad and does not explain what security is required.  
**Clarification question:** Who should be allowed to access or change patient and appointment information?

**Appointments should normally be easy to cancel.**

**Problem:** "Normally" and "easy" are unclear and cannot be tested properly.  
**Clarification question:** Who can cancel an appointment and what steps should be required to cancel it?

## Activity 4 - AI Requirements Audit

**Classify each suggestion: Confirmed / Assumption requiring validation / Unsupported / Out of scope.**

| AI suggestion | Classification | Evidence / reason |
|---|---|---|
| Patients receive SMS reminders. | Unsupported | The case study does not state that SMS reminders are required. |
| Facial recognition login. | Out of scope | Facial recognition is not requested and the first version is meant to remain a manageable application for a small clinic. |
| Receptionists create appointments. | Assumption requiring validation | Appointment management is required, but the case study does not state that receptionists specifically must create appointments. |
| Online payment. | Out of scope | Payment functionality is not part of the patient, practitioner and appointment management requested in the case study. |
| Practitioners view schedules. | Assumption requiring validation | Limited visibility of practitioner availability is identified as a problem, but the case study does not specifically say that practitioners themselves must view schedules. |
| AI recommends treatments. | Out of scope | Treatment recommendations are not part of the requested patient, practitioner and appointment management system. |
| Cancelled appointments remain in history. | Assumption requiring validation | Manual cancellations and unreliable appointment history are identified as problems, but the case study does not explicitly state that cancelled appointments must remain in history. |

## Exit question

**Why is 'AI suggested it' not sufficient evidence for a requirement?**

AI can suggest features or make assumptions that the client did not actually request. A requirement needs evidence from the client or case study, or it needs to be confirmed before it is treated as a real requirement.