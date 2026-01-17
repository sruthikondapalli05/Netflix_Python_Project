def count_movies(df):
    """
    Counts how many movies are present in the Netflix dataset.

    Parameters:
    df (pandas.DataFrame): Netflix dataset

    Returns:
    int: Number of movies
    """
    return (df['type'] == 'Movie').sum()
