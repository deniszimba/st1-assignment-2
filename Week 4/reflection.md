# Stage 1 Reflection

Before using AI, I built a basic SmartCare appointment booking prototype in Python. The first version stored the patient name, practitioner name and appointment time in separate variables. I then worked with a version that used a list, dictionaries and functions to make the appointments easier to store and display.

Using Microsoft Copilot helped me understand why functions and lists are useful when a program starts getting bigger. Instead of creating separate variables for every appointment, a list can store multiple appointments and functions can be reused for tasks such as adding and displaying them. Copilot also generated an alternative version that used user input and stored each appointment as a list.

The AI did make some assumptions. For example, its version assumed that the user would enter valid information and did not include input validation. I verified the ideas by running the code and testing different inputs. I tested a normal appointment, a blank patient name, two appointments with the same practitioner and time, and an appointment with None as the time.

The engineering work still required me to test the program, identify limitations, compare the different approaches and decide which improvements were appropriate for the SmartCare requirements.