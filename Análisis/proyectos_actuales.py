import pandas as pd

# Trae el archivo
dataset = pd.read_excel(r'D:\Isaías\Desktop\3er año - 2023\Probabilidad y Estadística\IntegradorPE\dataset_empleados_limpio.xlsx')

# Calcular la tabla de frecuencias usando value_counts()
frecuencias = dataset['Proyectos_Actuales'].value_counts().reset_index()
frecuencias.columns = ['Proyecto Actual', '| Frecuencia']

# Mostrar la tabla de frecuencias
print("\n"*3)

print("Tabla de Frecuencias de los proyectos actuales:")
print()
print(frecuencias.to_string(index=False))

print("\n"*3)