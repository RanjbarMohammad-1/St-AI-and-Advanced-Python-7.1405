# importing required modules 
import matplotlib.pyplot as plt 
import numpy as np 

def main():   
    # 1. Training data
    hours = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    scores = np.array([25, 32, 40, 48, 55, 65, 72, 85])

    # 2. Train a simple AI model
    # Find the best straight line: score = m * hours + b

    m, b = np.polyfit(hours, scores, 1)

    print("AI Model Training Completed!")
    print("Slope:", round(m, 2))
    print("Intercept:", round(b, 2))

    # 3. Predict scores
    new_hours = np.array([2.5, 4.5, 6.5])

    predicted_scores = m * new_hours + b

    for h, score in zip(new_hours, predicted_scores):
        print(f"Study hours: {h}, Predicted score: {score:.2f}")

    # 4. Draw the results
    plt.scatter(
        hours,
        scores,
        color="blue",
        label="Real student scores"
    )

    plt.plot(
        hours,
        m * hours + b,
        color="red",
        label="AI prediction line"
    )

    plt.scatter(
        new_hours,
        predicted_scores,
        color="green",
        marker="x",
        s=100,
        label="New predictions"
    )

    plt.xlabel("Study Hours")
    plt.ylabel("Exam Score")
    plt.title("AI: Predicting Student Scores")
    plt.legend()
    plt.grid(True)

    plt.show()

if __name__=='__main__':
    main()