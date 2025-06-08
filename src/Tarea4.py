import numpy as np
import matplotlib.pyplot as plt

def dac_analisis(bits):
    VFS = 5.0  
    N = int(bits)
    niveles = 2 ** N
    paso = VFS / (niveles - 1)
    resolucion = (paso / VFS) * 100 

    print(f"DAC de {N} bits")
    print(f"Número de niveles: {niveles}")
    print(f"Tamaño del paso: {paso:.5f} V")
    print(f"Resolución porcentual: {resolucion:.5f}%")

    entradas = np.arange(niveles)
    salidas = entradas * paso

    plt.figure()
    plt.step(entradas, salidas, where='post', label=f"DAC {N} bits")
    plt.xlabel("Entrada digital")
    plt.ylabel("Salida analógica (V)")
    plt.title(f"Salida de DAC con {N} bits (VFS = {VFS}V)")
    plt.grid(True)
    plt.legend()
    plt.show()

