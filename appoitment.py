from fhir.resources.appointment import Appointment, AppointmentParticipant
from fhir.resources.reference import Reference

def create_simple_appointment(patient_id, practitioner_id, start_time, end_time):
    appointment = Appointment(
        status="booked",
        start=start_time,
        end=end_time,
        participant=[
            AppointmentParticipant(
                actor=Reference(reference=f"Patient/{patient_id}"),
                status="accepted"
            ),
            AppointmentParticipant(
                actor=Reference(reference=f"Practitioner/{practitioner_id}"),
                status="accepted"
            )
        ]
    )

    return appointment