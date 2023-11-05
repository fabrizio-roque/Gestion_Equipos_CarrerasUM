from datetime import datetime
import random # Solo para simular la carrera

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

class Imprevisto:
    def __init__(self):
        self.lesionado = False
        self.abandono = False
        self.errores_en_pits = 0
        self.penalidades = 0
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
import random

def generar_imprevistos_aleatorios():
    imprevisto = Imprevisto()
    
    # Supongamos que hay un 10% de probabilidad de que un piloto se lesione
    if random.random() < 0.10:
        imprevisto.lesionado = True
        
    # 5% de probabilidad de que un piloto abandone
    if random.random() < 0.05:
        imprevisto.abandono = True
        
    # Un piloto podría cometer entre 0 y 3 errores en pits
    imprevisto.errores_en_pits = random.randint(0, 3)
    
    # Un piloto podría recibir entre 0 y 2 penalidades
    imprevisto.penalidades = random.randint(0, 2)
    
    return imprevisto

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

    # Recopilar imprevistos antes de iniciar la carrera
    imprevistos_pilotos = {}
    for piloto in pilotos:
        imprevisto = generar_imprevistos_aleatorios()
        imprevistos_pilotos[piloto._id] = imprevisto

    print("\nSimulación...\n")
    resultados = []

    for piloto in pilotos:
        auto = next((auto for auto in autos if auto._modelo == piloto._numero_auto), None)
        if auto:
            imprevisto = imprevistos_pilotos[piloto._id]
            
            if imprevisto.abandono:
                score_final = 0
            else:
                # Suponiendo que la suma_score_mecanicos es un valor constante
                # si necesitas calcularlo, deberás agregar la lógica correspondiente
                suma_score_mecanicos = 10  # Valor de ejemplo
                score_final = suma_score_mecanicos + auto._score + piloto._score - 5 * imprevisto.errores_en_pits - 8 * imprevisto.penalidades

            resultados.append((piloto._nombre, score_final))

    resultados.sort(key=lambda x: x[1], reverse=True)  # Ordena los resultados de mayor a menor score

    print("Resultados de la carrera:")
    puntos = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
    for i, (nombre, score) in enumerate(resultados, 1):
        if i <= len(puntos):
            print(f"{i}. {nombre} - Score: {score:.2f} - Puntos obtenidos: {puntos[i-1]}")
        else:
            print(f"{i}. {nombre} - Score: {score:.2f}")

def realizar_consultas(equipos):
    while True:
        print("\nSeleccione una opción de consulta:")
        print("1. Top 10 pilotos con más puntos en el campeonato.")
        print("2. Resumen campeonato de constructores (equipos).")
        print("3. Top 5 pilotos mejor pagados.")
        print("4. Top 3 pilotos más habilidosos.")
        print("5. Retornar jefes de equipo.")
        print("6. Volver al menú principal.")
        
        opcion = valida_opcion(1, 6)
        
        if opcion == 1:
            pilotos = [piloto for equipo in equipos for piloto in equipo.pilotos]
            top_10_pilotos = sorted(pilotos, key=lambda x: x._puntaje_campeonato, reverse=True)[:10]
            print("\nTop 10 pilotos con más puntos en el campeonato:")
            for piloto in top_10_pilotos:
                print(f"{piloto._nombre} - {piloto._puntaje_campeonato} puntos")
                
        elif opcion == 2:
            print("\nResumen campeonato de constructores (equipos):")
            for equipo in equipos:
                total_puntos = sum([piloto._puntaje_campeonato for piloto in equipo.pilotos])
                print(f"{equipo.nombre} - {total_puntos} puntos")

        elif opcion == 3:
            pilotos = [piloto for equipo in equipos for piloto in equipo.pilotos]
            top_5_pagados = sorted(pilotos, key=lambda x: x._salario, reverse=True)[:5]
            print("\nTop 5 pilotos mejor pagados:")
            for piloto in top_5_pagados:
                print(f"{piloto._nombre} - ${piloto._salario:.2f}")
        
        elif opcion == 4:
            pilotos = [piloto for equipo in equipos for piloto in equipo.pilotos]
            top_3_habilidosos = sorted(pilotos, key=lambda x: x._score, reverse=True)[:3]
            print("\nTop 3 pilotos más habilidosos:")
            for piloto in top_3_habilidosos:
                print(f"{piloto._nombre} - Score: {piloto._score}")
        
        elif opcion == 5:
            directores = [empleado for equipo in equipos for empleado in equipo._empleados if isinstance(empleado, DirectorEquipo)]
            print("\nJefes de equipo:")
            for director in directores:
                print(director._nombre)

        elif opcion == 6:
            break

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
