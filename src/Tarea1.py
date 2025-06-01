import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Tarea 1: Graficado de señales continuas y discretas

# Definimos las frecuencias
f=2 # Frecuencia de 2 Hz
t = np.linspace(-1,5,1000) # Tiempo continuo de -1 a 5 segundos con 1000 puntos

# Definimos las señales continuas
x1t = np.sin(2*np.pi*2*t) # Sinusoide de 2 Hz
u = np.heaviside(t, 1) 
x2t = np.exp(-2 * t) * u # Escalon unitario 
x3t = signal.sawtooth(2 * np.pi * f * t, width=0.5) # Señal triangular de 2 Hz 
x4t = signal.square(2 * np.pi * f * t) # Señal cuadrada de 2Hz

#Discretización (muestreo de las señales)
Ts= 0.01 # Periodo de muestreo
n = np.arange(-100,500) # rango de muestras
tn= n*Ts  # conversión a tiempo muestreado

# Definimos las señales discretas
x1tn = np.sin(2*np.pi*f*tn) # Señal muestreada de sinusoide de 2 Hz
ut = np.heaviside(tn, 1)
x2tn = np.exp(-2 * tn) * ut # Escalon unitario muestreado
x3tn = signal.sawtooth(2 * np.pi * f * tn, width=0.5)  # Señal triangular muestreada de 2 Hz
x4tn = signal.square(2 * np.pi * f * tn)   # Señal cuadrada muestreada de 2Hz

#Graficamos las señales

plt.figure()
plt.subplots_adjust(hspace=0.5)

# Graficamos las señales continuas

plt.subplot(4,1,1)
plt.plot(t, x1t, "r")
plt.stem(tn, x1tn)
plt.title("Sinusoide de 2 Hz")
plt.grid()

plt.subplot(4,1,2)
plt.plot(t, x2t, "r")
plt.stem(tn, x2tn)
plt.title("Escalon unitario")
plt.grid()

# Graficamos las señales discretas

plt.subplot(4,1,3)
plt.plot(t, x3t, "r")
plt.stem(tn, x3tn)
plt.title("Señal triangular de 2 Hz")
plt.grid()

plt.subplot(4,1,4)
plt.plot(t, x4t, "r")
plt.stem(tn, x4tn)
plt.title("Señal cuadrada de 2Hz")
plt.grid()

plt.show()
