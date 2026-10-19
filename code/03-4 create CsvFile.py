import pandas as pd  
import numpy as np 

def main():
    df = pd.DataFrame({
        "Name": ["Ali", "Sara", "Reza", "Mary", "Omid", "Neda", "Amir", "Lila"],
        "Family": ["Ahmadi", "Karimi", "Hosseini", "Moradi", "Rahimi", "Jafari", "Mousavi", "Ebrahimi"],
        "Age": [20, 19, 21, 22, 20, 18, 23, 19],
        "Telephone": [
            "000-000-0001", "000-000-0002", "000-000-0003", "000-000-0004",
            "000-000-0005", "000-000-0006", "000-000-0007", "000-000-0008"
        ],
        "Address": [
            "Example Street 1", "Example Street 2", "Example Street 3", "Example Street 4",
            "Example Street 5", "Example Street 6", "Example Street 7", "Example Street 8"
        ]
    })

    path = "./students.csv"
    df.to_csv(path, index=False, encoding="utf-8")
    print(f"Created CSV file: {path}")
    print(df.to_string(index=False))



   

if __name__=='__main__':
    main()