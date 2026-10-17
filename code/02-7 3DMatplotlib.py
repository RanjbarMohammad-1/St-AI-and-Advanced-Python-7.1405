import matplotlib.pyplot as plt
import numpy as np

def main():



    # Create 3D axes
    ax = plt.axes(projection='3d')

    # Data for a three-dimensional line
    zline = np.linspace(0, 15, 1000)
    xline = np.sin(zline)
    yline = np.cos(zline)

    # Plot the 3D curve
    ax.plot3D(xline, yline, zline, color='gray', linewidth=2)

    # Data for three-dimensional scattered points
    zdata = 15 * np.random.random(100)
    xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
    ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
    plt.show()


if __name__=='__main__':
    main()