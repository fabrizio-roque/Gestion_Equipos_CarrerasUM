class Empleado:
    def __init__(self, id, nombre, edad, nacionalidad, fecha_nacimiento, salario):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.salario = salario

class Piloto(Empleado):
    def __init__(self, id, nombre, edad, nacionalidad, fecha_nacimiento, salario, score, numero_auto, puntaje_campeonato, lesionado):
        super().__init__(id, nombre, edad, nacionalidad, fecha_nacimiento, salario)
        self.score = score
        self.numero_auto = numero_auto
        self.puntaje_campeonato = puntaje_campeonato
        self.lesionado = lesionado

class Mecanico(Empleado):
    def __init__(self, id, nombre, edad, nacionalidad, fecha_nacimiento, salario, score):
        super().__init__(id, nombre, edad, nacionalidad, fecha_nacimiento, salario)
        self.score = score

class DirectorEquipo(Empleado):
    def __init__(self, id, nombre, edad, nacionalidad, fecha_nacimiento, salario):
        super().__init__(id, nombre, edad, nacionalidad, fecha_nacimiento, salario)

class Auto:
    def __init__(self, modelo, score, color):
        self.modelo = modelo
        self.score = score
        self.color = color

class Equipo:
    def __init__(self, nombre, pais_origen, ano_creacion):
        self.nombre = nombre
        self.pais_origen = pais_origen
        self.ano_creacion = ano_creacion
        self.empleados = []
        self.modelo_auto = None

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def asignar_modelo_auto(self, modelo_auto):
        self.modelo_auto = modelo_auto

def main():
    equipos = []
    while True:
        print("1. Alta de empleado")
        print("2. Alta de auto")
        print("3. Alta de equipo")
        print("4. Simular carrera")
        print("5. Realizar consultas")
        print("6. Finalizar programa")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            while True:
                print("Opción 1 - Alta de empleado")
                tipo_empleado = input("Seleccione el tipo de empleado (Piloto/Mecánico/Director) para volver escriba Salir ").lower()
            
                if tipo_empleado == "piloto":
                    id = int(input("\n\nIngrese ID: "))
                    nombre = input("\nIngrese nombre: ")
                    edad = int(input("\nIngrese edad: "))
                    nacionalidad = input("\nIngrese nacionalidad: ")
                    fecha_nacimiento = input("\nIngrese fecha de nacimiento: ")
                    salario = float(input("\nIngrese salario: "))  # Usar float para salario si admite decimales
                    score = int(input("\nIngrese score: "))
                    numero_auto = int(input("\nIngrese número de auto: "))
                    puntaje_campeonato = int(input("\nIngrese puntaje de campeonato: "))
                    lesionado = input("\n¿Está lesionado? (Sí/No): ").lower() == "si"
                    empleado = Piloto(id, nombre, edad, nacionalidad, fecha_nacimiento, salario, score, numero_auto, puntaje_campeonato, lesionado)
                    print('El piloto se ha creado correctamente')
                
                elif tipo_empleado == "mecanico":
                    id = int(input("\n\nIngrese ID: "))
                    nombre = input("\nIngrese nombre: ")
                    edad = int(input("\nIngrese edad: "))
                    nacionalidad = input("\nIngrese nacionalidad: ")
                    fecha_nacimiento = input("\nIngrese fecha de nacimiento: ")
                    salario = float(input("\nIngrese salario: "))
                    score = int(input("\nIngrese score: "))
                    empleado = Mecanico(id, nombre, edad, nacionalidad, fecha_nacimiento, salario, score)
                    print('El mecánico se ha creado correctamente')
               
                elif tipo_empleado == "director":
                    id = int(input("\n\nIngrese ID: "))
                    nombre = input("\nIngrese nombre: ")
                    edad = int(input("\nIngrese edad: "))
                    nacionalidad = input("\nIngrese nacionalidad: ")
                    fecha_nacimiento = input("\nIngrese fecha de nacimiento: ")
                    salario = float(input("\nIngrese salario: "))
                    empleado = DirectorEquipo(id, nombre, edad, nacionalidad, fecha_nacimiento, salario)
                    print('El director se ha creado correctamente')
                elif tipo_empleado == "salir":
                    break
                
                else:
                    print("\n\nTipo de empleado no válido.")
                    return
                while True:
                    equipo_asociado = input(f"\nIngrese el nombre del equipo al que pertenece el {tipo_empleado}:")
                    equipo_encontrado = None
                    for equipo in equipos:
                        if equipo.nombre.lower() == equipo_asociado.lower():
                            equipo_encontrado = equipo
                            break
                            
                    if equipo_encontrado:
                        equipo_encontrado.agregar_empleado(empleado)
                        print(f"\n{tipo_empleado.capitalize()} agregado al equipo {equipo_asociado}.")
                    else:
                        print(f"\nNo se encontró el equipo {equipo_asociado}.")
                        equipo_nuevo = input(f"\nDesea crear el equipo {equipo_asociado}? Escriba si o no en caso de querer insertar el Empleado en otro equipo.").lower() == "si"
                        if equipo_nuevo:
                            nombre = equipo_asociado
                            pais_origen = input("\nIngrese país de origen: ")
                            ano_creacion = int(input("\nIngrese año de creación: "))
                            equipo = Equipo(nombre, pais_origen, ano_creacion)
                            equipo.agregar_empleado(empleado)
                            equipos.append(equipo)
                            print(f"\n{tipo_empleado.capitalize()} agregado al equipo {equipo_asociado}.")
                            break
                        
                        

            
        elif opcion == 2:
            # Lógica para Alta de auto
            pass
        elif opcion == 3:
            # Lógica para Alta de equipo
            nombre = input("Ingrese nombre del equipo: ")
            pais_origen = input("Ingrese país de origen: ")
            year_creacion = int(input("Ingrese año de creación: "))
            equipo = Equipo(nombre, pais_origen, year_creacion)
            equipos.append(equipo)
        elif opcion == 4:
            # Lógica para Simular carrera
            pass
        elif opcion == 5:
            # Lógica para Realizar consultas
            pass
        elif opcion == 6:
            break


main()

        
