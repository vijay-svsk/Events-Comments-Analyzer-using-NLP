# NLP Sentiment Analyzer for Event Feedback

Welcome to the NLP Sentiment Analyzer for Event Feedback project! This project aims to analyze comments provided by attendees during or after an event to determine the sentiment and gauge the success of the event based on collected opinions.

## Overview
The project utilizes Natural Language Processing (NLP) techniques to perform sentiment analysis on comments provided by event attendees. It employs the VADER lexicon for sentiment analysis and visualizes the sentiment distribution using pie charts.

## Features
- **Sentiment Analysis**: Analyze the sentiment of comments provided by attendees using the VADER lexicon.
- **Visualization**: Visualize the sentiment distribution using pie charts to understand the overall sentiment of event feedback.
- **Scalability**: The system can handle a large volume of comments efficiently, making it suitable for events of various scales.

## Prerequisites
- Python 3.x
- Pandas
- NLTK (Natural Language Toolkit)
- Matplotlib

## How to Use
1. **Clone the Repository**: Clone this repository to your local machine.
2. **Install Dependencies**: Install the required dependencies using pip:
   ```
   pip install pandas nltk matplotlib
   ```
3. **Download NLTK Resources**: Download the VADER lexicon from NLTK using the following command:
   ```python
   import nltk
   nltk.download('vader_lexicon')
   ```
4. **Prepare the Dataset**: Prepare a CSV file containing attendee comments. Ensure that the CSV file has columns named 'Student_Name' and 'Comments'.
5. **Run the Code**: Execute the main script `sentiment_analyzer.py`. Make sure to replace the file path `'Comments.csv'` with the actual path to your CSV file.
6. **Review Results**: The script will perform sentiment analysis on the comments and visualize the sentiment distribution. You'll see the sentiment analysis results for each student and the average positive percentage for all students.

## Example Usage
Suppose you have a CSV file named `Comments.csv` containing attendee comments. You can run the script as follows:
```python
python sentiment_analyzer.py
```

## Contributors
- [Vijay Sai Kumar](https://github.com/vijay-svsk)
- [Sri Harsh](https://github.com/sriharsh-2003)
- [Kailash Varma](https://github.com/kailash123varma)

Feel free to contribute to this project by providing feedback, suggesting improvements, or adding new features!

---
*Note: This project is designed for analyzing event feedback using NLP-based sentiment analysis techniques. Make sure to credit NLTK for the sentiment analysis lexicon and adhere to its licensing terms.*
