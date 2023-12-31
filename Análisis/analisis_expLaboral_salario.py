import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

# Paso 1: Cargar el archivo
dataset = pd.read_excel(r'D:\Isaías\Desktop\3er año - 2023\Probabilidad y Estadística\IntegradorPE\dataset_empleados_limpio.xlsx')

# Paso 3: Calcular estadísticas descriptivas comunes
estadisticas = dataset.describe()

print("\n"*3)
print(estadisticas)
print('')

estadisticas_exp_laboral = dataset['Experiencia_Laboral'].describe()

plt.boxplot(dataset['Experiencia_Laboral'])
plt.title('Boxplot de Años de experiencia')
plt.ylabel('Experiencia laboral')

# Mostrar datos estadísticos en el gráfico
# plt.text(1, estadisticas_exp_laboral['25%'], f"Q1: {estadisticas_exp_laboral['25%']}")
# plt.text(1, estadisticas_exp_laboral['50%'], f"Q2 (Mediana): {estadisticas_exp_laboral['50%']}")
# plt.text(1, estadisticas_exp_laboral['75%'], f"Q3: {estadisticas_exp_laboral['75%']}")
# plt.text(1, estadisticas_exp_laboral['min'], f"Mínimo: {estadisticas_exp_laboral['min']}")
# plt.text(1, estadisticas_exp_laboral['max'], f"Máximo: {estadisticas_exp_laboral['max']}")
plt.show()

# Paso 4: Hacer un diagrama de dispersión
plt.scatter(dataset['Experiencia_Laboral'], dataset['Salario'])
plt.xlabel('Años de Experiencia')
plt.ylabel('Salario (en dólares)')
plt.title('Diagrama de Dispersión: Años de Experiencia vs. Salario')
plt.show()

# Paso 5: Hacer una regresión lineal entrenando el modelo con un 20% de prueba
X = dataset[['Experiencia_Laboral']]
y = dataset['Salario']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Paso 6: Graficar la recta de regresión en el diagrama de dispersión
plt.scatter(dataset['Experiencia_Laboral'], dataset['Salario'])
plt.xlabel('Años de Experiencia')
plt.ylabel('Salario (en dólares)')
plt.title('Diagrama de Dispersión con Regresión Lineal')
plt.plot(X, model.predict(X), color='red')
plt.show()

# Paso 7: Calcular el coeficiente de determinación (R-squared)
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
print(f'Coeficiente de Determinación (R-squared): {r2}')

# Paso 8: Calcular los coeficientes del modelo
coeficiente_pendiente = model.coef_[0]
ordenada_al_origen = model.intercept_

print(f'Coeficiente de Pendiente: {coeficiente_pendiente}')
print(f'Ordenada al Origen: {ordenada_al_origen}')
print(f"La fórmula de la regresión lineal es: y = {coeficiente_pendiente}x + {ordenada_al_origen}")
print("\n"*3)

# # Hacer una predicción para 8 años de experiencia
# años_experiencia_nuevo = 8
# prediccion_salario = model.predict(np.array([[años_experiencia_nuevo]]))
# print(f'Predicción de Salario para {años_experiencia_nuevo} años de experiencia: {prediccion_salario[0]} dólares')