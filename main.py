import pandas as pd

def load_database():
    # Load the database from a CSV file
    df = pd.read_csv('final_cleaned_indian_movies_database.csv')
    return df

def get_user_filters():
    filters = {}
    print("Enter your preferences (press Enter to skip):")
    filters['genres'] = input("Genres (comma-separated): ").lower().split(',')
    filters['actors'] = input("Actors (comma-separated): ").lower().split(',')
    filters['directors'] = input("Directors (comma-separated): ").lower().split(',')
    while True:
        try:
            filters['min_rating'] = float(input("Minimum rating (0-10): ") or 0)
            if filters['min_rating'] < 0 or filters['min_rating'] > 10:
                print("Rating should be between 0 and 10. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 10.")
    while True:
        try:
            filters['max_duration'] = int(input("Maximum duration (in minutes): ") or 1000)
            if filters['max_duration'] < 0:
                print("Duration should be a positive number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive number.")
    return {k: v for k, v in filters.items() if v}

def apply_filters(df, filters):
    df['Duration'] = df['Duration'].astype(int)  # Convert 'Duration' column to integers
    filtered_df = df.copy()
    if 'genres' in filters:
        for genre in filters['genres']:
            filtered_df = filtered_df[filtered_df['Genre'].str.lower().str.contains(genre.strip())]
            print(f"Filtered by genre: {genre}")
            print(filtered_df)
    if 'actors' in filters:
        for actor in filters['actors']:
            filtered_df = filtered_df[(filtered_df['Actor 1'].str.lower().str.contains(actor.strip())) |
                                        (filtered_df['Actor 2'].str.lower().str.contains(actor.strip())) |
                                        (filtered_df['Actor 3'].str.lower().str.contains(actor.strip()))]
            print(f"Filtered by actor: {actor}")
            print(filtered_df)
    if 'directors' in filters:
        for director in filters['directors']:
            filtered_df = filtered_df[filtered_df['Director'].str.lower().str.contains(director.strip())]
            print(f"Filtered by director: {director}")
            print(filtered_df)
    if 'min_rating' in filters:
        filtered_df = filtered_df[filtered_df['Rating'] >= filters['min_rating']]
        print(f"Filtered by minimum rating: {filters['min_rating']}")
        print(filtered_df)
    if 'max_duration' in filters:
        filtered_df = filtered_df[filtered_df['Duration'] <= filters['max_duration']]
        print(f"Filtered by maximum duration: {filters['max_duration']}")
        print(filtered_df)
    return filtered_df

def main():
    df = load_database()
    print("Database:")
    print(df)

    user_filters = get_user_filters()
    print("Filters:")
    print(user_filters)

    filtered_df = apply_filters(df, user_filters)

    if filtered_df.empty:
        print("No movies match your criteria. Try broadening your filters.")
    else:
        print("\nRecommended Movies:")
        for _, movie in filtered_df.iterrows():
            print(f"Title: {movie['Name']} ")
            print(f"Year: {movie['Year']} ")
            print(f"Duration: {movie['Duration']} minutes ")
            print(f"Genre: {movie['Genre']} ")
            print(f"Director: {movie['Director']} ")
            print(f"Actors: {movie['Actor 1']}, {movie['Actor 2']}, {movie['Actor 3']} ")
            print(f"Rating: {movie['Rating']} ")
            print(f"Votes: {movie['Votes']} ")
            print("-" * 50)

if __name__ == "__main__":
    main()