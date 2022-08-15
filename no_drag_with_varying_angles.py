"""

author: Angelica Uzo
course: Chemical Engineering
school: University of Birmingham

"""

# This code will model the trajectory of a projectile with no drag starting from the ground, with an initial speed 
# of 10m s^-1 at 30 and 60 degrees from the horizontal at initial time, t0 in steps dt until final time, tf is reached
import numpy as np
import matplotlib.pyplot as plt
import seaborn; seaborn.set_style("whitegrid")

# Pre-defined parameters
# Initial position
ry0 = 0 #m
rx0 = 0 #m

# Initial speed and angle of inclination to the horizontal
v0 = 10 #m s^-1
# To obtain 30 degrees trajectory, change theta to 30
theta = 60 #in degrees

# Gravitational acceleration
g = 9.81 #m s^-2

# Initial time
t0 = 0 #s

# User-defined parameters
# Time step                                      
dt = 0.001 #s

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

# Euler's Method
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
    # The 'if' condition breaks the loop when r_current[0] is negative, restricting the vertical 
    # displacement to values >= 0 
    if r_current[0] < 0:
        break

# Analytical Method
# This function will calculate the analytical rx values at analytical_time 
def analytical_rx(analytical_time):
    analytical_vx = v0 * np.cos(np.radians(theta)) 
    analyt_rx = analytical_vx * (analytical_time-t0) + rx0
    return analyt_rx
ana_rx = analytical_rx(t)

# This function will calculate the analytical ry values at analytical_time 
def analytical_ry(analytical_time):
    analytical_vy = v0 * np.sin(np.radians(theta)) 
    analyt_ry = analytical_vy * (analytical_time-t0) - g * ((analytical_time**2)/2 - (t0**2)/2)+ ry0
    return analyt_ry
ana_ry = analytical_ry(t)

# Plotting the graphs
# rx_and_ry[:,1] represents the Euler's horizontal displacement
# rx_and_ry[:,0] represents the Euler's vertical displacement
plt.scatter(rx_and_ry[:,1], rx_and_ry[:,0], c=t, label='Euler Projectile Position')
# A line graph is produced for the analytical data
plt.plot(ana_rx, ana_ry, label='Analytical Projectile Position')
plt.title("Trajectory of the Projectile")
plt.xlabel("Horizontal displacement ($m$)")
plt.ylabel("Vertical displacement ($m$)")
plt.legend()

plt.show()

# Range represents the maximum horizontal distance the projectile travels
# Maximum height represents the maximum vertical distance the projectile travels
# Euler's range is detemined by finding the maximum value in rx_and_ry[:,1]
# Euler's maximum height is detemined by finding the maximum value in rx_and_ry[:,0]
range = max(rx_and_ry[:,1])
max_height = max(rx_and_ry[:,0])
print ("Euler's Maximum Height of Projectile =", round(max_height, 3),"m")
print ("Euler's Range of Projectile =", round(range, 3),"m")

# Calculating the analytical maximum height and range
analytic_range = (v0**2 * np.sin(np.radians(2*theta)))/g 
analytic_max_height = (v0**2 * (np.sin(np.radians(theta)))**2)/(2 * g) 
print ("Analytical Maximum Height of Projectile =", round(analytic_max_height, 3),"m")
print ("Analytical Range of Projectile =", round(analytic_range, 3),"m")

# Calculating the percentage difference between the analytical and Euler's range and 
# maximum height respectively
percent_diff_max_height = (max_height - analytic_max_height)/analytic_max_height * 100
percent_diff_range = (range - analytic_range)/range * 100
print ("Percentage difference for Maximum Height of Projectile =", round(percent_diff_max_height, 3),"%")
print ("Percentage difference for Range of Projectile =", round(percent_diff_range, 3),"%")
