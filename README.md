#  Simulador de Carreras de Agustin Roque y Germán Martirena. (Obligatorio 2023 s2)
Proyeto de programación Agustin Roque (Universidad de Montevideo) equipo: Agustin Roque, Germán Martirena

Este es un simulador de carreras desarrollado en Python. El simulador incluye la simulación de equipos de carreras, empleados (pilotos, mecánicos y directores de equipo), autos y carreras. A continuación, se presentan las principales características y funcionalidades del código:

Clases Principales

El código incluye las siguientes clases principales:

Empleado: Representa a un empleado de un equipo de carreras, con atributos como ID, nombre, edad, nacionalidad, fecha de nacimiento, salario y puntaje.
Piloto: Una subclase de Empleado, representa a un piloto con atributos adicionales como número de auto, puntaje de campeonato y estado de lesiones.
Mecanico: Una subclase de Empleado, representa a un mecánico del equipo.
DirectorEquipo: Una subclase de Empleado, representa al director del equipo.
Auto: Representa un automóvil de carrera con atributos como modelo, puntaje y color.
Imprevisto: Representa eventos inesperados que pueden ocurrir durante una carrera, como lesiones, abandonos, errores en pits y penalidades.
Equipo: Representa un equipo de carreras con atributos como nombre, país de origen y año de creación.

Funcionalidades Principales:

Alta de empleados: Permite agregar pilotos, mecánicos y directores de equipo a los equipos de carreras existentes o crear nuevos equipos.
Alta de autos: Permite crear y agregar autos de carrera al simulador, especificando modelo, puntaje y color.
Alta de equipos: Permite crear y agregar equipos de carreras al simulador, proporcionando nombre, país de origen y año de creación.
Simulación de carrera: Simula una carrera, teniendo en cuenta los empleados, autos y eventos inesperados como lesiones, abandonos, errores en pits y penalidades. Luego, muestra los resultados de la carrera y actualiza los puntajes de los pilotos.
Realización de consultas: Ofrece la capacidad de realizar consultas sobre los datos almacenados en el simulador, como obtener el top 10 de pilotos con más puntos en el campeonato, resumen del campeonato de constructores, top 5 de pilotos mejor pagados, top 3 de pilotos más habilidosos y lista de directores de equipo.
Configuración de prueba y simulación: Permite configurar una prueba inicial con datos predefinidos y luego simular una carrera utilizando estos datos.

Uso del Código
Para usar el simulador de carreras, siga las instrucciones que aparecen en el menú principal. Puede agregar empleados, autos y equipos, simular carreras y realizar consultas sobre los datos almacenados.
