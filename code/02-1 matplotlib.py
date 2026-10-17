
# importing the required module 
import matplotlib.pyplot as plt 
def example1():

    fig = plt.figure()
    fig.canvas.manager.set_window_title("AI class")
    # x axis values 
    x = [1,2,3] 
    # corresponding y axis values 
    y = [2,4,1] 
    # plotting the points  
    plt.plot(x, y) 
    # naming the x axis 
    plt.xlabel('x - axis') 
    # naming the y axis 
    plt.ylabel('y - axis') 
    # giving a title to my graph 
    plt.title('My first graph!') 
    # function to show the plot 
    plt.show()


def example2():
    # line 1 points 
    x1 = [1,2,3] 
    y1 = [2,4,1] 
    # plotting the line 1 points 
    plt.plot(x1, y1, label = "line 1") 
    # line 2 points 
    x2 = [1,2,3] 
    y2 = [4,1,3] 
    # plotting the line 2 points 
    plt.plot(x2, y2, label = "line 2") 
    # naming the x axis 
    plt.xlabel('x - axis') 
    # naming the y axis 
    plt.ylabel('y - axis') 
    # giving a title to my graph 
    plt.title('Two lines on same graph!') 
    # show a legend on the plot 
    plt.legend() 
    # function to show the plot 
    plt.show() 

if __name__== '__main__':
    example1()
    example2()