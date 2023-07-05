# Reference: https://www.johndcook.com/blog/2020/09/23/circles-to-circles/
# https://glowingpython.blogspot.com/2011/08/applying-moebius-transformation-to.html
# https://stackoverflow.com/questions/23439685/apply-complex-transformation-to-an-image-using-matplotlib-and-numpy
import numpy as np
from numpy import exp, pi, linspace
import matplotlib.pyplot as plt
import seaborn as sns

sns_colors = sns.color_palette("Set1", 10)

def circle(radius, center):
    theta = linspace(0, 2 * pi, 200)
    return center + radius * exp(1j * theta)

def plot_curves(curves, sing_pt=None, fname="a.jpg"):
    for i, c in enumerate(curves):
        plt.plot(c.real, c.imag, color=sns_colors[i], label=f"{i}")
        plt.scatter(c.real[0], c.imag[0], color=sns_colors[i], marker="^")
        # print(c.real[0], c.imag[0])
    if sing_pt is not None:
        plt.scatter(sing_pt.real, sing_pt.imag, color=sns_colors[i + 1], marker="s", label=f"Sing")
    plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
    plt.gca().set_aspect('equal')
    plt.savefig(fname)
    plt.clf()

def mobius(z, a, b, c, d):
    return (a * z + b)/(c * z + d)

# scale circles
circles = [circle(1, 0), circle(2, 0), circle(2, 6)]
plot_curves(circles, sing_pt=-4/3 + 0.0j, fname="circles.jpg")
# plot_curves([mobius(c, 2, 0, 0, 1) for c in circles], fname="circles-scaled.jpg")

# rotate by a degree in radian
R = 1
for _theta in range(0, 361, 45):
    __theta = np.radians(_theta)
    a = R * np.exp(eval(f"{__theta}j"))
    plot_curves([mobius(c, a, 0, 0, 1) for c in circles], fname=f"circles-rotate{_theta}.jpg")

# circle to circle
circles = [circle(1, 0), circle(2, 0), circle(2, 6)]
# plot_curves(circles, sing_pt=-4/3 + 0.0j, fname="circles.jpg")
plot_curves([mobius(c, 1, 2, 3, 4) for c in circles], fname="circles-transformed.jpg")

# line to line
line = linspace(-100, 100, 600)
curves = [line, 1j * line - 4/3]
plot_curves(curves, fname="lines.jpg")
plot_curves([mobius(c, 1, 2, 3, 4) for c in curves], fname="lines-transformed.jpg")

# line to circle
lines = [1j * line - 4, 1j * line + 4, line - 4j, line + 4j]
plot_curves(lines, fname="line-to-circle.jpg")
plot_curves([mobius(c, 1, 2, 3, 4) for c in lines], fname="line-to-circle-transformed.jpg")

# Face
dash = linspace(0.60, 0.90, 20)
smile = 0.3*exp(1j*2*pi*dash) - 0.2j
left_eye  = circle(0.1, -0.4+.2j)
right_eye = circle(0.1,  0.4+.2j)
face = [circle(1, 0), left_eye, smile, right_eye]
plot_curves(face, fname="face.jpg")
plot_curves([mobius(c, 1, 0, 1, -1 + 1j) for c in face], fname="face-transformed-1.jpg")
plot_curves([mobius(c, 1, 0, 3, 1) for c in face], fname="face-transformed-2.jpg")
plot_curves([mobius(c, 1, 0, 1, 0.4-0.2j) for c in face], fname="face-transformed-3.jpg")
