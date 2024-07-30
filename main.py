import pandas as pd
import numpy as np
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
from scalecast.Forecaster import Forecaster

df = pd.read_csv('AirPassengers.csv',parse_dates=['Month'])