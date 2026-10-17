import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 1. Setup the figure and axis
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x, np.sin(x))

# Set fixed axis limits so the view doesn't jump around
ax.set_ylim(-1.5, 1.5)
ax.set_xlim(0, 2 * np.pi)
ax.set_title("Real-Time Changing Curve")
ax.grid(True)

# 2. Define the update function
def update(frame):
    # Update the y-data based on the current frame (time)
    # Here we add a phase shift to make it look like it's moving
    y_data = (np.sin(x + frame / 10.0) )
    line.set_ydata(y_data)
    return line,

# 3. Create the animation
# interval=50 means update every 50 milliseconds
ani = animation.FuncAnimation(fig, update, interval=50, blit=True)

plt.show()