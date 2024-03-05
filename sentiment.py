import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Download the VADER lexicon (required for SentimentIntensityAnalyzer)
nltk.download('vader_lexicon')


def analyze_sentiment(comment):
    sid = SentimentIntensityAnalyzer()
    sentiment_score = sid.polarity_scores(comment)
    return sentiment_score['compound']


def visualize_sentiment(positive_percentage):
    labels = ['Positive', 'Negative']
    sizes = [positive_percentage, 100 - positive_percentage]
    colors = ['#4CAF50', '#FF5733']  # Green for positive, Orange for negative

    plt.pie(sizes, labels=labels, colors=colors,
            autopct='%1.1f%%', startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.axis('equal')
    plt.title('Sentiment Analysis for the Event')
    plt.show()


def analyze_and_visualize_sentiment(student_data):
    positive_percentages = []

    for _, row in student_data.iterrows():
        student_name = row['Student_Name']
        comments = row['Comments']

        # Perform sentiment analysis
        sentiment_score = analyze_sentiment(comments)
        # Convert to percentage (normalized to [0, 100])
        positive_percentage = (sentiment_score + 1) * 50
        positive_percentages.append(positive_percentage)

        # Output: Show the percentage of positiveness
        print(f"\nSentiment Analysis Result for {student_name}:")
        print(f"Positive Percentage: {positive_percentage:.2f}%")

    # Visualize sentiment for all students in a ring graph
    average_positive_percentage = sum(
        positive_percentages) / len(positive_percentages)
    print(
        f"\nAverage Positive Percentage for All Students: {average_positive_percentage:.2f}%")
    visualize_sentiment(average_positive_percentage)


def main():
    # Load the dataset from a CSV file
   # Replace with the actual path to your CSV file
    student_data = pd.read_csv('Comments.csv', encoding='latin1')

    # Analyze and visualize sentiment for each student
    analyze_and_visualize_sentiment(student_data)


if __name__ == "__main__":
    main()