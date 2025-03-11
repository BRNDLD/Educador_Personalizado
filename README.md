# Educador Personalizado de IA

## Descripción
El **Educador Personalizado de IA** es un sistema de tutoría inteligente diseñado para adaptarse al nivel de conocimiento y estilo de aprendizaje del estudiante. Su función principal es proporcionar ejercicios de álgebra básica y ajustar dinámicamente la dificultad de los ejercicios según el desempeño del estudiante. Implementa una combinación de lógica declarativa con **pyDatalog** y un enfoque basado en aprendizaje por refuerzo y planificación heurística.

## Estructura del Código

### 1. Declaración de términos y hechos iniciales
El código define términos globales mediante `pyDatalog.create_terms`, lo que permite manipular estados dentro del sistema de reglas lógicas. Se inicializan hechos como:
- Nivel de conocimiento del estudiante (`Bajo` por defecto).
- Dificultad del subtema (`Basico`).
- Progreso (`0%` al inicio).
- Errores consecutivos (`0`).

### 2. Funciones de actualización de estado
- **`update_correcta(est, sub)`**: Incrementa el progreso del estudiante en 25% cada vez que responde correctamente, hasta un máximo de 100%. Reinicia el contador de errores y, si el progreso llega a 100%, aumenta la dificultad a `Intermedio`.
- **`update_incorrecta(est, sub)`**: Aumenta el contador de errores cuando el estudiante falla una respuesta. Si alcanza 3 errores consecutivos y la dificultad es `Intermedio`, reduce la dificultad a `Basico`.

### 3. Funciones auxiliares
- **`get_dificultad(sub)`**: Recupera la dificultad actual del subtema de forma segura.
- **`mostrar_estado(est, sub)`**: Imprime el estado actual del estudiante, incluyendo nivel de conocimiento, progreso, dificultad y errores consecutivos.

### 4. Simulación de interacciones
- **`simular_respuesta(est, sub, respuesta)`**: Llama a `update_correcta` o `update_incorrecta` según la respuesta dada por el estudiante.
- El código ejecuta una simulación donde:
  1. Se muestra el estado inicial.
  2. Se simulan tres respuestas incorrectas consecutivas.
  3. Se simulan cinco respuestas correctas consecutivas.

## Salidas Esperadas

1. **Estado inicial:**
   ```
   Estado actual del sistema:
   Nivel de conocimiento: Bajo
   Dificultad actual: Basico
   Progreso en el subtema: 0 %
   Errores consecutivos: 0
   ```

2. **Después de 3 respuestas incorrectas:**
   ```
   Simulación de respuestas incorrectas:
   Estado actual del sistema:
   Nivel de conocimiento: Bajo
   Dificultad actual: Basico
   Progreso en el subtema: 0 %
   Errores consecutivos: 3
   ```

3. **Después de 5 respuestas correctas:**
   ```
   Simulación de respuestas correctas:
   Estado actual del sistema:
   Nivel de conocimiento: Bajo
   Dificultad actual: Intermedio
   Progreso en el subtema: 100 %
   Errores consecutivos: 0
   ```

## Autor
**Brandold Vega Pérez**

_Universidad de Cartagena - Ingeniería de Sistemas y Computación_