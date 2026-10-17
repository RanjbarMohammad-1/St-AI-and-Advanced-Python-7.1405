
import matplotlib.pyplot as plt
import numpy as np

def f(x, y):  return np.sin(np.sqrt(x ** 2 + y ** 2))
def main():
    # Create x and y coordinates
    x = np.linspace(-6, 6, 30)
    y = np.linspace(-6, 6, 30)

    # Create a grid of coordinates
    X, Y = np.meshgrid(x, y)

    # Calculate z values
    Z = f(X, Y)

    # Create a figure and 3D axes
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Set the viewing angle
    ax.view_init(elev=60, azim=35)

    # Draw the 3D surface
    ax.plot_surface(X, Y, Z, cmap='viridis')

    # Add axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    # Display the plot
    plt.show()


if __name__ == '__main__':
    main()
