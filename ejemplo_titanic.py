import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv("titanic.csv")

# ---------------------------------------
# MODIFICACIÓN: de (1,2) a (1,3) + ancho 15
# ---------------------------------------
fig, ax = plt.subplots(1, 3, figsize=(15, 3))

# ---------------------------------------
# Gráfico 1: Histograma de edades
# ---------------------------------------
div = 10   # número de divisiones para los bins

ax[0].hist(df["Age"], bins=div)
ax[0].set_xlabel("Edad")
ax[0].set_ylabel("Frecuencia")
ax[0].set_title("Histograma de edades")

# ---------------------------------------
# Gráfico 2: Total hombres y mujeres
# ---------------------------------------
df_male = df[df["Sex"] == "male"]
df_female = df[df["Sex"] == "female"]

cant_male = len(df_male)
cant_female = len(df_female)

ax[1].bar(["Masculino", "Femenino"], [cant_male, cant_female], color="red")
ax[1].set_xlabel("Sexo")
ax[1].set_ylabel("Cantidad")
ax[1].set_title("Distribución de hombres y mujeres")

# ---------------------------------------
# Gráfico 3: Sobrevivientes agrupados por sexo
# ---------------------------------------
sob_male = len(df[(df["Sex"] == "male") & (df["Survived"] == 1)])
sob_female = len(df[(df["Sex"] == "female") & (df["Survived"] == 1)])

ax[2].bar(["Masculino", "Femenino"], [sob_male, sob_female], color="navy")
ax[2].set_xlabel("Sexo")
ax[2].set_ylabel("Cantidad Sobrevivientes")
ax[2].set_title("Sobrevivientes por Sexo")

# Mostrar gráfico
st.pyplot(fig)

# ---------------------------------------
# Mostrar tabla
# ---------------------------------------
st.write("## Muestra de datos cargados")
st.table(df.head())
