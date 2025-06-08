import numpy as np
import matplotlib.pyplot as plt

def par_ing(f, A, fase):
    Ts = 0.05
    x = np.linspace(-1, 5, 1000)
    y = A * np.sin(2 * np.pi * f * x + fase)
    N = int((5 - (-1)) / Ts) + 1
    n = np.arange(N)
    t_n = -1 + n * Ts
    y_disc = A * np.sin(2 * np.pi * f* t_n + fase)
    x_ref = np.sin(2 * np.pi * 1 * x)

    plt.figure()
    plt.subplots_adjust(hspace=0.5)
    plt.subplot(2,1,1)
    plt.plot(x, y, 'b')
    plt.plot(x, x_ref, "g--", label="Referencia")
    plt.title(f"Señal senoidal: A={A}, f={f}Hz, ϕ={fase} rad")
    plt.grid(True)

    plt.subplot(2,1,2)
    plt.plot(x, y, 'b')
    plt.stem(t_n, y_disc,'r')
    plt.plot(x, x_ref, "g--",  label="Referencia")
    plt.grid(True)
    plt.show()
