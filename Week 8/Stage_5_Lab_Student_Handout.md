# Assignment 2- Case Study (8995-G level Task)

# Stage 5 Lab Activities

## Refactoring SmartCare into a Layered Architecture

**HUMAN ANALYSIS -> REFACTOR -> AI REVIEW -> VERIFY | 1 hour**

## A - Inspect SmartCare v0.4

Identify domain, workflow, data-access and presentation responsibilities currently mixed together.

In SmartCare v0.4, the domain classes and the manual testing/output were still kept together in one Python file.

The main responsibilities were:

- Domain: Patient, Practitioner, Appointment and AppointmentStatus
- Workflow: creating and cancelling appointments
- Presentation: printing test results
- Data access: no separate repository or persistence layer yet

This worked, but the responsibilities were not separated into clear layers.

## B - Propose Architecture

Draw Presentation -> Service -> Domain, with Service using a Repository abstraction and Persistence implementing it.

The proposed architecture is:

```text
Presentation
    |
    v
Service
    |
    v
Domain

Service
    |
    v
Repository abstraction
    ^
    |
Persistence implementation
```

The domain stays independent from the presentation and persistence layers.

## C - Create Package Structure

Create domain/, services/, repositories/, persistence/ and presentation/ or a justified equivalent.

I created this package structure:

```text
smartcare/
├── domain/
│   └── models.py
├── services/
│   └── appointment_service.py
├── repositories/
│   └── appointment_repository.py
├── persistence/
│   └── in_memory_appointment_repository.py
└── presentation/
    └── main.py
```

Each folder has one main responsibility.

## D - Introduce AppointmentService

Move workflow coordination into a focused service without stealing Appointment domain behaviour.

I created `AppointmentService`.

It coordinates:

- booking an appointment
- saving an appointment
- cancelling an appointment

The actual cancellation rule still stays inside `Appointment.cancel()`.

This keeps the service focused on workflow while the Appointment class keeps its own domain behaviour.

## E - Repository Abstraction

Define a small AppointmentRepository contract using only current use-case needs.

I created `AppointmentRepository` with:

- `save()`
- `list_all()`

The service depends on this repository abstraction instead of a specific storage method.

The in-memory repository implements the same contract using a Python list.

## F - AI Architecture Review

Ask AI to review dependency direction, misplaced responsibilities and unnecessary complexity; request simplest justified improvements.

I used Microsoft Copilot as an architecture reviewer.

Copilot said the overall architecture was already clean and identified some possible improvements or future risks.

### Copilot suggestions

- Keep cancellation and validation rules inside the domain objects.
- Keep the repository interface small.
- Let AppointmentService create appointments.
- Move the repository interface into the domain layer.
- Add a separate composition module for choosing the repository implementation.
- Avoid letting AppointmentService become a large service with too many responsibilities.
- Presentation creating Patient and Practitioner objects creates some coupling.

### Review decisions

**Accepted**

- Keep domain rules inside Appointment.
- Keep the repository interface small.
- Keep AppointmentService focused on workflow coordination.

These already matched the current design.

**Modified**

Copilot suggested moving more object creation away from Presentation.

I kept appointment creation inside `AppointmentService`, but left Patient and Practitioner creation in Presentation because the system is still small and another layer was not needed.

**Rejected**

I rejected moving `AppointmentRepository` into the Domain layer because the Week 8 architecture uses a separate Repository layer.

I also rejected adding a separate composition module because it would add extra structure without solving an important problem in the current system.

## G - Refactor and Verify

Apply only justified changes and confirm required behaviour remains unchanged.

No further code changes were needed after the AI review because the important architecture rules were already followed.

I ran the refactored system again and got:

```text
Initial status: Scheduled
After cancellation: Cancelled
Repeated cancellation: Appointment cannot be cancelled again
Stored appointments: 1
```

This confirmed that the main behaviour still worked after moving the code into separate layers.

## H - Reflection

Document one AI suggestion accepted, one modified and one rejected/deferred.

**Accepted:**  
I accepted the suggestion to keep the repository interface small because only the operations currently needed should be included.

**Modified:**  
I kept appointment creation in AppointmentService, but left Patient and Practitioner creation in Presentation because adding more structure was not necessary for this small system.

**Rejected:**  
I rejected moving the repository abstraction into the Domain layer because the Week 8 architecture shows Repository as its own layer.

The AI review was useful for checking the architecture, but I still compared its suggestions with the SmartCare requirements and the Week 8 design before deciding what to change.

## Suggested AI prompt

Act as a software architecture reviewer. Review this small SmartCare Python system against separation of concerns, cohesion, coupling and introductory SOLID principles. Identify concrete layer violations and dependency risks. Prefer the simplest refactoring that solves an observed problem. Do not introduce frameworks, microservices or patterns unless current requirements justify them.