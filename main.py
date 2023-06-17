# Importing necessary modules
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs

def z_val(sig_level=0.05, two_tailed=True):
    # Returns the z-score for a given significance level
    z_dist = scs.norm()
    if two_tailed:
        sig_level = sig_level/2
        area = 1 - sig_level
    else:
        area = 1 - sig_level

    z = z_dist.ppf(area)

    return z

