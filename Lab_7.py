import numpy as np
from matplotlib import pyplot as plt

plt.close('all')

# Constants
g = 9.80
π = np.pi

# Nominal launch parameters
v0_nominal = 3.78  # m/s
theta_nominal = 45 * π / 180  # radians
y0_nominal = 1.035  # meters

# Uncertainty parameters (standard deviations)
v0_uncertainty = 0.1  # m/s
theta_uncertainty = 1 * π / 180  # radians
y0_uncertainty = 0.01  # meters

# Simulation parameters
num_simulations = 500
dt = 0.001

# Arrays to store the results
final_x = []

for _ in range(num_simulations):
    # Generate random values with uncertainties
    v0 = np.random.normal(v0_nominal, v0_uncertainty)
    theta = np.random.normal(theta_nominal, theta_uncertainty)
    y0 = np.random.normal(y0_nominal, y0_uncertainty)
    
    # Calculate initial velocity components
    vx = v0 * np.cos(theta)
    vy = v0 * np.sin(theta)
    
    # Initialize lists for positions and time
    x = [0.0]
    y = [y0]
    t = [0.0]
    
    # Loop to compute the projectile's trajectory
    while y[-1] > 0:
        ax = 0
        ay = -g
        x.append(x[-1] + vx * dt)
        vx = vx + ax * dt
        y.append(y[-1] + vy * dt)
        vy += ay * dt
        t.append(t[-1] + dt)
    
    # Store the final horizontal position
    final_x.append(x[-1])

# Calculate mean and standard deviation of the results
mean_x = np.mean(final_x)
std_x = np.std(final_x)

# Plot a sample trajectory (optional)
plt.plot(x, y)
plt.title('Projectile Motion Diagram (Sample Trajectory)')
plt.xlabel('Horizontal Position (m)')
plt.ylabel('Vertical Position (m)')
plt.show()

# Output the statistics
print(f"Nominal final horizontal position: {x[-1]:.2f} m")
print(f"Mean final horizontal position: {mean_x:.2f} m")
print(f"Standard deviation of final horizontal position: {std_x:.2f} m")
