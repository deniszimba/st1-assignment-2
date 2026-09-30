from enum import Enum


class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"


class Patient:
    def __init__(self, patient_id: str, name: str):
        self.patient_id = patient_id
        self.name = name

    def validate(self):
        if self.name == "":
            raise ValueError("Patient name cannot be empty")


class Practitioner:
    def __init__(self, practitioner_id: str, name: str, specialty: str):
        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty


class Appointment:
    def __init__(
        self,
        patient: Patient,
        practitioner: Practitioner,
        date_time: str
    ):
        self.patient = patient
        self.practitioner = practitioner
        self.date_time = date_time
        self._status = AppointmentStatus.SCHEDULED

    @property
    def status(self):
        return self._status

    def cancel(self):
        if self._status != AppointmentStatus.SCHEDULED:
            raise ValueError("Appointment cannot be cancelled again")

        self._status = AppointmentStatus.CANCELLED