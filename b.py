# Reference: https://www.johndcook.com/blog/2020/09/23/circles-to-circles/
# https://glowingpython.blogspot.com/2011/08/applying-moebius-transformation-to.html
# https://stackoverflow.com/questions/23439685/apply-complex-transformation-to-an-image-using-matplotlib-and-numpy

# https://math.stackexchange.com/questions/4730679/decompose-a-mobius-transformation-to-understand-what-it-does?noredirect=1#comment10027691_4730679
import numpy as np
from numpy import exp, pi, linspace
import matplotlib.pyplot as plt
import seaborn as sns
import os

if not os.path.exists("./images"):
    os.makedirs("./images")

sns_colors = sns.color_palette("Set1", 10)

def circle(radius, center):
    theta = linspace(0, 2 * pi, 200)
    return center + radius * exp(1j * theta)

def plot_curves(before_curves, after_curves, sing_pt=None, fname="./images/a.jpg", before_asp=True, after_asp=True):
    plt.subplot(121)
    # fig = plt.figure(figsize=(15, 15))
    for i, c in enumerate(before_curves):
        plt.plot(c.real, c.imag, color=sns_colors[i], label=f"{i}")
        plt.scatter(c.real[0], c.imag[0], color=sns_colors[i], marker="^")
    if sing_pt is not None:
        plt.scatter(sing_pt.real, sing_pt.imag, color=sns_colors[i + 1], marker="s", label=f"Sing")
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=5, fancybox=True, shadow=True)
    plt.title("Before transform")
    if before_asp: plt.gca().set_aspect('equal')

    plt.subplot(122)
    for i, c in enumerate(after_curves):
        plt.plot(c.real, c.imag, color=sns_colors[i], label=f"{i}")
        plt.scatter(c.real[0], c.imag[0], color=sns_colors[i], marker="^")
    # plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
    # plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
    # plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=5, fancybox=True, shadow=True)
    plt.title("After transform")
    if after_asp: plt.gca().set_aspect('equal')
    plt.savefig(fname)
    plt.clf()

def mobius(z, a, b, c, d):
    return (a * z + b)/(c * z + d)

# # scale circles
circles = [circle(1, 0), circle(2, 0), circle(2, 6)]
# plot_curves(before_curves=circles, after_curves=[mobius(c, 2, 0, 0, 1) for c in circles], fname="./images/circles-scaled.jpg")

# # rotate by a degree in radian
# # Ref: Example 3.6 of http://www.warwickmaths.com/wp-content/uploads/2020/07/80_-M%C3%B6bius-Transformations.pdf
# R = 1
# for _theta in range(0, 361, 90):
#     __theta = np.radians(_theta)
#     a = R * np.exp(eval(f"{__theta}j"))
#     plot_curves(before_curves=circles, after_curves=[mobius(c, a, 0, 0, 1) for c in circles], fname=f"./images/circles-rotate{_theta}.jpg")

# # Inversion of circles
# plot_curves(before_curves=circles, after_curves=[mobius(c, 0, 1, 1, 0) for c in circles], sing_pt=0.0, fname="./images/circles-inv.jpg")

# # circle to circle
# plot_curves(before_curves=circles, after_curves=[mobius(c, 1, 2, 3, 4) for c in circles], sing_pt=-4/3 + 0.0j, fname="./images/circles-transformed.jpg")

# # line to line
# line = linspace(-20, 20, 600)
# curves = [1j * line - 4/3, 1j * line + 4/3, 1j * line - 2]
# plot_curves(before_curves=curves, after_curves=[mobius(c, 1, 2, 3, 4) for c in curves], sing_pt=-4/3 + 0.0j, fname="./images/line2line.jpg")
# plot_curves(before_curves=curves, after_curves=[mobius(c, 0, 1, 1, 0) for c in curves], sing_pt=0.0, fname="./images/line-inv.jpg")

# # line to circle
# lines = [1j * line - 4, 1j * line + 4, line - 4j, line + 4j]
# plot_curves(before_curves=lines, after_curves=[mobius(c, 1, 2, 3, 4) for c in lines], sing_pt=-4/3 + 0.0j, fname="./images/line2circle.jpg")

# # Face
# dash = linspace(0.60, 0.90, 20)
# smile = 0.3*exp(1j*2*pi*dash) - 0.2j
# left_eye  = circle(0.1, -0.4+.2j)
# right_eye = circle(0.1,  0.4+.2j)
# face = [circle(1, 0), left_eye, smile, right_eye]
# plot_curves(before_curves=face, after_curves=[mobius(c, 1, 2, 3, 4) for c in face], sing_pt=-4/3 + 0.0j, fname="./images/face-transformed.jpg")


# ====== line to line
# line = linspace(-20, 20, 600)
# curves = [1j * line - 4/3, 1j * line + 4/3, 1j * line - 2]
# Circular
plot_curves(before_curves=circles, after_curves=[mobius(c, 1j, 0, 0, -1j) for c in circles], fname="./images/circular.jpg")

# Elliptic: Just rotation
a = np.exp(np.deg2rad(90)*(1j)/2)
d = np.exp(- np.deg2rad(90)*(1j)/2 )
plot_curves(before_curves=circles, after_curves=[mobius(c, a, 0, 0, d) for c in circles], fname="./images/elliptic.jpg")

# Parabolic
plot_curves(before_curves=circles, after_curves=[mobius(c, 1, 2, 0, 1) for c in circles], fname="./images/parabolic.jpg")

# Hyperbolic
a = 2
plot_curves(before_curves=circles, after_curves=[mobius(c, a, 0, 0, a^(-1)) for c in circles], fname="./images/hyperbolic.jpg")