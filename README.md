# Spotify likes/playlist analysis

I wanted to know which artists' songs I've liked the most on Spotify. Turns out Spotify doesn't provide this information. Through [this reddit post](https://www.reddit.com/r/spotify/comments/s4v8z6/is_there_a_way_to_show_which_artists_i_have_the/) I found the [Chosic Spotify Playlist Analyzer](https://www.chosic.com/spotify-playlist-analyzer/), which does display some interesting stats but isn't exactly what I was looking for. However, one handy feature is that it allows you to easily download a CSV file with all the songs in the playlist. Exactly the excuse I needed to dip my toes into some data analysis with Python. One [data science VS Code setup tutorial](https://www.youtube.com/watch?v=mpk4Q5feWaw) and a few hours later, here we are.

## How to use this project with your own Spotify data

[This comment](https://www.reddit.com/r/spotify/comments/s4v8z6/comment/kgfj77e/) explains how you can get your liked songs into a playlist for use with the Chosic app.

Chosic only supports playlists up to 5000 songs, and I've liked more songs than that. As a quick workaround, I split my liked songs into multiple playlists and downloaded the CSV file for each playlist separately.

Just place your CSV files in the [`./data/raw`](./data/raw) folder, naming them `likes-*.csv` (e.g. `likes-1.csv`, `likes-2.csv`). Then run the [`./src/dataset.py`](./src/dataset.py) script to clean and extract the data. Extracted data is currently written to CSV files in the [`./data/interim`](./data/interim) folder.

The data cleaning actually turned out to be pretty important to get any kind of accurate song count, as Spotify often has duplicate entries for the same song by the same artist, and over time they change which one appears on the artist's page so it's practically inevitable you end up liking the same song multiple times.

If you want to edit the code at all, or explore the data further, I highly recommend using the Jupyter interactive window feature for this. The tutorial I linked above explains how to set this up. Super nice workflow, especially when combined with the [Data Wrangler extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.datawrangler) for viewing the DataFrame Jupyter variables and with the built-in Copilot features.

---

## Data Project Template

<a target="_blank" href="https://datalumina.com/">
    <img src="https://img.shields.io/badge/Datalumina-Project%20Template-2856f7" alt="Datalumina Project" />
</a>

### Cookiecutter Data Science

This project template is a simplified version of the [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org) template, created to suit the needs of Datalumina and made available as a GitHub template.

### Adjusting .gitignore

Ensure you adjust the `.gitignore` file according to your project needs. For example, since this is a template, the `/data/` folder is commented out and data will not be exlucded from source control:

```plaintext
# exclude data from source control by default
# /data/
```

Typically, you want to exclude this folder if it contains either sensitive data that you do not want to add to version control or large files.

### Duplicating the .env File

To set up your environment variables, you need to duplicate the `.env.example` file and rename it to `.env`. You can do this manually or using the following terminal command:

```bash
cp .env.example .env # Linux, macOS, Git Bash, WSL
copy .env.example .env # Windows Command Prompt
```

This command creates a copy of `.env.example` and names it `.env`, allowing you to configure your environment variables specific to your setup.

### Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── README.md          <- The top-level README for developers using this project
├── data
│   ├── external       <- Data from third party sources
│   ├── interim        <- Intermediate data that has been transformed
│   ├── processed      <- The final, canonical data sets for modeling
│   └── raw            <- The original, immutable data dump
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
└── src                         <- Source code for this project
    │
    ├── __init__.py             <- Makes src a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    │
    ├── modeling
    │   ├── __init__.py
    │   ├── predict.py          <- Code to run model inference with trained models
    │   └── train.py            <- Code to train models
    │
    ├── plots.py                <- Code to create visualizations
    │
    └── services                <- Service classes to connect with external platforms, tools, or APIs
        └── __init__.py
```

---
