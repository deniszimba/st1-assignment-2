from smartcare.domain.models import Appointment, Patient, Practitioner
from smartcare.repositories.appointment_repository import AppointmentRepository


class AppointmentService:
    def __init__(self, repository: AppointmentRepository):
        self.repository = repository

    def book_appointment(
        self,
        patient: Patient,
        practitioner: Practitioner,
        date_time: str
    ) -> Appointment:
        appointment = Appointment(patient, practitioner, date_time)
        self.repository.save(appointment)
        return appointment

    def cancel_appointment(self, appointment: Appointment) -> None:
        appointment.cancel()
        self.repository.save(appointment)