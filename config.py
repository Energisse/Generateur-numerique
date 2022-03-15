'''Config module contient la configuration du générateur numérique.'''

# includes
import datetime

# config
OUTPUT_FILE_NAME = "output/" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+".csv"