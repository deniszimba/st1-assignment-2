from smartcare.domain.models import Appointment
from smartcare.repositories.appointment_repository import AppointmentRepository


class InMemoryAppointmentRepository(AppointmentRepository):
    def __init__(self):
        self._appointments = []

    def save(self, appointment: Appointment) -> None:
        if appointment not in self._appointments:
            self._appointments.append(appointment)

    def list_all(self) -> list[Appointment]:
        return list(self._appointments)