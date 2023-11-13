from datetime import datetime
import time
import sys
import random 

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
        
    def actualizar_puntaje_campeonato(self, puntos):
        self._puntaje_campeonato += puntos


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
        
    @property
    def mecanicos(self):
        return [empleado for empleado in self._empleados if isinstance(empleado, Mecanico)]


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
    score = input_validado("Ingrese score (entre 1 y 99): ", tipo=int, minimo=1, maximo=99)
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
    
    #10% de probabilidad de que un piloto se lesione
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

def input_validado(mensaje, tipo, minimo=None, maximo=None):
    while True:
        valor = input(mensaje)
        try:
            if tipo == int:
                valor_int = int(valor)
                if (minimo is not None and valor_int < minimo) or (maximo is not None and valor_int > maximo):
                    raise ValueError
                return valor_int
            elif tipo == float:
                return float(valor)
            elif tipo == str and valor:
                return valor.strip()
            else:
                print("Valor inválido. Intente de nuevo.")
        except ValueError:
            print("Valor inválido. Intente de nuevo.")
            
def tiene_suficientes_mecanicos(equipo):
    return len([empleado for empleado in equipo._empleados if isinstance(empleado, Mecanico)]) >= 8
           
def print_loading(duration=5):
    end_time = time.time() + duration
    load_chars = ['|', '/', '-', '\\']
    i = 0

    while time.time() < end_time:
        sys.stdout.write('\r' + load_chars[i % len(load_chars)] + " Simulando...")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1

    sys.stdout.write('\rCarrera Finalizada...\n')
    
def simular_carrera(autos, equipos):
    
    pilotos = []
    
    # Filtrar equipos que tienen suficientes mecánicos
    equipos_calificados = [equipo for equipo in equipos if tiene_suficientes_mecanicos(equipo)]
    equipos_descalificados = [equipo for equipo in equipos if not tiene_suficientes_mecanicos(equipo)]

    # Imprimir equipos calificados y descalificados
    print("Equipos calificados para la carrera:\n")
    for equipo in equipos_calificados:
        print(f"- {equipo.nombre}")
    print("\n")
    print("\nEquipos descalificados por falta de mecánicos:\n")
    for equipo in equipos_descalificados:
        print(f"- {equipo.nombre}")
    print("\n")
    # Verifica si hay equipos calificados para la carrera
    if not equipos_calificados:
        print("\nNo hay equipos con suficientes mecánicos para iniciar la carrera.\n")
        return

    for equipo in equipos_calificados:
        pilotos_equipo = equipo.pilotos
        if pilotos_equipo:
            piloto_titular = pilotos_equipo[0]
            if piloto_titular._lesionado and len(pilotos_equipo) > 1:
                piloto_reserva = pilotos_equipo[1]
                if not piloto_reserva._lesionado:
                    pilotos.append(piloto_reserva)
            else:
                pilotos.append(piloto_titular)

    # Verifica si hay pilotos disponibles para la carrera
    if not pilotos:
        print("No hay pilotos disponibles para la carrera.")
        return

    # Recopilar imprevistos antes de iniciar la carrera
    imprevistos_pilotos = {}
    for piloto in pilotos:
        imprevisto = generar_imprevistos_aleatorios()
        imprevistos_pilotos[piloto._id] = imprevisto

    print_loading()
    resultados = []
    
    for piloto in pilotos:
        auto = next((auto for auto in autos if auto._modelo == piloto._numero_auto), None)
        if auto:
            imprevisto = imprevistos_pilotos[piloto._id]
            
            if imprevisto.abandono:
                score_final = 0
            else:
                suma_score_mecanicos = 10  # Valor de ejemplo
                score_final = suma_score_mecanicos + auto._score + piloto._score - 5 * imprevisto.errores_en_pits - 8 * imprevisto.penalidades

            resultados.append((piloto, score_final))

    resultados.sort(key=lambda x: x[1], reverse=True)

    print("Resultados de la carrera:")
    puntos = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
    for i, (piloto, score) in enumerate(resultados, 1):
        puntos_adicionales = puntos[i-1] if i <= len(puntos) else 0
        piloto.actualizar_puntaje_campeonato(puntos_adicionales)
        print(f"{i}. {piloto._nombre} - Score: {score:.2f} - Puntos obtenidos: {puntos_adicionales}")
    print("")
        
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
def configurar_prueba_y_simular(equipos, autos):
    # Limpiamos los datos existentes para la prueba
    equipos.clear()
    autos.clear()

    # Creando autos de prueba
    autos.append(Auto("Ferrari", 90, "Rojo"))
    autos.append(Auto("Lamborghini", 85, "Azul"))
    autos.append(Auto("Nissan", 88, "Verde"))
    autos.append(Auto("Renault", 92, "Amarillo"))
    autos.append(Auto("Redbull", 87, "Blanco"))
    autos.append(Auto("BMW", 91, "Violeta"))
    autos.append(Auto("BYD", 95, "Celeste"))
    autos.append(Auto("Audi", 80, "Naranja"))
    autos.append(Auto("Chevrolet", 80, "Naranja"))
    autos.append(Auto("Alfa Romeo", 80, "Naranja"))

    # Creando equipos y empleados de prueba
    equipo1 = Equipo("RedBull", "País1", 2000)
    equipo2 = Equipo("Mercedes", "País2", 2001)
    equipo3 = Equipo("Alpine", "País3", 1999)
    equipo4 = Equipo("Aston Martin", "País4", 2002)
    equipo5 = Equipo("Haas", "País5", 2003)
    equipo6 = Equipo("Ferrari", "País6", 2004)
    equipo7 = Equipo("Peru", "País7", 2005)
    equipo8 = Equipo("Argentina", "País8", 2006)
    equipo9 = Equipo("Uruguay", "País9", 2007)
    equipo10 = Equipo("Brasil", "País10", 2008)
    
    
    # Pilotos
    piloto1 = Piloto(1, "Agustin", 30, "Italiana", "01-01-2002", 50000, 95, "Ferrari", 10, False)
    piloto2 = Piloto(2, "German", 32, "Uruguaya", "02-02-1988", 60000, 92, "Lamborghini", 8, False)
    piloto3 = Piloto(3, "Arturo", 28, "Brasilera", "03-03-1992", 55000, 90, "Nissan", 6, False)
    piloto4 = Piloto(4, "Juan", 35, "Argentina", "04-04-1985", 65000, 88, "Renault", 4, False)
    piloto5 = Piloto(5, "Axel", 33, "Uruguaya", "05-05-1987", 70000, 85, "Audi", 2, False)
    piloto6 = Piloto(6, "Matias", 31, "Argentina", "06-06-1989", 75000, 82, "Redbull", 0, False)
    piloto7 = Piloto(7, "Joaquin", 29, "Peruana", "07-07-1991", 80000, 80, "BMW", 0, False)
    piloto8 = Piloto(8, "Marcos", 27, "Peruana", "08-08-1993", 85000, 78, "BYD", 0, False)
    piloto9 = Piloto(9, "Sebastian", 25, "Boaliviana", "09-09-1995", 90000, 75, "Chevrolet", 0, False)
    piloto10 = Piloto(10, "Alberto", 23, "Mexicana", "09-09-1995", 95000, 72, "Alfa Romeo", 0, False)

    # Mecánicos
    mecanico1 = Mecanico(4, "Mecanico1", 40, "Francesa", "04-04-1980", 40000, 80)
    mecanico2 = Mecanico(5, "Mecanico2", 38, "Francesa", "05-05-1982", 42000, 85)
    mecanico3 = Mecanico(6, "Mecanico3", 36, "Francesa", "06-06-1984", 44000, 90)
    mecanico4 = Mecanico(7, "Mecanico4", 34, "Francesa", "07-07-1986", 46000, 95)
    mecanico5 = Mecanico(8, "Mecanico5", 32, "Francesa", "08-08-1988", 48000, 85)
    mecanico6 = Mecanico(9, "Mecanico6", 30, "Francesa", "09-09-1990", 50000, 85)
    mecanico7 = Mecanico(10, "Mecanico7", 28, "Francesa", "10-10-1992", 52000, 85)
    mecanico8 = Mecanico(11, "Mecanico8", 26, "Francesa", "11-11-1994", 54000, 85)
    mecanico9 = Mecanico(12, "Mecanico9", 24, "Francesa", "12-12-1996", 56000, 85)
    mecanico10 = Mecanico(13, "Mecanico10", 22, "Francesa", "09-09-1995", 58000, 85)
    mecanico11 = Mecanico(14, "Mecanico11", 22, "Francesa", "09-09-1995", 58000, 85)
    mecanico12 = Mecanico(15, "Mecanico12", 22, "Francesa", "09-09-1995", 58000, 85)
    mecanico13 = Mecanico(16, "Mecanico13", 22, "Francesa", "09-09-1995", 58000, 85)
    mecanico14 = Mecanico(17, "Mecanico14", 22, "Francesa", "09-09-1995", 58000, 85)
    mecanico15 = Mecanico(18, "Mecanico15", 22, "Francesa", "09-09-1995", 58000, 85)
    mecanico16 = Mecanico(19, "Mecanico16", 22, "Francesa", "09-09-1995", 58000, 85)
    mecanico17 = Mecanico(20, "Mecanico17", 22, "Francesa", "09-09-1995", 58000, 85)
    mecanico18 = Mecanico(21, "Mecanico18", 22, "Francesa", "09-09-1995", 58000, 85)
    mecanico19 = Mecanico(22, "Mecanico19", 22, "Francesa", "09-09-1995", 58000, 85)
    mecanico20 = Mecanico(23, "Mecanico20", 22, "Francesa", "09-09-1995", 58000, 85)
    mecanico21 = Mecanico(24, "Mecanico21", 22, "Francesa", "09-09-1995", 58000, 85)
    mecanico22 = Mecanico(25, "Mecanico22", 22, "Francesa", "09-09-1995", 58000, 85)
    mecanico23 = Mecanico(26, "Mecanico23", 22, "Francesa", "09-09-1995", 58000, 85)
    mecanico24 = Mecanico(27, "Mecanico24", 22, "Francesa", "09-09-1995", 58000, 85)
    # Directores de equipo
    director1 = DirectorEquipo(6, "Director1", 50, "Alemana", "06-06-1970", 100000)
    director2 = DirectorEquipo(7, "Director2", 48, "Alemana", "07-07-1972", 95000)
    director3 = DirectorEquipo(8, "Director3", 46, "Alemana", "08-08-1974", 90000)
    director4 = DirectorEquipo(9, "Director4", 44, "Alemana", "09-09-1976", 85000)
    director5 = DirectorEquipo(10, "Director5", 42, "Alemana", "10-10-1978", 80000)
    director6 = DirectorEquipo(11, "Director6", 40, "Alemana", "11-11-1980", 75000)
    director7 = DirectorEquipo(12, "Director7", 38, "Alemana", "12-12-1982", 70000)
    director8 = DirectorEquipo(13, "Director8", 36, "Alemana", "09-09-1995", 65000)
    director9 = DirectorEquipo(14, "Director9", 34, "Alemana", "09-09-1995", 60000)
    director10 = DirectorEquipo(15, "Director10", 32, "Alemana", "09-09-1995", 55000)
    
    # Limpiamos los puntajes de campeonato de los pilotos
    for piloto in [piloto1, piloto2, piloto3, piloto4, piloto5, piloto6, piloto7, piloto8, piloto9, piloto10]:
        piloto._puntaje_campeonato = 0
    

    equipo1.agregar_empleado(piloto1)
    equipo1.agregar_empleado(mecanico1)
    equipo1.agregar_empleado(director1)
    equipo1.agregar_empleado(mecanico11)
    equipo1.agregar_empleado(mecanico12)
    equipo1.agregar_empleado(mecanico13)
    equipo1.agregar_empleado(mecanico14)
    equipo1.agregar_empleado(mecanico15)
    equipo1.agregar_empleado(mecanico16)
    equipo1.agregar_empleado(mecanico17)
   
    equipo2.agregar_empleado(piloto2)
    equipo2.agregar_empleado(mecanico2)
    equipo2.agregar_empleado(director2)
    equipo2.agregar_empleado(mecanico18)
    equipo2.agregar_empleado(mecanico19)
    equipo2.agregar_empleado(mecanico20)
    equipo2.agregar_empleado(mecanico21)
    equipo2.agregar_empleado(mecanico22)
    equipo2.agregar_empleado(mecanico23)
    equipo2.agregar_empleado(mecanico24) 
    
    equipo3.agregar_empleado(piloto3)
    equipo3.agregar_empleado(mecanico3)
    equipo3.agregar_empleado(director3)
    
    equipo4.agregar_empleado(piloto4)
    equipo4.agregar_empleado(mecanico4)
    equipo4.agregar_empleado(director4)
    
    equipo5.agregar_empleado(piloto5)
    equipo5.agregar_empleado(mecanico5)
    equipo5.agregar_empleado(director5)
    
    equipo6.agregar_empleado(piloto6)
    equipo6.agregar_empleado(mecanico6)
    equipo6.agregar_empleado(director6)
    
    equipo7.agregar_empleado(piloto7)
    equipo7.agregar_empleado(mecanico7)
    equipo7.agregar_empleado(director7)
    
    equipo8.agregar_empleado(piloto8)
    equipo8.agregar_empleado(mecanico8)
    equipo8.agregar_empleado(director8)
    
    equipo9.agregar_empleado(piloto9)
    equipo9.agregar_empleado(mecanico9)
    equipo9.agregar_empleado(director9)
    
    equipo10.agregar_empleado(piloto10)
    equipo10.agregar_empleado(mecanico10)
    equipo10.agregar_empleado(director10)

    equipos.extend([equipo1, equipo2, equipo3, equipo4, equipo5, equipo6, equipo7, equipo8, equipo9, equipo10])

    #simulamos la carrera con datos anteriores
    simular_carrera(autos, equipos)
    
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
        print("7. Configurar prueba y simular")

        opcion = valida_opcion(1, 7)

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
        elif opcion == 7:
            configurar_prueba_y_simular(equipos, autos)


main()
