import pandas as pd  
import numpy as np 

def main():
    # importing pandas module  
    # making data frame  
    df = pd.read_csv("students.csv")  
    names = pd.Series(df['Name']) 
    data = names.head(10)
    print("name series :\n",data) 

    # using loc
    families=pd.Series(df['Family'])
    selectedFamilies=families.loc[3:7]
    print("selected family:\n",selectedFamilies)




if __name__=='__main__':
    main()