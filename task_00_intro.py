import os

def generate_invitations(template, attendees):
    if type(template) is not str:
        print("Error: template are not string")
        return 
    if type(attendees) is not list or not all(type(a) is dict for a in attendees):
        print("Error: value of attendees is not Dict or attendees are not a list")
        return
    if not template:
        print(" template is empty")
        return
    if not attendees:
        print("attendees list is empty")

    
    for idx, attendee in enumerate(attendees, start=1):
        content = template.format(
            name=attendee.get("name", ""),
            event_title=attendee.get("event_title", ""),
            event_date=attendee.get("event_date", ""),
            event_location=attendee.get("event_location", "")
        )
        with open(f'output_{idx}.txt', 'w') as file:
            file.write(content)

