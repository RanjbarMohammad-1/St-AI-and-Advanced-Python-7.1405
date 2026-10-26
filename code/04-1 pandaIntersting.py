import pandas as pd  
import numpy as np 
from sklearn.tree import DecisionTreeClassifier
def main():  
    # 1. Create a dataset
    data = {
        "study_hours": [1, 2, 2, 3, 4, 5, 6, 7, 8, 9],
        "attendance":  [40, 50, 60, 55, 65, 70, 80, 85, 90, 95],
        "passed":     [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    }

    df = pd.DataFrame(data)

    # 2. Display the dataset
    print("Student Dataset:")
    print(df)

    # 3. Select the input features and target
    X = df[["study_hours", "attendance"]]
    y = df["passed"]

    # 4. Train a simple AI model
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X, y)

    # 5. Predict for a new student
    new_student = pd.DataFrame({
        "study_hours": [3],
        "attendance": [60]
    })

    prediction = model.predict(new_student)

    print("\nNew Student:")
    print(new_student)

    if prediction[0] == 1:
        print("AI Prediction: The student may PASS.")
    else:
        print("AI Prediction: The student may NOT PASS.")










if __name__=='__main__':
    main()