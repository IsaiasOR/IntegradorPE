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

# Mostrar gráfico
plt.show()
