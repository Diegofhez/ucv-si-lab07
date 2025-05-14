# CREAR UN GRÁFICO LINEAL 02
import numpy as np
import matplotlib.pyplot as plt

# Definir datos
x1 = [1, 3, 5, 6, 7]
y1 = [5, 6, 7, 8, 7]
x2 = [2, 4, 6, 8]
y2 = [2, 3, 4, 3]

# Aplicar configuración de características del gráfico
plt.bar(x1, y1, label='línea 1', linewidth=4, color='blue')
plt.bar(x2, y2, label='línea 2', linewidth=4, color='green')

# Definiendo el título y nombres de los ejes
plt.title('Diagrama de Barras')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

# Mostrar leyenda, cuadrícula y figura(gráfica)
plt.legend()
plt.grid()
plt.show()





