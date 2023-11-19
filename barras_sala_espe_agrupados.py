import pandas as pd
import matplotlib.pyplot as plt

# Nombre del archivo
dataset = pd.read_excel(r'D:\Isaías\Desktop\3er año - 2023\Probabilidad y Estadística\IntegradorPE\dataset_empleados_limpio.xlsx')

# Agrupar por especialización y calcular el salario promedio
promedio_salario_por_especializacion = dataset.groupby('Especializacion_Agrupados')['Salario'].mean()

# Crear el gráfico de barras
bars = plt.bar(promedio_salario_por_especializacion.index, promedio_salario_por_especializacion)

# Etiquetas y título
plt.xlabel('Especialización')
plt.ylabel('Salario Promedio')
plt.title('Salario Promedio por Especialización (2)')

# Rotar ejes
plt.xticks(rotation=45, ha='right', fontsize=9)

# Agregar etiquetas a barras
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom', size=10)

# Mostrar el gráfico
plt.show()