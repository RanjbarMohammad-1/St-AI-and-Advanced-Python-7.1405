import pandas as pd  
import numpy as np 

def main():
    # creating a series
    data1 = pd.Series([5, 2, 3,7], index=['a', 'b', 'c', 'd'])
    print("data1=\n",data1)
    # creating a series
    data2 = pd.Series([1, 6, 4, 9], index=['a', 'b', 'd', 'e'])
    print("data2=\n",data2)

    # add 
    addValue=data1.add(data2,fill_value=0)
    print("addValue:\n",addValue)



if __name__=='__main__':
    main()