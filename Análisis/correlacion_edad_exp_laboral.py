import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Cargar el archivo
datos = pd.read_excel(r'D:\Isaías\Desktop\3er año - 2023\Probabilidad y Estadística\IntegradorPE\dataset_empleados_limpio.xlsx')

# Calcular la covarianza entre las dos variables
covarianza = np.cov(datos['Edad'], datos['Experiencia_Laboral'], ddof=0)[0][1]

# Calcular el coeficiente de correlación lineal (coeficiente de Pearson)
correlacion = np.corrcoef(datos['Edad'], datos['Experiencia_Laboral'])[0][1]

# Calcular el coeficiente de determinación (R cuadrado)
coef_determinacion = correlacion ** 2

# Crear el gráfico de dispersión
plt.figure(figsize=(8, 6))
plt.scatter(datos['Edad'], datos['Experiencia_Laboral'], color='blue')
plt.title('Gráfico de Dispersión: Edad vs Experiencia Laboral')
plt.xlabel('Edad (Años)')
plt.ylabel('Experiencia Laboral (Años)')
plt.grid(True)
plt.show()

print(f'Covarianza entre Experiencia Laboral y Edad: {covarianza}')
print(f'Coeficiente de Correlación Lineal (Pearson): {correlacion}')
print(f'Coeficiente de Determinación (R cuadrado): {coef_determinacion}')