# SmartCare v0.5 - Architecture and Refactoring Workbook

## Week 8 student resource

## Current Architecture Problems

| Problem | Evidence | Impact | Refactoring |
|---|---|---|---|
| Domain and testing/output were together in one file | SmartCare v0.4 contained the domain classes and manual behaviour checks in the same Python file | Responsibilities were mixed together | Move domain classes into the Domain layer and output into Presentation |
| No separate service layer | Booking and cancellation workflow was not separated from the rest of the code | Workflow responsibilities were not clearly owned | Introduce `AppointmentService` |
| No repository abstraction | SmartCare v0.4 did not have a separate data-access contract | Application code could become tied to a storage method later | Add `AppointmentRepository` |
| No persistence layer | There was no separate storage implementation | Storage responsibility was not separated | Add an in-memory repository implementation |

## Layer Responsibilities

| Layer | Responsibilities | Must not contain |
|---|---|---|
| Presentation | User interaction and output formatting | Domain rules or storage code |
| Service | Coordinate booking and cancellation use cases | UI formatting or direct storage implementation details |
| Domain | Patient, Practitioner, Appointment, status and business rules | UI or persistence code |
| Repository | Define the data-access operations needed by the application | UI formatting or business rules |
| Persistence | Implement the repository using a storage method | Presentation or domain workflow logic |

## Architecture Diagram

Insert SmartCare v0.5 architecture and dependency direction.

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

The Presentation layer calls the Service layer.

The Service layer coordinates the use case and works with the Domain and Repository abstraction.

The Persistence layer implements the Repository contract.

The Domain layer stays independent from the UI and concrete storage method.

## SOLID Review

| Principle | Relevant? | Evidence | Decision |
|---|---|---|---|
| SRP | Yes | Each layer has one main responsibility | Keep responsibilities separated between Presentation, Service, Domain, Repository and Persistence |
| OCP | Partly | Different persistence implementations could be added without changing the service | No extra abstraction is needed beyond the repository contract |
| LSP | Not currently important | The current domain model does not rely on inheritance or subtype substitution | Do not add inheritance just to use the principle |
| ISP | Yes | `AppointmentRepository` only contains `save()` and `list_all()` | Keep the repository contract small and only add methods when required |
| DIP | Yes | `AppointmentService` depends on `AppointmentRepository` instead of the in-memory implementation | Keep the service dependent on the abstraction |

## AI Architecture Review

| AI suggestion | Observed problem? | Decision | Reason | Verification |
|---|---|---|---|---|
| Keep cancellation rules inside Appointment | No current problem | Accepted | Domain behaviour should remain with the class that owns it | `AppointmentService` calls `appointment.cancel()` |
| Keep repository interface small | No current problem | Accepted | The current use cases only need a small contract | Repository only contains `save()` and `list_all()` |
| Let AppointmentService create appointments | Yes / already handled | Accepted | Appointment creation is coordinated by the service | `book_appointment()` creates and saves the Appointment |
| Move AppointmentRepository into Domain | Mild suggestion only | Rejected | The Week 8 architecture uses Repository as its own layer | Repository remains in `repositories/` |
| Move more object creation away from Presentation | Minor coupling | Modified | Appointment creation stays in the service, but Patient and Practitioner creation stays in Presentation for simplicity | Program still follows the required dependency direction |
| Add a composition module | No important current problem | Rejected / Deferred | It would add extra structure to a small system without a clear current benefit | Current program runs correctly without it |
| Watch for AppointmentService becoming too large | Future risk only | Accepted as a design check | Services should coordinate use cases without becoming a new monolith | Current service only handles booking and cancellation |

## Verification

The refactored SmartCare system was run after the architecture review.

The output was:

```text
Initial status: Scheduled
After cancellation: Cancelled
Repeated cancellation: Appointment cannot be cancelled again
Stored appointments: 1
```

The main behaviour remained the same after refactoring.

The architecture now has clearer responsibilities and dependency direction without adding unnecessary complexity.