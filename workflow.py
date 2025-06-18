from patient import create_patient_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir, get_resource_from_hapi_fhir_by_dni

if __name__ == "__main__":
    # Parámetros del paciente
    family_name = "Costa de Carvalho"
    given_name = "Mateus"
    birth_date = "1991-07-23"
    gender = "male"
    phone = None 
    DNI = "95632418"

    # Crear y enviar el recurso de paciente
    patient = create_patient_resource(family_name, given_name, birth_date, gender, phone, DNI)
    patient_id = send_resource_to_hapi_fhir(patient, 'Patient')
    print(patient_id)

    # Ver el recurso de paciente creado
    if patient_id:
        get_resource_from_hapi_fhir(patient_id,'Patient')

    if DNI:
        get_resource_from_hapi_fhir_by_dni(DNI,'Patient')
