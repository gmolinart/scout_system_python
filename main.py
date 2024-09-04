import json
import os
from datetime import datetime

def load_data():
    if os.path.exists('pacientes.json'):
        with open('pacientes.json', 'r') as file:
            return json.load(file)
    return {"pacientes": []}

def save_data(data):
    with open('pacientes.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def seleccionar_paciente(data):
    while True:
        print("\n1. Introducir nuevo paciente")
        print("2. Seleccionar paciente existente")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Introduzca el nombre del nuevo paciente: ")
            data["pacientes"].append({"nombre": nombre, "consultas": []})
            save_data(data)
            return nombre
        elif opcion == "2":
            if not data["pacientes"]:
                print("No hay pacientes registrados.")
                continue
            for i, paciente in enumerate(data["pacientes"], 1):
                print(f"{i}. {paciente['nombre']}")
            seleccion = int(input("Seleccione el número del paciente: ")) - 1
            return data["pacientes"][seleccion]["nombre"]

def nueva_consulta(paciente, data):
    consulta = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "motivo": input("Motivo de la visita: "),
        "historial": input("Historial clínico: "),
        "notas": input("Notas adicionales: "),
        "diagnostico": input("Diagnóstico: ")
    }
    for p in data["pacientes"]:
        if p["nombre"] == paciente:
            p["consultas"].append(consulta)
            break
    save_data(data)

def ver_consultas(paciente, data):
    for p in data["pacientes"]:
        if p["nombre"] == paciente:
            if not p["consultas"]:
                print("No hay consultas registradas para este paciente.")
            else:
                for i, consulta in enumerate(p["consultas"], 1):
                    print(f"\nConsulta {i}:")
                    print(f"Fecha: {consulta['fecha']}")
                    print(f"Motivo: {consulta['motivo']}")
                    print(f"Historial: {consulta['historial']}")
                    print(f"Notas: {consulta['notas']}")
                    print(f"Diagnóstico: {consulta['diagnostico']}")
            break

def main():
    data = load_data()
    while True:
        paciente = seleccionar_paciente(data)
        while True:
            print(f"\nPaciente: {paciente}")
            print("1. Nueva consulta")
            print("2. Ver consultas anteriores")
            print("3. Cambiar de paciente")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nueva_consulta(paciente, data)
            elif opcion == "2":
                ver_consultas(paciente, data)
            elif opcion == "3":
                break
            elif opcion == "4":
                return
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
