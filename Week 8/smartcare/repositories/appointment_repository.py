from abc import ABC, abstractmethod

from smartcare.domain.models import Appointment


class AppointmentRepository(ABC):
    @abstractmethod
    def save(self, appointment: Appointment) -> None:
        pass

    @abstractmethod
    def list_all(self) -> list[Appointment]:
        pass