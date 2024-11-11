import glob
import os

import numpy as np
import pandas as pd

all_files = glob.glob(os.path.join("../data/raw", "likes-*.csv"))

df = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Remove leading and trailing whitespace everywhere
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

    # Drop rows with missing data in columns: 'Song', 'Artist', 'Album'
    df = df.dropna(subset=["Song", "Artist", "Album"])

    # Clean 'Genres' and 'Parent Genres' columns
    df["Genres"] = df["Genres"].apply(
        lambda x: set(map(str.strip, x.split(","))) if isinstance(x, str) else set()
    )
    df["Parent Genres"] = df["Parent Genres"].apply(
        lambda x: set(map(str.strip, x.split(","))) if isinstance(x, str) else set()
    )

    # Sort by columns: 'Artist' (ascending), 'Album' (ascending), 'Song' (ascending)
    df = df.sort_values(["Artist", "Album", "Song"], na_position="first")

    # Remove duplicate rows for the same song by the same artist, while unioning
    # the 'Genres' and 'Parent Genres' columns
    df = df.groupby(["Song", "Artist"], as_index=False).agg(
        {
            "Genres": lambda x: ",".join(
                set([item for sublist in x for item in sublist])
            ),
            "Parent Genres": lambda x: ",".join(
                set([item for sublist in x for item in sublist])
            ),
            **{
                col: "first"
                for col in df.columns
                if col not in ["Song", "Artist", "Genres", "Parent Genres"]
            },
        }
    )
    return df


df_clean = clean_data(df.copy())
df_clean.to_csv(os.path.join("../data/interim", "cleaned_likes.csv"), index=False)


def extract_artists_and_count_songs(df: pd.DataFrame) -> pd.DataFrame:
    # Split the 'Artist' column into individual artists
    artists_series = df["Artist"].str.split(",").explode().str.strip()

    # Count the number of songs by each artist
    artist_counts = artists_series.value_counts().reset_index()
    artist_counts.columns = ["Artist", "Song Count"]

    return artist_counts.sort_values(
        ["Song Count", "Artist"], ascending=[False, True]
    ).reset_index(drop=True)


artist_counts_df = extract_artists_and_count_songs(df_clean)
artist_counts_df.to_csv(
    os.path.join("../data/interim", "artist_counts.csv"), index=False
)

# Keep only rows where song count is > 1
artist_counts_df_multi = artist_counts_df.copy()[artist_counts_df["Song Count"] > 1]
artist_counts_df_multi.to_csv(
    os.path.join("../data/interim", "artist_counts_multi.csv"), index=False
)
