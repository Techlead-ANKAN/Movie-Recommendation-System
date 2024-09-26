# Movie Recommendation System

## Introduction

This is a Python-based movie recommendation system that uses a database of Indian movies to suggest films based on user preferences. The system allows users to filter movies by genre, actors, directors, minimum rating, and maximum duration.

## Setup

To use this movie recommendation system, follow these steps:

1. Clone this repository to your local machine using `git clone https://github.com/your-username/movie-recommendation-system.git`
2. Make sure you have Python 3.x installed on your machine.
3. Install the required libraries by running `pip install pandas` in your terminal/command prompt.
4. Download the `final_cleaned_indian_movies_database.csv` file and place it in the same directory as the Python script.

## Running the System

To run the movie recommendation system, follow these steps:

1. Open a terminal/command prompt and navigate to the directory where the Python script is located.
2. Run the script using `python main.py`
3. Follow the prompts to enter your preferences:
	* Genres: Enter a comma-separated list of genres (e.g., "action, comedy, drama")
	* Actors: Enter a comma-separated list of actors (e.g., "shah rukh khan, salman khan, aamir khan")
	* Directors: Enter a comma-separated list of directors (e.g., "sanjay leela bhansali, rajkumar hirani, karthik subbaraj")
	* Minimum rating: Enter a number between 0 and 10 (e.g., "7.5")
	* Maximum duration: Enter a positive integer (e.g., "180")
4. Press Enter to skip any of the above prompts.

## Expected Output

After entering your preferences, the system will display a list of recommended movies that match your criteria. Each movie will have the following information:

* Title
* Year
* Duration
* Genre
* Director
* Actors
* Rating
* Votes

If no movies match your criteria, the system will display a message indicating that no movies were found.

## Troubleshooting

If you encounter any issues while running the system, check the following:

* Make sure the `final_cleaned_indian_movies_database.csv` file is in the correct location.
* Ensure that the Python script is running with the correct permissions.
* Check the console output for any error messages.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes. Make sure to follow standard professional guidelines for commit messages and API documentation.
