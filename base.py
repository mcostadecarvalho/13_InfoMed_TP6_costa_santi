import requests
from patient import create_patient_resource
from appoitment import create_simple_appointment


# Enviar el recurso FHIR al servidor HAPI FHIR
def send_resource_to_hapi_fhir(resource,resource_type):
    url = f"http://hapi.fhir.org/baseR4/{resource_type}"
    headers = {"Content-Type": "application/fhir+json"}
    resource_json = resource.json()

    response = requests.post(url, headers=headers, data=resource_json)

    if response.status_code == 201:
        print("Recurso creado exitosamente")
        
        # Devolver el ID del recurso creado
        return response.json()['id']
    else:
        print(f"Error al crear el recurso: {response.status_code}")
        print(response.json())
        return None

# Buscar el recurso por ID 
def get_resource_from_hapi_fhir(resource_id, resource_type):
    url = f"http://hapi.fhir.org/baseR4/{resource_type}/{resource_id}"
    response = requests.get(url, headers={"Accept": "application/fhir+json"})

    if response.status_code == 200:
        resource = response.json()
        print(resource)
    else:
        print(f"Error al obtener el recurso: {response.status_code}")
        print(response.json())

# Buscar el recurso por DNI
def get_resource_from_hapi_fhir_by_dni(identifier_value, resource_type):
    url = f"http://hapi.fhir.org/baseR4/{resource_type}"
    params = {"identifier":identifier_value}
    response = requests.get(url, params=params, headers={"Accept": "application/fhir+json"})

    if response.status_code == 200:
        resource = response.json()
        print(resource)
    else:
        print(f"Error al obtener el recurso: {response.status_code}")
        print(response.json())

# Buscar id de paciente por el dni
def get_patient_id_by_dni(identifier_value):
    url = "http://hapi.fhir.org/baseR4/Patient"
    params = {"identifier": identifier_value}
    response = requests.get(url, params=params, headers={"Accept": "application/fhir+json"})

    if response.status_code == 200:
        bundle = response.json()
        entries = bundle.get("entry", [])
        if entries:
            patient_id = entries[0]["resource"]["id"]
            print(f"Paciente encontrado: Patient/{patient_id}")
            return patient_id
        else:
            print("No se encontró ningún paciente con ese DNI.")
            return None
    else:
        print("Error al buscar el paciente:", response.status_code)
        return None

# buscar appointments de paciente con el id de paciente
def get_appointments_by_patient_id(patient_id):
    url = "http://hapi.fhir.org/baseR4/Appointment"
    params = {"actor": f"Patient/{patient_id}"}
    response = requests.get(url, params=params, headers={"Accept": "application/fhir+json"})

    if response.status_code == 200:
        bundle = response.json()
        entries = bundle.get("entry", [])
        if entries:
            appointments = [entry["resource"] for entry in entries]
            return appointments
        else:
            print("No se encontraron appointments para el paciente.")
            return []
    else:
        print("Error al buscar appointments:", response.status_code)
        return []
