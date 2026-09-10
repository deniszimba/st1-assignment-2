# Stage 1 Lab - Human vs AI: Building Your First SmartCare Prototype

## Part A - Understand the Problem

### What data must be stored?

The patient's name, practitioner's name and appointment time.

### What functions might be useful?

Functions for booking an appointment and displaying appointments.

### What could go wrong?

- The patient name could be left blank.
- Two appointments could be booked with the same practitioner at the same time.
- The practitioner name or appointment time could be missing.
- Incorrect information could be entered.

### What requirements are unclear?

It is not clear how appointments should be changed or cancelled, what validation is required, or whether duplicate appointment times should be prevented.

## Part B - Build a Human-Written Prototype

I created a basic Python prototype that stored two appointments using separate variables for the patient name, practitioner name and appointment time.

I then enhanced the program using a list, dictionaries and functions to make the appointments easier to store and display.

The completed program is stored in:

`smartcare_v01.py`

### Five limitations identified

1. The appointments are hard-coded instead of being entered by the user.
2. The program does not stop two appointments being booked with the same practitioner at the same time.
3. The practitioner name and appointment time are not checked for missing or incorrect values.
4. The appointments are only stored while the program is running and are lost when it closes.
5. There is no way to cancel, edit or search for an appointment.

## Part C - Use AI as Tutor

I used Microsoft Copilot as a tutor to help me understand how functions and lists could improve the basic appointment program.

### Prompt used

> I am a first-year programming student working on a simple Python clinic appointment booking system. Can you explain how functions and lists can improve a basic program that currently stores appointment details in separate variables? Please explain it simply and act as a tutor rather than writing the whole program for me.

Copilot explained that lists can keep multiple appointments together instead of creating separate variables for every appointment. It also explained that functions can be reused for tasks such as adding and displaying appointments.

The AI tutor activity is documented in:

`ai_usage.md`

## Part D - Generate an Alternative

I asked Microsoft Copilot:

> Create a simple beginner-friendly Python function that stores patient name, practitioner name and appointment time for a clinic appointment system. Keep the code suitable for a first-year programming student. Do not use a database or GUI.

The alternative used a function and stored appointment information together. I compared the AI approach with my own version before deciding which ideas were useful.

## Part E - Compare Human and AI Versions

The completed comparison table is stored in:

`comparison.md`

## Part F - Verify Behaviour

### Normal appointment

I tested a normal appointment with a patient name, practitioner name and appointment time.

**Result:** The appointment was added and displayed successfully.

### Blank patient name

I tested the program with a blank patient name.

**Result:** The program raised:

`ValueError: Patient name cannot be empty`

### Same practitioner and appointment time

I tested two appointments with the same practitioner and appointment time.

**Result:** Both appointments were accepted. This showed that the program does not currently prevent appointment conflicts.

### None value

I tested an appointment with `None` as the appointment time.

**Result:** The appointment was accepted and displayed. This showed that the program does not currently validate the appointment time.

## Part G - Improve One Thing

I added one controlled improvement to prevent an appointment from being added when the patient name is empty:

```python
if not patient_name:
    raise ValueError("Patient name cannot be empty")