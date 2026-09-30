# Assignment 2- Case Study (8995-G level Task)

# Stage 5 Tutorial Activities

## Architecture and Responsibility

**Week 8 | 60 minutes**

## Activity 1 - Where Does This Belong?

| Responsibility | Layer | Reason |
|---|---|---|
| Read menu input | Presentation | User input belongs in the presentation layer. |
| Check appointment status transition | Domain | The Appointment object should control its own valid status changes. |
| Coordinate booking use case | Service | The service layer coordinates the steps needed to complete a booking. |
| Execute SQLite INSERT | Persistence | SQLite code is a storage detail and belongs in persistence. |
| Format confirmation message | Presentation | Output shown to the user belongs in presentation. |
| Find appointment by ID | Repository | The repository defines how the application finds stored appointments. |

## Activity 2 - Architecture Smell Hunt

A SmartCare file contains input(), SQL, appointment conflict rules, printing and validation. Identify at least five architecture problems and propose a layer for each responsibility.

1. `input()` is mixed with the rest of the system. It should be in the Presentation layer.

2. SQL is mixed with business logic. SQL should be in the Persistence layer.

3. Appointment conflict checking should not be mixed with user input or SQL. The Service layer can coordinate this check using appointment information.

4. Printing and output formatting should be handled by the Presentation layer.

5. Validation and appointment rules should stay with the Domain objects that own the data and behaviour.

Separating these responsibilities makes the code easier to understand, test and change.

## Activity 3 - SOLID Without Overengineering

**ClinicManager handles every use case. Which principle is threatened?**

The Single Responsibility Principle is threatened because ClinicManager has too many different responsibilities.

**AppointmentService imports sqlite3 directly. What dependency concern exists?**

The service is depending directly on a storage detail. It should depend on a repository abstraction instead of SQLite.

**A repository interface has 20 methods but a client needs two. What concern exists?**

This goes against Interface Segregation because the client is depending on methods it does not need.

**Should every class have an interface? Explain.**

No. Interfaces should only be added when they solve a real design problem. Adding one for every class would make the system more complicated without a clear benefit.

## Activity 4 - AI Architecture Critique

AI proposes microservices, an event bus, six interfaces and a dependency-injection framework. Decide what to reject, defer or keep using current requirements.

I would reject the microservices, event bus and dependency-injection framework because SmartCare is a small clinic system and the current requirements do not need that level of complexity.

I would also reject creating six interfaces just because they are possible.

I would keep a small repository abstraction because it helps separate the service layer from the persistence code.

The architecture should stay simple and only add structure that solves a current problem.