import matplotlib.pyplot as plt   



def main():
    # x-coordinates of left sides of bars   
    left = [1, 2, 3, 4, 5]   
    # heights of bars   
    height = [10, 20, 30, 40, 50]   
    # labels for bars   
    tick_label = ['one', 'two', 'three', 'four', 'five']   
    # plotting a bar chart   
    plt.bar(left, height, tick_label = tick_label,   
            width = 0.8, color = ['blue', 'green', 'red','yellow','black'])   
    # naming the x-axis   
    plt.xlabel('x - axis')   
    # naming the y-axis   
    plt.ylabel('y - axis')   
    # plot title   
    plt.title('bar chart!')   
    # function to show the plot   
    plt.show()



if __name__=='__main__':
    main()