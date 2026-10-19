import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt

def main():   

    # # 1 like and array
    print("==============================\n")
    print("1 like and array")
    # Creating empty series  
    ser = pd.Series()  
    print(ser)  
    # simple array  
    data = np.array(['g', 'e', 'e', 'k', 's'])  
    ser = pd.Series(data)  
    print(ser)

    # # 2 like a series
    print("==============================\n")
    print("value index")
    my_series=pd.Series([1., 2., 3.], index=['a', 'b', 'c'])
    print("my_series.values : ",my_series.values)
    print("my_series.index : ",my_series.index)

    # 3 like dictionary
    print("==============================\n")
    print("dictionary:")
    data = {'a' : 0., 'b' : 1., 'c' : 2.}
    s = pd.Series(data)
    print (s) 

    print("==============================\n")
    print("dictionary add index:")
    data = {'a' : 0., 'b' : 1., 'c' : 2.}
    s = pd.Series(data,index=['b','c','d','a'])
    print (s)

   

if __name__=='__main__':
    main()