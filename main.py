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

def zplot(area=0.95, two_tailed=True, align_right=False):
    # Plots a z distribution with common annotations

    # Creating plotting area
    fig = plt.figure(figsize=(12, 6))
    ax = fig.subplots()

    # Creating the normal distribution
    norm = scs.norm()

    # Creating the data points to plot
    x = np.linspace(-5, 5, 1000)
    y = norm.pdf(x)

    ax.plot(x, y)

    # Filling in areas for two-tailed tests
    if two_tailed:
        left = norm.ppf(0.5 - area / 2)
        right = norm.ppf(0.5 + area / 2)
        ax.vlines(right, 0, norm.pdf(right), color='grey', linestyle='--')
        ax.vlines(left, 0, norm.pdf(left), color='grey', linestyle='--')

        ax.fill_between(x, 0, y, color='grey', alpha='0.25', where=(x > left) & (x < right))
        plt.xlabel('z')
        plt.ylabel('PDF')
        plt.text(left, norm.pdf(left), "z = {0:.3f}".format(left), fontsize=12, rotation=90, va="bottom", ha="right")
        plt.text(right, norm.pdf(right), "z = {0:.3f}".format(right), fontsize=12, rotation=90, va="bottom", ha="left")

    # Filling in areas for one-tailed tests
    else:
        # Aligning the area to the right
        if align_right:
            left = norm.ppf(1-area)
            ax.vlines(left, 0, norm.pdf(left), color='grey', linestyle='--')
            ax.fill_between(x, 0, y, color='grey', alpha='0.25', where=x > left)
            plt.text(left, norm.pdf(left), "z = {0:.3f}".format(left), fontsize=12, rotation=90, va="bottom", ha="right")

        # Aligning the area to the left
        else:
            right = norm.ppf(area)
            ax.vlines(right, 0, norm.pdf(right), color='grey', linestyle='--')
            ax.fill_between(x, 0, y, color='grey', alpha='0.25', where=x < right)
            plt.text(right, norm.pdf(right), "z = {0:.3f}".format(right), fontsize=12, rotation=90, va="bottom", ha="left")

    # Annotating the shaded area
    plt.text(0, 0.1, "shaded area = {0:.3f}".format(area), fontsize=12, ha='center')

    # Labeling the axis
    plt.xlabel('z')
    plt.ylabel('PDF')

    plt.show()

