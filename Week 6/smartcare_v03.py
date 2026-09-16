class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name

    def validate(self):
        pass


class Practitioner:
    def __init__(self, practitioner_id, name, specialty):
        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty


class Appointment:
    def __init__(self, patient, practitioner, date_time, status):
        self.patient = patient
        self.practitioner = practitioner
        self.date_time = date_time
        self.status = status

    def cancel(self):
        pass