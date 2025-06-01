import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square, sawtooth

# Definimos las frecuencias
f=2
t = np.linspace(-1,5,1000)

x1t = np.sin(2*np.pi*2*t)
u = np.heaviside(t, 1) 
x2t = np.exp(-2 * t) * u
x3t = sawtooth(2 * np.pi * f * t, width=0.5) 
x4t = square(2 * np.pi * f * t)

#Discretización (muestreo de las señales)
Ts= 0.01
n = np.arange(-100,500)
tn= n*Ts

x1tn = np.sin(2*np.pi*f*tn)
ut = np.heaviside(tn, 1)
x2tn = np.exp(-2 * tn) * ut
x3tn = sawtooth(2 * np.pi * f * tn, width=0.5) 
x4tn = square(2 * np.pi * f * tn)

#Graficamos las señales
plt.figure()
plt.subplots_adjust(hspace=0.5)

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
