import pandas as pd
import os

def load_data(folder):
    for filename in os.listdir(folder):
        print(filename)