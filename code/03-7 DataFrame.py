import pandas as pd  
import numpy as np 

def main():

    # Calling DataFrame constructor 
    print(" Calling DataFrame constructor \n")
    df = pd.DataFrame() 
    print(df)

    print("====================================\n")
    print("Calling DataFrame constructor on list ")
    lst = ['this', 'is', 'a', 'practial', 
			'article', 'for', 'Pandas'] 
    # Calling DataFrame constructor on list 
    df = pd.DataFrame(lst) 
    print(df)

    print("====================================\n")
    print("Calling DataFrame constructor on list ")
    # list of strings 
    lst = ['this', 'is', 'a', 'practical', 
                'article', 'for', 'Pandas'] 
    # Calling DataFrame constructor on list 
    df = pd.DataFrame(lst, index=['row1','row2',
    'row3','row4','row5','row6','row7'], columns=['col1']) 
    print(df)






if __name__=='__main__':
    main()