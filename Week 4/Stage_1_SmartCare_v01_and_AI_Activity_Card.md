# SmartCare v0.1 - Initial Engineering Brief and AI Activity Card

**A2 Case Study Stage 1 student resource**

## SmartCare scenario

SmartCare Community Clinic currently uses spreadsheets and paper records to manage patients and appointments. The client says: 'We need software to help manage patients, practitioners and appointments.' This is not yet a complete specification.

# Initial Engineering Brief

## 1. Problem summary

**Write approximately 100 words.**

SmartCare Community Clinic currently uses spreadsheets and paper records to manage patient and appointment information. This can make the clinic's processes harder to manage and may lead to problems when storing and finding information. The clinic wants a software system that can help manage patients, practitioners and appointments in a more organised way. However, the client has only provided a basic description of what they need, so the requirements are not yet complete. More information needs to be collected from the client before deciding exactly what features the system should include and how the system should work.

## 2. Initial stakeholders

| Stakeholder | Possible need |
|---|---|
| Patients | Have their details and appointments managed correctly. |
| Receptionists / clinic staff | Manage patient information and appointments easily. |
| Practitioners | View their appointment information and schedules. |
| Clinic management | Improve how patient, practitioner and appointment information is managed. |

## 3. Initial features

| Feature | Confirmed or provisional? | Why? |
|---|---|---|
| Manage patients | Confirmed | The client specifically said the software should help manage patients. |
| Manage practitioners | Confirmed | The client specifically said the software should help manage practitioners. |
| Manage appointments | Confirmed | The client specifically said the software should help manage appointments. |
| Practitioner schedule view | Provisional | It could be useful, but the client has not specifically requested it yet. |

## 4. Questions for the client

1. What patient information needs to be stored?
2. What practitioner information needs to be stored?
3. What information should be recorded for each appointment?
4. Who should be allowed to create, change or cancel appointments?
5. Do practitioners need to be able to view their appointment schedules?

## 5. What we do not yet know

1. Exactly what information needs to be stored for each patient and practitioner.
2. Who should have access to different parts of the system.
3. How appointments should be changed, cancelled or kept in appointment history.

# AI Activity Card - Ask, Check, Explain

## Before AI

**What do I think the code does? What problems can I already identify?**

The code stores patient, practitioner and appointment time information and displays the appointments. I can already identify that it does not prevent duplicate appointments, does not fully validate the information entered and only stores the appointments while the program is running.

## AI request

**Act as a tutor. Explain this code and identify potential problems. Do not provide a complete replacement. Ask me questions that help me reason about the solution.**

## Evaluate

| Suggestion | Useful | Unclear | Incorrect | Out of scope |
|---|---|---|---|---|
| Use a list to store multiple appointments | Yes | | | |
| Use functions to add appointments | Yes | | | |
| Use user input for appointment details | Yes | | | |
| Store each appointment together instead of separate variables | Yes | | | |

## Decide

**For each significant suggestion: Accept / Modify / Reject / Keep unverified.**

- Use a list to store appointments – Accept
- Use functions to add appointments – Accept
- Use user input – Keep unverified
- Store appointment details together – Accept

## Verify

- Run the code
- Test normal input
- Test unusual input
- Compare with requirements
- Ask tutor/peer
- Check documentation

I ran the code and tested normal and unusual inputs. I tested a normal appointment, a blank patient name, two appointments with the same practitioner and time, and a None value for the appointment time. I also compared the results with the SmartCare requirements and identified limitations in the program.

## Explain

**Can I explain the final code without reading the AI response? What do I still need to understand?**

Yes, I can explain the final code without reading the AI response. I understand how the list stores appointments, how the functions add and display appointments, and how the patient name validation works. I still need to learn more about validating other inputs and preventing duplicate appointment times.