print("Hola, bienvenido a su Hsmart, seleccione una opción")
menu = [
    '1. Configuración de temperatura',
    '2. Control',
    '3. Programar horario',
    '4. Salir',
]
Areas_de_la_casa = ('Cocina', 'Sala', 'Comedor', 'Baño')
temperatura_fija = 22
opcion = ''

Temperatura_registrada = [temperatura_fija] * len(Areas_de_la_casa)
Programacion_horaria = {area: {} for area in Areas_de_la_casa}

while opcion != '4':
    # Mostrar el menú principal
    for item in menu:
        print('\n' + item)
    
    print("Ingrese número de opción")
    opcion = input().strip()
    
    if opcion == '1':
        print("Ingresando a configuración de temperatura.... ")
        print("Seleccione un área de la casa")
        while True:
            try:
                for i, area in enumerate(Areas_de_la_casa):
                    print(f"{i + 1}. {area}")
                area_seleccionada = int(input("Ingrese el número del área: ").strip()) - 1
                if 0 <= area_seleccionada < len(Areas_de_la_casa):
                    break
                else:
                    print("Número inválido. Intente nuevamente.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número válido.")
        
        print(f"Temperatura actual para {Areas_de_la_casa[area_seleccionada]}: {Temperatura_registrada[area_seleccionada]}°C")
        while True:
            print("Ingrese la nueva temperatura deseada (entre 14°C y 32°C)")
            nueva_temperatura = float(input().strip())
            if 14 <= nueva_temperatura <= 32:
                break
            else:
                print("Temperatura fuera del rango. Ingrese nuevamente una.")
        Temperatura_registrada[area_seleccionada] = nueva_temperatura
        print(f"Temperatura para {Areas_de_la_casa[area_seleccionada]} actualizada a {nueva_temperatura}°C") 
        
    elif opcion == '2':
        print("Visualizando temperatura actual.....")
        # Mostrar la temperatura actual en todas las áreas
        for i, area in enumerate(Areas_de_la_casa):
            print(f"{i + 1}. {area}: {Temperatura_registrada[i]}°C")
        cambiar_temperatura = input("¿Desea cambiar la temperatura? (si/no): ").strip().lower()
        if cambiar_temperatura == "si":
            opcion = "1" # Cambiar la opción a 1 (Configuracion de temperatura)

    elif opcion == '3':
        print("Ingresando a programación de horario.....")
        print("Seleccione un área de la casa")
        # Seleccionar un área
        while True:
            try:
                for i, area in enumerate(Areas_de_la_casa):
                    print(f"{i + 1}. {area}")
                area_seleccionada = int(input("Ingrese el número del área: ").strip()) - 1
                if 0 <= area_seleccionada < len(Areas_de_la_casa):
                    break
                else:
                    print("Número inválido. Intente nuevamente.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número válido.")

        while True:
            try:
                hora_inicio = input("Ingrese la hora de inicio (formato HH:MM): ").strip()
                hora_fin = input("Ingrese la hora de fin (formato HH:MM): ").strip()
                temperatura_programada = float(input("Ingrese la temperatura deseada para el horario: ").strip())
                if 14 <= temperatura_programada <= 32:
                    break
                else:
                    print("Temperatura incorrecta. Ingrese una válida.")
            except ValueError:
                print("Formato de hora o temperatura inválido. Ingrese nuevamente.")

        Programacion_horaria[Areas_de_la_casa[area_seleccionada]] = {
            "hora_inicio": hora_inicio,
            "hora_fin": hora_fin,
            "temperatura": temperatura_programada
        }
        print(f"Programación agregada para {Areas_de_la_casa[area_seleccionada]} de {hora_inicio} a {hora_fin} con temperatura {temperatura_programada}°C")

    
    elif opcion == '4':
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida del menú")