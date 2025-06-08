import sys
import subprocess
from src.Activity_1 import continuous_sine, discrete_sine
from src.Activity_2 import understanding_freq
from src.Tarea2 import frec_ing
from src.Tarea3 import par_ing
from src.Tarea4 import dac_analisis 

def main(options):
    if len(options) < 2:
        print("Uso: python main.py [act_1 | act_2 | tarea1 | tarea2 | tarea3] [parametros...]")
        return

    if options[1] == "act_1":
        continuous_sine()
        discrete_sine()

    elif options[1] == "act_2":
        understanding_freq(options[2])

    elif options[1] == "tarea1":
        subprocess.run(["python", "src/tarea1.py"])

    elif options[1] == "tarea2":
        frec_ing(options[2])

    elif options[1] == "tarea3":
        par_ing(float(options[2]), float(options[3]), float(options[4])) 

    elif options[1] == "tarea4":
        dac_analisis(options[2])
    else:
        print("Opción no reconocida. Usa: act_1, act_2, tarea1, tarea2, tarea3")

if __name__ == '__main__':
    main(sys.argv)