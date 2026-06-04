import json

while True:

    print("\n=== Recordatorio de Medicinas ===")
    print("1. Agregar medicina")
    print("2. Ver medicinas")
    print("3. Eliminar medicina")
    print("4. Marcar como tomada")
    print("5. Ver pendientes")
    print("6. Buscar medicina")
    print("7. Saliendo...")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        medicina = input("Escribe el nombre de la medicina: ")
        hora = input("Escribe la hora: ")
        fecha = input("Escribe la fecha: ")

        with open("medicinas.json", "r") as archivo:
            medicinas = json.load(archivo)

        medicinas.append(f"{medicina} - {hora} - {fecha} - Pendiente")

        with open("medicinas.json", "w") as archivo:
            json.dump(medicinas, archivo)

        print("Medicina guardada:", medicina)

    elif opcion == "2":
        with open("medicinas.json", "r") as archivo:
            medicinas = json.load(archivo)

        print("Tus medicinas:")

        for medicina in medicinas:
            print("-", medicina)

    elif opcion == "3":
        with open("medicinas.json", "r") as archivo:
            medicinas = json.load(archivo)

        print("Medicinas registradas:")

        for i, medicina in enumerate(medicinas):
            print(i + 1, "-", medicina)

        eliminar = int(input("Número de la medicina que quieres eliminar: "))

        if 1 <= eliminar <= len(medicinas):
            medicinas.pop(eliminar - 1)

            with open("medicinas.json", "w") as archivo:
                json.dump(medicinas, archivo)

            print("Medicina eliminada correctamente")
        else:
            print("Número inválido")

    elif opcion == "4":
        with open("medicinas.json", "r") as archivo:
            medicinas = json.load(archivo)

        print("Medicinas registradas:")

        for i, medicina in enumerate(medicinas):
            print(i + 1, "-", medicina)

        numero = int(input("Número de la medicina tomada: "))

        if 1 <= numero <= len(medicinas):
            medicinas[numero - 1] = medicinas[numero - 1].replace("Pendiente", "Tomada")

            with open("medicinas.json", "w") as archivo:
                json.dump(medicinas, archivo)

            print("Medicina marcada como tomada")
        else:
            print("Número inválido")

    elif opcion == "5":
        with open("medicinas.json", "r") as archivo:
            medicinas = json.load(archivo)

        print("Medicinas pendientes:")

        for medicina in medicinas:
            if "Pendiente" in medicina:
                print("-", medicina)

    elif opcion == "6":
       buscar = input("Escribe el nombre de la medicina: ")

       with open("medicinas.json", "r") as archivo:
        medicinas = json.load(archivo)

       print("Resultados encontrados:")

       for medicina in medicinas:
           if buscar.lower() in medicina.lower():1
              print("-", medicina)

    elif opcion == "7":
        print("Saliendo...")
        break

    else:
        print("Por favor elige otra opcion")