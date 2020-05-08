import numpy as np
from scipy.integrate import odeint

from model.set_model import *


class Simulation(object):
    """
    This is where you define the simulations you want to run. In this file you 
    can define different conditions for each simulation 
    (for example, ligand concentration) and how you would like each variable to 
    be simulated (i.e. do you want absolute concentration to be simulated? or 
    percentage change over time? Etc).
    """
