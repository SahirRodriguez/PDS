import sys
import subprocess
from src.Activity_1 import continuous_sine, discrete_sine
from src.Activity_2 import understanding_freq
from src.Tarea2 import frec_ing

def main(options):
    if options[1] == "act_1":
        continuous_sine()
        discrete_sine()
    elif options[1] == "act_2":
        if len(args) > 2:
            understanding_freq(options[2])
    elif options[1] == "tarea1":
        subprocess.run(["python", "src/tarea1.py"])
    elif options[1] == "tarea2":
        if len(args) > 2:
            frec_ing(options[2])
    else:
        print("Please give a frequency. Example: python main.py act_2 2")


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Please give an argument")
        print("Example ( run Activity_1 ) : python main.py act_1")
        print("Example ( run Activity_2 ) : python main.py act_2 1")

        #Hola