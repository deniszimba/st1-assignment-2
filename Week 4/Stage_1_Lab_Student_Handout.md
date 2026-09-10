# Stage 1 Lab - Human vs AI: Building Your First SmartCare Prototype

## Learning objectives

- Create and run a simple Python file with basic input,output and processing statements
- Use lists, dictionaries and functions to enhance the Python file
- Build a small SmartCare appointment prototype.
- Use AI as a tutor rather than a replacement.
- Compare human-written and AI-generated code.
- Verify AI-generated code through execution and test inputs.
- Document a short AI-use reflection.

## Files to create and commit in GitHub

```text
stage01/
  smartcare_v01.py
  comparison.md
  reflection.md
  ai_usage.md
```

## Part A - Understand the Problem: AI OFF

SmartCare needs a small prototype that allows a receptionist to record patient appointments. Each appointment records patient name, practitioner name and appointment time.

**What data must be stored?**

The patient name, practitioner name and appointment time need to be stored.

**What functions might be useful?**

A function to book an appointment and a function to display appointments would be useful.

**What could go wrong?**

Information could be missing or incorrect, two appointments could be booked for the same practitioner and time, or an appointment might not be stored correctly.

**What requirements are unclear?**

It is unclear how appointments should be changed or cancelled, what other patient or practitioner information should be stored, and whether duplicate appointment times should be prevented.

## Part B - Build a Human-Written Prototype: AI OFF

```python
#task 1
# Create and run a simple Python file with basic input,output statements

print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

# First Appointment
patient1_name = 'Alice Smith'
practitioner1_name = 'Dr. John Doe'
appointment1_time = '2024-07-20 10:00 AM'

print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")

# Second Appointment
patient2_name = 'Bob Johnson'
practitioner2_name = 'Dr. Jane Roe'
appointment2_time = '2024-07-20 11:30 AM'

print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time: {appointment2_time}")


#task1enhanced
# Use lists, dictionaries and functions to enhance the Python file

appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")

    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)

def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return

    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")

print("Welcome to SmartCare: The Clinical Appointment Booking System!")

book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')

display_appointments()
```

**^ Now, run both programs , and identify at least five limitations.**

1. The appointments are hard-coded instead of being entered by the user.
2. The program does not stop two appointments being booked with the same practitioner at the same time.
3. The practitioner name and appointment time are not checked for missing or incorrect values.
4. The appointments are only stored while the program is running and are lost when it closes.
5. There is no way to cancel, edit or search for an appointment.

## Part C - Use AI as Tutor: AI ON (Use only UC approved GenAI Tool such as Microsoft CoPilot)

**Suggested prompt structure:**

Act as a Python tutor.  
I am learning introductory software technology.  
Here is a small appointment-booking function.

1. Explain what the code does.
2. Identify three limitations.
3. Suggest improvements.
4. Do not rewrite the whole application.
5. Ask me two questions to test my understanding.

### AI use

Microsoft Copilot was used as a tutor to explain how functions and lists could improve the basic appointment program.

It explained that a list can keep multiple appointments together instead of creating separate variables for every appointment. It also explained that functions can be used for tasks such as adding and displaying appointments, which reduces repeated code and makes the program easier to update.

The AI usage is documented in `ai_usage.md`.

## Part D - Generate an Alternative: AI ON

**Ask AI to create a simple beginner-friendly Python function that stores patient name, practitioner name and appointment time. Explicitly prohibit a database or GUI.**

The AI-generated alternative used a simple function to store the patient name, practitioner name and appointment time together. It did not use a database or GUI.

The alternative was reviewed rather than automatically replacing the human-written version.

## Part E - Compare Human and AI Versions

| Question | Human version | AI version |
|---|---|---|
| Easy to understand? | Yes, the code is simple and I understand how it works. | Yes, the function and list are easy to follow. |
| Runs successfully? | Yes, it runs successfully. | Yes, after testing it. |
| Uses only required features? | Yes, it uses basic Python features. | Yes, it uses a function, lists and input. |
| Adds assumptions? | Very few assumptions are made. | Yes, it assumes the user will enter valid information. |
| Handles errors? | Only checks if the patient name is empty. | No, it does not validate the inputs. |
| Could I explain it? | Yes. | Yes, I understand how the function adds an appointment to the list. |

The comparison is also recorded in `comparison.md`.

## Part F - Verify Behaviour

- Normal appointment
- Blank patient name
- Two appointments for the same practitioner/time
- Strange input such as patient_name=None or appointment_time=None

### Test results

**Normal appointment:**  
A normal appointment was tested using Charlie Brown, Dr. John Doe and 2024-07-20 12:00 PM. The appointment was added successfully.

**Blank patient name:**  
A blank patient name raised `ValueError: Patient name cannot be empty`.

**Two appointments for the same practitioner/time:**  
The program accepted both appointments. This showed that there is currently no check to prevent appointment conflicts.

**Strange input:**  
An appointment with `appointment_time=None` was accepted. This showed that the appointment time is not currently validated.

## Part G - Improve One Thing

**Choose exactly one controlled improvement, for example:**

```python
if not patient_name:
    raise ValueError("Patient name cannot be empty")
```

The controlled improvement used was:

```python
if not patient_name:
    raise ValueError("Patient name cannot be empty")
```

This prevents an appointment from being added when the patient name is empty.

## Part H - Reflection (150-250 words)

**What did you build before using AI?**

**What did AI help you understand?**

**Did AI make assumptions?**

**How did you verify the AI output?**

**What engineering work remained for you?**

The completed reflection is recorded in `reflection.md`.

## Submission checklist [GitHub Commit]

- Python file runs.
- Comparison table completed.
- Normal and unusual inputs tested.
- AI assistance documented.
- Reflection completed.
- I can explain my code.
