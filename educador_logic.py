from pyDatalog import pyDatalog

# Declarar los términos globales necesarios
pyDatalog.create_terms('nivel_conocimiento, dificultad_actual, progreso_subtema, errores_consecutivos')
pyDatalog.create_terms('estudiante, subtema, p, n, X')

# Hechos iniciales
+ nivel_conocimiento('e1', 'Bajo')
+ dificultad_actual('s1', 'Basico')
+ progreso_subtema('e1', 's1', 0)
+ errores_consecutivos('e1', 's1', 0)

# Función auxiliar para obtener la dificultad del subtema de forma segura
def get_dificultad(sub):
    res = dificultad_actual(sub, X)
    if res.data and len(res.data[0]) >= 2:
        return res.data[0][1]
    return 'Desconocido'

# Función para actualizar el estado ante una respuesta correcta
def update_correcta(est, sub):
    # Consultar el progreso actual
    res = progreso_subtema(est, sub, p)
    current_progress = res.data[0][2] if res.data else 0
    new_progress = current_progress + 25
    if new_progress > 100:
        new_progress = 100

    # Actualizar el progreso: retirar el hecho antiguo y agregar el nuevo
    pyDatalog.retract_fact("progreso_subtema", est, sub, current_progress)
    + progreso_subtema(est, sub, new_progress)

    # Reiniciar el contador de errores
    res_err = errores_consecutivos(est, sub, n)
    current_err = res_err.data[0][2] if res_err.data else 0
    pyDatalog.retract_fact("errores_consecutivos", est, sub, current_err)
    + errores_consecutivos(est, sub, 0)

    # Si el progreso alcanza 100, actualizar la dificultad a 'Intermedio'
    if new_progress == 100:
        diff_val = get_dificultad(sub)
        if diff_val == 'Basico':
            pyDatalog.retract_fact("dificultad_actual", sub, "Basico")
            + dificultad_actual(sub, "Intermedio")

# Función para actualizar el estado ante una respuesta incorrecta
def update_incorrecta(est, sub):
    # Consultar el contador actual de errores
    res_err = errores_consecutivos(est, sub, n)
    current_err = res_err.data[0][2] if res_err.data else 0
    new_err = current_err + 1
    if new_err > 3:
        new_err = 3  # Limitar a 3 errores consecutivos

    pyDatalog.retract_fact("errores_consecutivos", est, sub, current_err)
    + errores_consecutivos(est, sub, new_err)

    # Si se acumulan 3 errores y la dificultad es 'Intermedio', reducirla a 'Basico'
    diff_val = get_dificultad(sub)
    if new_err == 3 and diff_val == 'Intermedio':
        pyDatalog.retract_fact("dificultad_actual", sub, "Intermedio")
        + dificultad_actual(sub, "Basico")

# Función para simular la respuesta del estudiante
def simular_respuesta(est, sub, respuesta):
    if respuesta == 'correcta':
        update_correcta(est, sub)
    elif respuesta == 'incorrecta':
        update_incorrecta(est, sub)
    else:
        print("Respuesta no válida. Use 'correcta' o 'incorrecta'.")

# Función para mostrar el estado actual del sistema
def mostrar_estado(est, sub):
    # Consultar el progreso y los errores; cada consulta devuelve una lista de tuplas (est, sub, valor)
    res_prog = progreso_subtema(est, sub, p)
    res_err = errores_consecutivos(est, sub, n)
    prog_val = res_prog.data[0][2] if res_prog.data else 0
    err_val = res_err.data[0][2] if res_err.data else 0

    diff_val = get_dificultad(sub)

    print("\nEstado actual del sistema:")
    print("Nivel de conocimiento: Bajo")
    print("Dificultad actual:", diff_val)
    print("Progreso en el subtema:", prog_val, "%")
    print("Errores consecutivos:", err_val)

# Simulación de la interacción
if __name__ == "__main__":
    estudiante_id = 'e1'
    subtema_id = 's1'
    
    # Estado inicial
    mostrar_estado(estudiante_id, subtema_id)
    
    # Simulación de respuestas incorrectas: se simulan 3 respuestas incorrectas
    print("\nSimulación de respuestas incorrectas:")
    simular_respuesta(estudiante_id, subtema_id, 'incorrecta')
    simular_respuesta(estudiante_id, subtema_id, 'incorrecta')
    simular_respuesta(estudiante_id, subtema_id, 'incorrecta')
    mostrar_estado(estudiante_id, subtema_id)
    
    # Simulación de respuestas correctas: se simulan 5 respuestas correctas consecutivas
    print("\nSimulación de respuestas correctas:")
    simular_respuesta(estudiante_id, subtema_id, 'correcta')
    simular_respuesta(estudiante_id, subtema_id, 'correcta')
    simular_respuesta(estudiante_id, subtema_id, 'correcta')
    simular_respuesta(estudiante_id, subtema_id, 'correcta')
    simular_respuesta(estudiante_id, subtema_id, 'correcta')
    mostrar_estado(estudiante_id, subtema_id)

