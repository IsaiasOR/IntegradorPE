import pandas as pd
import matplotlib.pyplot as plt

# Nombre del archivo
dataset = pd.read_excel(r'D:\Isaías\Desktop\3er año - 2023\Probabilidad y Estadística\IntegradorPE\dataset_empleados_limpio.xlsx')

# Agrupar por lenguaje de programación y calcular el salario promedio
promedio_salario_por_lenguaje = dataset.groupby('Lenguajes_Programacion')['Salario'].mean()

# Crear el gráfico de barras
bars = plt.bar(promedio_salario_por_lenguaje.index, promedio_salario_por_lenguaje)

# Etiquetas y título
plt.xlabel('Lenguaje de Programación')
plt.ylabel('Salario Promedio')
plt.title('Salario Promedio por Combinación de lenguajes de programación')

# Rotar ejes
plt.xticks(rotation=45, ha='right', fontsize=8)

# Agregar etiquetas a barras
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom', size=6)

# Mostrar el gráfico
plt.show()