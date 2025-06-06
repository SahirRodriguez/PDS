
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from src.utils.grapher import continuous_plotter, discrete_plotter


def frec_ing(mod_frec):
# Señal seno continuo
    f = float(mod_frec)
    A = 1
    number_of_points = 1000
    t = np.linspace(0, 5, 200)
    xt = A * np.sin(2 * np.pi * f * t)

    continuous_plotter(t, xt,
    'Seno Continuo', 'Señal seno',
    'Tiempo [s]', 'Amplitud')

# Señal seno discreto
    fs = 20
    ts = 1 / fs
    samples = 100
    n = np.arange(samples)
    x_n = A * np.sin(2 * np.pi * f * n * ts )

    discrete_plotter(
    n, x_n,
    "Seno discreto", 'Señal seno',
    "Tiempo [n]", "Amplitud")