import matplotlib.pyplot as plt
import io
import base64
import numpy as np

# Función para generar gráfico de barras
def generar_grafico_barras(edad, salario):
    # Convertir edad y salario a arrays de numpy
    edad = np.array(edad)
    salario = np.array(salario)

    # Definir los rangos de edad
    rangos = [(0, 20), (20, 30), (30, 40), (40, 50), (50, 60), (60, 100)]
    
    # Inicializar listas para almacenar los datos agrupados
    salarios_promedio = []
    etiquetas_rangos = []

    # Agrupar los datos por rango de edad
    for rango_min, rango_max in rangos:
        # Filtrar las edades y salarios que caen en este rango
        mask = (edad >= rango_min) & (edad < rango_max)
        salarios_rango = salario[mask]
        
        if len(salarios_rango) > 0:
            salario_promedio = np.mean(salarios_rango)
            salarios_promedio.append(salario_promedio)
            etiquetas_rangos.append(f'{rango_min}-{rango_max}')

    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(etiquetas_rangos, salarios_promedio, color='blue')
    plt.xlabel('Rango de Edad')
    plt.ylabel('Salario Promedio')
    plt.title('Relación entre Rango de Edad y Salario Promedio')

    # Rotar las etiquetas del eje x para mejor legibilidad
    plt.xticks(rotation=45)

    # Convertir gráfico en imagen para enviar como respuesta
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plt.close()

    # Codificar la imagen en base64 para insertar en HTML
    return base64.b64encode(img.getvalue()).decode()


# Función para generar gráfico de pie
def generar_grafico_pie(ciudades, cantidad_personas):
    plt.figure(figsize=(8,8))
    plt.pie(cantidad_personas, labels=ciudades, autopct='%1.1f%%', startangle=90)
    plt.title('Distribución de Personas por Ciudad')
    plt.axis('equal')  # Para que el gráfico sea circular

    # Convertir gráfico en imagen para enviar como respuesta
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    # Codificar la imagen en base64 para insertar en HTML
    return base64.b64encode(img.getvalue()).decode()
