import numpy as np
from src.utils.grapher import continuous_plotter, discrete_plotter

def frec_ing(mod_frec):
    f = float(mod_frec)
    A = 1
    t = np.linspace(0, 5, 1000)
    xt = A * np.sin(2 * np.pi * f * t)
    continuous_plotter(t, xt,'Seno Continuo', 'Señal seno','Tiempo [s]', 'Amplitud')
    fs = 20 
    ts = 1 / fs
    n = np.arange(100)
    x_n = A * np.sin(2 * np.pi * f * n * ts )
    discrete_plotter(n, x_n,"Seno discreto", 'Señal seno',"Tiempo [n]", "Amplitud")