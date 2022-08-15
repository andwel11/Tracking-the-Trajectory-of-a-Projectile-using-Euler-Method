"""

author: Angelica Uzo
course: Chemical Engineering
school: University of Birmingham

"""

# This code will model the trajectory of a projectile with no drag provided the initial position,
# initial speed and angle of inclination to the horizontal in degrees at an initial time, t0 
# in steps dt until final time, tf is reached
import numpy as np
import matplotlib.pyplot as plt
import seaborn; seaborn.set_style("whitegrid")

# Pre-defined parameters
# Initial position
rx0 = 0 #m
ry0 = 0 #m

# Initial speed and angle of inclination to the horizontal
v0 = 10 #m s^-1
theta = 45 #º

# Gravitational acceleration
g = 9.81 #m s^-2

# Initial time
t0 = 0 #s

# User-defined parameters
# Time step                                      
dt = 0.01 #s

# Final time
tf = 10 #s 

# t_current represents the time at the current position of the projectile
t_current = t0

# r_current is an array containing the current vertical and horizontal displacements of the projectile respectively 
r_current = np.array([ry0 , rx0])

# v_current is an array containing the current vertical and horizontal velocities of the projectile respectively
v_current = np.array([v0 * np.sin(np.radians(theta)) , v0 * np.cos(np.radians(theta))])

# position and time represent empty lists into which the r_current and t_current 
# values will be appended respectively
position = []
time = []

# This loop calculates r_current at t_current and appends it to the list 'position' until t_current
# is equal to tf after which, the loop is terminated. 
while t_current <= tf:
    # r_current[0] represents the vertical displacement, r_current[1] represents the horizontal displacement
    # v_current[0] represents the vertical velocity, v_current[1] represents the horizontal velocity
    v_new = np.array([v_current[0] - g * dt , v_current[1] + 0 * dt])
    r_new = np.array([r_current[0] + v_current[0] * dt , r_current[1] + v_current[1] * dt])
    # 'position.append(r_current)' modifies the list 'position' by adding r_current to the end of the list 
    # rx_and_ry represents an array of the entries within 'position'
    position.append(r_current)
    rx_and_ry = np.array(position)
    # r_new and v_new become the next timestep's r_current and v_current values
    v_current = v_new
    r_current = r_new
    # 'time.append(t_current)' modifies the list 'time' by adding t_current to the end of the list 
    # t represents an array of the entries within 'time'
    time.append(t_current)
    t = np.array(time)
    # This defines t_current at the new timestep and the loop repeats
    t_current = t_current + dt
    # To break the loop 
    if r_current[0] < 0:
        break

# Plots
# rx_and_ry[:,1] represents the horizontal displacement
# rx_and_ry[:,0] represents the vertical displacement
plt.scatter(rx_and_ry[:,1], rx_and_ry[:,0], c=t)
plt.title("Trajectory of the Projectile")
plt.xlabel("Horizontal displacement ($m$)")
plt.ylabel("Vertical displacement ($m$)")

plt.show()

# range represents the maximum horizontal distance the projectile travels
range = max(rx_and_ry[:,1])
# max_height represents the maximum vertical distance the projectile travels
max_height = max(rx_and_ry[:,0])
print ("Maximum height of Projectile =", round(max_height, 3),"m")
print ("Range of Projectile =", round(range, 3),"m")

