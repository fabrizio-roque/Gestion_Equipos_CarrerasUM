from datetime import datetime


class Empleado:
    FORMATO_FECHA = "%d-%m-%Y"

    def __init__(self, id, nombre, edad, nacionalidad, fecha_nacimiento, salario, score=None):
        self._id = id
        self._nombre = nombre
        self._edad = edad
        self._nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self._salario = salario
        self._score = score

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, valor):
        try:
            datetime.strptime(valor, self.FORMATO_FECHA)
            self._fecha_nacimiento = valor
        except ValueError:
            raise ValueError(f"La fecha '{valor}' no tiene el formato correcto. Debe ser DD-MM-YYYY.")


class Piloto(Empleado):
    def __init__(self, id, nombre, edad, nacionalidad, fecha_nacimiento, salario, score, numero_auto, puntaje_campeonato, lesionado):
        super().__init__(id, nombre, edad, nacionalidad, fecha_nacimiento, salario, score)
        self._numero_auto = numero_auto
        self._puntaje_campeonato = puntaje_campeonato
        self._lesionado = lesionado


class Mecanico(Empleado):
    pass


class DirectorEquipo(Empleado):
    pass


class Auto:
    def __init__(self, modelo, score, color):
        self._modelo = modelo
        self._score = score
        self._color = color


class Equipo:
    def __init__(self, nombre, pais_origen, ano_creacion):
        self._nombre = nombre
        self._pais_origen = pais_origen
        self._ano_creacion = ano_creacion
        self._empleados = []
        self._modelo_auto = None

    @property
    def nombre(self):
        return self._nombre

    @property
    def pilotos(self):
        return [empleado for empleado in self._empleados if isinstance(empleado, Piloto)]

    def agregar_empleado(self, empleado):
        if isinstance(empleado, Piloto) and len(self.pilotos) >= 2:
            print("Ya hay 2 pilotos en este equipo. No se puede agregar otro.")
            return
        self._empleados.append(empleado)


def obtener_datos_empleado():
    id = int(input_validado("\nIngrese ID: ", tipo=int))
    nombre = input_validado("Ingrese nombre: ", tipo=str)
    edad = input_validado("Ingrese edad: ", tipo=int)
    nacionalidad = input_validado("Ingrese nacionalidad: ", tipo=str)
    
    fecha_nacimiento = ""
    while True:
        fecha_nacimiento = input("Ingrese fecha de nacimiento (DD-MM-YYYY): ")
        try:
            datetime.strptime(fecha_nacimiento, Empleado.FORMATO_FECHA)
            break
        except ValueError:
            print(f"La fecha '{fecha_nacimiento}' no tiene el formato correcto. Debe ser DD-MM-YYYY.")

    salario = input_validado("Ingrese salario: ", tipo=float)
    score = input_validado("Ingrese score: ", tipo=int)
    return id, nombre, edad, nacionalidad, fecha_nacimiento, salario, score


def valida_opcion(minimo, maximo):
    while True:
        try:
            opcion = int(input(f"\nSeleccione una opción ({minimo}-{maximo}): "))
            if minimo <= opcion <= maximo:
                return opcion
            else:
                print(f"Por favor, ingrese una opción entre {minimo} y {maximo}.")
        except ValueError:
            print("Por favor, ingrese un número válido.")


def input_validado(mensaje, tipo):
    while True:
        valor = input(mensaje)
        try:
            if tipo == int:
                return int(valor)
            elif tipo == float:
                return float(valor)
            elif tipo == str and valor:
                return valor.strip()
            else:
                print("Valor inválido. Intente de nuevo.")
        except ValueError:
            print("Valor inválido. Intente de nuevo.")

def simular_carrera(autos, equipos):
    pilotos = []
    for equipo in equipos:
        pilotos_equipo = equipo.pilotos
        if pilotos_equipo:
            piloto_titular = pilotos_equipo[0]
            if piloto_titular._lesionado:
                if len(pilotos_equipo) > 1:
                    piloto_reserva = pilotos_equipo[1]
                    if not piloto_reserva._lesionado:
                        pilotos.append(piloto_reserva)
            else:
                pilotos.append(piloto_titular)

    # Verifica si hay pilotos y autos disponibles
    if not pilotos or not autos:
        print("No hay pilotos y/o autos suficientes para simular una carrera.")
        return

    print("\nSimulación...\n")
    resultados = []

    for piloto in pilotos:
        auto = next((auto for auto in autos if auto._modelo == piloto._numero_auto), None)
        if auto:
            score_final = (piloto._score + auto._score) / 2
            resultados.append((piloto._nombre, score_final))

    resultados.sort(key=lambda x: x[1], reverse=True)  # Ordena los resultados de mayor a menor score

    print("Resultados de la carrera:")
    for i, (nombre, score) in enumerate(resultados, 1):
        print(f"{i}. {nombre} - Score: {score:.2f}")

def realizar_consultas(equipos):
    while True:
        print("\nSeleccione una opción de consulta:")
        print("1. Lista de empleados por equipo.")
        print("2. Pilotos lesionados.")
        print("3. Volver al menú principal.")
        
        opcion = valida_opcion(1, 6)
        
        if opcion == 1:
            pass
        
        elif opcion == 2:
            pass
        
        elif opcion == 3:
            pass
        
        elif opcion == 4:
            pass
        
        elif opcion == 5:
            pass
        
        elif opcion == 6:
            pass

def main():
    equipos = []
    autos = []

    while True:
        print("1. Alta de empleado")
        print("2. Alta de auto")
        print("3. Alta de equipo")
        print("4. Simular carrera")
        print("5. Realizar consultas")
        print("6. Finalizar programa")

        opcion = valida_opcion(1, 6)

        if opcion == 1:
            while True:
                tipo_empleado = input("\nSeleccione el tipo de empleado (Piloto/Mecánico/Director) o 'salir' para volver al menú principal: ").lower().strip()

                if tipo_empleado not in ["piloto", "mecanico", "director", "salir"]:
                    print("Opción no válida. Intente de nuevo.")
                    continue
                elif tipo_empleado == "salir":
                    break

                id, nombre, edad, nacionalidad, fecha_nacimiento, salario, score = obtener_datos_empleado()

                if tipo_empleado == "piloto":
                    numero_auto = input_validado("Ingrese número de auto: ", tipo=int)
                    puntaje_campeonato = input_validado("Ingrese puntaje de campeonato: ", tipo=int)
                    lesionado_input = ""
                    while lesionado_input not in ["si", "no"]:
                        lesionado_input = input("¿Está lesionado? (Sí/No): ").lower().strip()
                    lesionado = lesionado_input == "si"
                    empleado = Piloto(id, nombre, edad, nacionalidad, fecha_nacimiento, salario, score, numero_auto, puntaje_campeonato, lesionado)
                elif tipo_empleado == "mecanico":
                    empleado = Mecanico(id, nombre, edad, nacionalidad, fecha_nacimiento, salario, score)
                elif tipo_empleado == "director":
                    empleado = DirectorEquipo(id, nombre, edad, nacionalidad, fecha_nacimiento, salario)
                else:
                    print("Tipo de empleado no válido.")
                    continue

                while True:
                    equipo_asociado = input_validado(f"Ingrese el nombre del equipo al que pertenece el {tipo_empleado}: ", tipo=str)
                    equipo_encontrado = next((equipo for equipo in equipos if equipo.nombre.lower() == equipo_asociado.lower()), None)

                    if equipo_encontrado:
                        equipo_encontrado.agregar_empleado(empleado)
                        print(f"\n{tipo_empleado.capitalize()} agregado al equipo {equipo_asociado}.")
                        break
                    else:
                        decision = ""
                        while decision not in ["si", "no"]:
                            decision = input(f"No se encontró el equipo {equipo_asociado}. ¿Desea crear el equipo {equipo_asociado}? (si/no): ").lower().strip()

                        if decision == "si":
                            pais_origen = input_validado("Ingrese país de origen: ", tipo=str)
                            ano_creacion = input_validado("Ingrese año de creación: ", tipo=int)
                            equipo = Equipo(equipo_asociado, pais_origen, ano_creacion)
                            equipo.agregar_empleado(empleado)
                            equipos.append(equipo)
                            print(f"\nEquipo {equipo_asociado} creado y {tipo_empleado.capitalize()} agregado.")
                            break
                        else:
                            print("Por favor, ingrese el nombre de un equipo existente o cree uno nuevo.")

        elif opcion == 2:
            modelo = input("Ingrese modelo del auto: ")
            score = int(input("Ingrese score: "))
            color = input("Ingrese color: ")
            auto = Auto(modelo, score, color)
            autos.append(auto)
            print("Auto creado correctamente")

        elif opcion == 3:
            nombre = input("Ingrese nombre del equipo: ")
            pais_origen = input("Ingrese país de origen: ")
            year_creacion = int(input("Ingrese año de creación: "))
            equipo = Equipo(nombre, pais_origen, year_creacion)
            equipos.append(equipo)
        elif opcion == 4:
            simular_carrera(autos, equipos)
        elif opcion == 5:
            realizar_consultas(equipos)
        elif opcion == 6:
            break


main()
