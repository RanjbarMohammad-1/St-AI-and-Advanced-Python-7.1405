# importing required modules 
import matplotlib.pyplot as plt 
import numpy as np 


def main():
        
    # ==================================================
    # PHASE 1: BUSINESS UNDERSTANDING
    # Goal: Predict student exam scores
    # ==================================================

    print("AI PROJECT: Student Performance Prediction")


    # ==================================================
    # PHASE 2: DATA UNDERSTANDING
    # Create a sample dataset of 80 students
    # ==================================================

    np.random.seed(42)

    number_of_students = 80

    study_hours = np.random.uniform(0, 12, number_of_students)
    attendance = np.random.uniform(50, 100, number_of_students)
    previous_score = np.random.uniform(20, 100, number_of_students)

    # Create example exam scores with some random variation
    noise = np.random.normal(0, 5, number_of_students)

    exam_score = (
        3.2 * study_hours
        + 0.25 * attendance
        + 0.45 * previous_score
        - 10
        + noise
    )

    exam_score = np.clip(exam_score, 0, 100)

    # Combine the input features into one NumPy array
    X = np.column_stack((
        study_hours,
        attendance,
        previous_score
    ))

    y = exam_score

    print("\nDataset shape:", X.shape)
    print("Target shape:", y.shape)
    print("Missing input values:", np.isnan(X).sum())
    print("Missing target values:", np.isnan(y).sum())

    print("\nFirst five students:")
    print(X[:5])

    print("\nFirst five exam scores:")
    print(y[:5])


    # Visualize one relationship in the data
    plt.figure("Visualize one relationship in the data")
    plt.scatter(study_hours, exam_score)
    plt.xlabel("Study Hours per Week")
    plt.ylabel("Exam Score")
    plt.title("Study Hours vs Exam Scores")
    plt.grid(True)
    plt.show(block=False)


    # ==================================================
    # PHASE 3: DATA PREPARATION
    # Split the data into training and testing sets
    # ==================================================

    indices = np.random.permutation(number_of_students)

    train_size = int(0.8 * number_of_students)

    train_indices = indices[:train_size]
    test_indices = indices[train_size:]

    X_train = X[train_indices]
    X_test = X[test_indices]

    y_train = y[train_indices]
    y_test = y[test_indices]

    print("\nTraining students:", len(X_train))
    print("Testing students:", len(X_test))


    # ==================================================
    # PHASE 4: MODELING
    # Train a linear regression model using NumPy
    # ==================================================

    # Add a column of ones for the intercept
    X_train_model = np.column_stack((
        np.ones(len(X_train)),
        X_train
    ))

    # Learn the model parameters
    weights = np.linalg.lstsq(
        X_train_model,
        y_train,
        rcond=None
    )[0]

    print("\nLearned model parameters:")
    print("Intercept:", round(weights[0], 2))
    print("Study hours coefficient:", round(weights[1], 2))
    print("Attendance coefficient:", round(weights[2], 2))
    print("Previous score coefficient:", round(weights[3], 2))


    # ==================================================
    # PHASE 5: EVALUATION
    # Test the model on unseen students
    # ==================================================

    X_test_model = np.column_stack((
        np.ones(len(X_test)),
        X_test
    ))

    predictions = X_test_model @ weights

    # Mean Absolute Error
    mae = np.mean(np.abs(y_test - predictions))

    print("\nModel Evaluation")
    print("Mean Absolute Error:", round(mae, 2))
    plt.figure("Actual vs Predicted Scores")

    # Plot actual scores against predicted scores
    plt.scatter(
        y_test,
        predictions,
        label="Test students"
    )

    plt.plot(
        [0, 100],
        [0, 100],
        "r--",
        label="Perfect predictions"
    )
    plt.xlabel("Actual Exam Score")
    plt.ylabel("Predicted Exam Score")
    plt.title("Actual vs Predicted Scores")
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.legend()
    plt.grid(True)
    plt.plot()
    plt.show()


    # ==================================================
    # PHASE 6: DEPLOYMENT
    # Predict the score of a new student
    # ==================================================

    new_student = np.array([[6, 90, 75]])

    new_student_model = np.column_stack((
        np.ones(len(new_student)),
        new_student
    ))

    new_prediction = new_student_model @ weights

    predicted_score = np.clip(new_prediction[0], 0, 100)

    print("\nNew Student")
    print("Study hours: 6")
    print("Attendance: 90%")
    print("Previous score: 75")
    print("Predicted exam score:", round(predicted_score, 2))

        
        





if __name__=='__main__':
    main()