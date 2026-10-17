# importing the required modules 
import matplotlib.pyplot as plt 
import numpy as np 



def main():

    # Set the window title
    fig = plt.figure()
    fig.canvas.manager.set_window_title("AI class")
    # setting the x - coordinates 
    x = np.arange(0, 2*(np.pi), 0.1) 
    # setting the corresponding y - coordinates 
    y = np.sin(x) 
    # potting the points 
    plt.plot(x, y) 
    # function to show the plot 
    plt.show() 

if __name__=='__main__':
    main()