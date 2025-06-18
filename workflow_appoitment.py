from appoitment import create_simple_appointment
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir, get_patient_id_by_dni, get_appointments_by_patient_id
from datetime import datetime

# Crear uno de ejemplo
if __name__ == "__main__":
    #Parámetros de la consulta
    patient_id="47930297" 
    practitioner_id="1973"
    start_time="2025-06-20T10:00:00Z"
    end_time="2025-06-20T10:30:00Z"
    
    
    appointment = create_simple_appointment(patient_id, practitioner_id, start_time, end_time)
    appotiment_id = send_resource_to_hapi_fhir(appointment, "Appointment")

    if appotiment_id:
        get_resource_from_hapi_fhir(appotiment_id, "Appointment")

    # Buscar todos los appointments de un paciente por DNI
    
    patient_dni="95632418"
    patient_id_by_dni = get_patient_id_by_dni(patient_dni)
    print(patient_id_by_dni)
    if patient_id_by_dni:
        appointments = get_appointments_by_patient_id(patient_id_by_dni)

        if appointments:
            print("\n Próximos appointments:")
            for appt in appointments:
                start = appt.get("start")
                if start:
                    start_dt = datetime.fromisoformat(start.replace("Z", "+00:00"))
                    print(f"- {start_dt} (Estado: {appt.get('status')})")
        else:
            print("No hay turnos programados.")
    