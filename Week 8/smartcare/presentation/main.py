from smartcare.domain.models import Patient, Practitioner
from smartcare.persistence.in_memory_appointment_repository import (
    InMemoryAppointmentRepository
)
from smartcare.services.appointment_service import AppointmentService


def main():
    patient = Patient("P001", "Alice Smith")
    patient.validate()

    practitioner = Practitioner(
        "PR001",
        "Dr John Doe",
        "General Practice"
    )

    repository = InMemoryAppointmentRepository()
    service = AppointmentService(repository)

    appointment = service.book_appointment(
        patient,
        practitioner,
        "2026-09-25 10:00 AM"
    )

    print("Initial status:", appointment.status.value)

    service.cancel_appointment(appointment)
    print("After cancellation:", appointment.status.value)

    try:
        service.cancel_appointment(appointment)
    except ValueError as error:
        print("Repeated cancellation:", error)

    print("Stored appointments:", len(service.list_appointments()))


if __name__ == "__main__":
    main()