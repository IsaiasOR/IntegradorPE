import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo
dataset = pd.read_excel(r'D:\Isaías\Desktop\3er año - 2023\Probabilidad y Estadística\IntegradorPE\dataset_empleados_limpio.xlsx')

# Obtener estadísticas descriptivas del salario
estadisticas = dataset['Salario'].describe()
print(estadisticas)

# Revisar valores atípicos del salario con un boxplot
plt.boxplot(dataset['Salario'])
plt.title('Boxplot del Salario')
plt.ylabel('Salario')

# Mostrar datos estadísticos en el gráfico
plt.text(1, estadisticas['25%'], f"Q1: {estadisticas['25%']}")
plt.text(1, estadisticas['50%'], f"Q2 (Mediana): {estadisticas['50%']}")
plt.text(1, estadisticas['75%'], f"Q3: {estadisticas['75%']}")
plt.text(1, estadisticas['min'], f"Mínimo: {estadisticas['min']}")
plt.text(1, estadisticas['max'], f"Máximo: {estadisticas['max']}")

# Mostrar gráfico
plt.show()
