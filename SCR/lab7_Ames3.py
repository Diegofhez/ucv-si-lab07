# CREAR UN GRÁFICO HISTOGRAMA
import numpy as np
import matplotlib.pyplot as plt

# Datos
a = [25, 55, 42, 41, 25, 22, 34, 42, 42, 102, 95, 85, 55, 110, 120, 70, 65, 55, 111, 115,
     80, 70, 55, 64, 44, 42, 40]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Aplicar configuración de características del gráfico
plt.hist(a, bins, histtype='bar', rwidth=0.8, color='blue')

# Definiendo el título y nombres de los ejes
plt.title('Histogramas')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

# Mostrar leyenda, cuadrícula y figura(gráfica)
plt.grid()
plt.show()
