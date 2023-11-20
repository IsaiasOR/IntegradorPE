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

# Calcular los parámetros de la regresión lineal (pendiente e intercepto)
pendiente, intercepto = np.polyfit(datos['Edad'], datos['Experiencia_Laboral'], 1)

# Crear el gráfico de dispersión con la recta de regresión
plt.figure(figsize=(8, 6))
plt.scatter(datos['Edad'], datos['Experiencia_Laboral'], color='blue', label='Datos')
plt.plot(datos['Edad'], pendiente * datos['Edad'] + intercepto, color='red', label='Recta de Regresión')
plt.title('Gráfico de Dispersión: Edad vs Experiencia Laboral')
plt.xlabel('Edad (Años)')
plt.ylabel('Experiencia Laboral (Años)')
plt.legend()
plt.grid(True)
plt.show()

# Mostrar la información de correlación y recta de regresión
print(f'Covarianza entre Experiencia Laboral y Edad: {covarianza}')
print(f'Coeficiente de Correlación Lineal (Pearson): {correlacion}')
print(f'Coeficiente de Determinación (R cuadrado): {coef_determinacion}')
print(f'La ecuación de la recta de regresión es: Experiencia Laboral = {pendiente:.4f} * Edad + {intercepto:.4f}')