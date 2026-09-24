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


# Manual behaviour checks

patient = Patient("P001", "Alice Smith")
practitioner = Practitioner("PR001", "Dr John Doe", "General Practice")

appointment = Appointment(
    patient,
    practitioner,
    "2026-09-25 10:00 AM"
)

print("Initial status:", appointment.status.value)

appointment.cancel()
print("After cancellation:", appointment.status.value)

try:
    appointment.cancel()
except ValueError as error:
    print("Repeated cancellation:", error)

try:
    invalid_patient = Patient("P002", "")
    invalid_patient.validate()
except ValueError as error:
    print("Invalid patient:", error)