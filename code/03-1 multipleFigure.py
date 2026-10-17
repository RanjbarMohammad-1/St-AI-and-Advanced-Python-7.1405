# importing required modules 
import matplotlib.pyplot as plt 
import numpy as np 

def main(): 
    # Figure 1
    plt.figure("Window 1")
    plt.plot([1, 2, 3], [10, 20, 30])
    plt.title("First Chart")
    plt.show(block=False)

    # Figure 2
    plt.figure("Window 2")
    plt.plot([1, 2, 3], [30, 20, 10])
    plt.title("Second Chart")
    plt.show(block=False)

    # Figure 3
    plt.figure("Window 3")
    plt.plot([1, 2, 3], [5, 15, 25])
    plt.title("Third Chart")
    plt.show(block=False)

    # Figure 4
    plt.figure("Window 4")
    plt.plot([1, 2, 3], [25, 15, 5])
    plt.title("Fourth Chart")
    plt.show()



if __name__=='__main__':
    main()