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
    x.append(x[-1] + vx * dt)
    vx = vx + ax * dt
    y.append(y[-1] + vy * dt)
    vy += ay * dt
    t.append(t[-1] + dt)


plt.plot(x,y)
plt.title('Projectile motion diagram')
plt.xlabel('Horizonal Position')
plt.show()

print(x[-1])