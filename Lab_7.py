from numpy import sin,cos,pi
from matplotlib import pyplot as plt

plt.close('all')

# Constants
g = 9.80
π = pi

#launch parameters
v0 = 6.42
theta = 40 * pi/180 #--> radians
y0 = 0.970 #--> Meters

# Config
vx = v0 * cos(theta)
vy = v0 * sin(theta)

x = [0.0]
y = [y0]
t = [0.0]
dt = 0.001

#loop di loops
while y[-1] > 0:
    ax = 0
    ay =-g