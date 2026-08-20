import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="Netflix Data Analysis Dashboard",
    layout="wide"
)

st.title("NETFLIX")
st.subheader("DATA ANALYSIS DASHBOARD")

# -----------------------------
# Load data
# -----------------------------

df = pd.read_csv("netflix_titles.csv")

# Clean data

df = df.dropna(
    subset=['type', 'release_year', 'rating', 'country', 'duration']
)

# Dataset

st.subheader("Netflix Dataset")
st.dataframe(df.head())


# 1. Movies vs TV Shows

col1, col2 = st.columns(2)

with col1:

    st.subheader("Movies vs TV Shows")

    type_counts = df['type'].value_counts()

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.bar(
        type_counts.index,
        type_counts.values,
        color=['#E50914', '#222222']
    )

    ax.set_title("Number of Movies VS TV Shows on Netflix")
    ax.set_xlabel("Type")
    ax.set_ylabel("Count")

    st.pyplot(fig)


# 2. Content Rating

# 2. Content Rating

with col2:

    st.subheader("Content Rating")

    rating_counts = pd.concat([
        df["rating"].value_counts().head(5),
        pd.Series({
            "Other": df["rating"].value_counts().iloc[5:].sum()
        })
    ])

    fig, ax = plt.subplots(figsize=(6, 4))

    wedges, text = ax.pie(
        rating_counts,
        startangle=90,
        wedgeprops=dict(width=0.4)
    )

    ax.text(
        0, 0,
        "CONTENT\nRATING",
        ha='center',
        va='center',
        fontweight='bold'
    )

    ax.legend(
        wedges,
        rating_counts.index,
        title="Rating",
        loc="upper center",
        bbox_to_anchor=(0.5, 0.02),
        ncol=3,
        fontsize=8
    )

    ax.set_title(
        "Percentage of Content Rating"
    )

    st.pyplot(fig)


# 3. Movie Duration

col1, col2 = st.columns(2)

with col1:

    st.subheader("Movie Duration")

    movie_df = df[df['type'] == 'Movie'].copy()

    movie_df['duration_int'] = (
        movie_df['duration']
        .str.replace(' min', '')
        .astype(int)
    )

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.hist(
        movie_df['duration_int'],
        bins=30,
        color='#E50914',
        edgecolor='white'
    )

    ax.set_title("Distribution of Movie Duration")
    ax.set_xlabel("Duration (minutes)")
    ax.set_ylabel("Number of Movies")

    st.pyplot(fig)


# 4. Top 10 Directors

with col2:

    st.subheader("Top 10 Directors")

    director_counts = (
        df['director']
        .dropna()
        .str.split(', ')
        .explode()
        .value_counts()
        .head(10)
    )

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.barh(
        director_counts.index[::-1],
        director_counts.values[::-1],
        color='#E50914'
    )

    ax.set_title("Top 10 Directors by Number of Titles")
    ax.set_xlabel("Number of Titles")
    ax.set_ylabel("Director")

    st.pyplot(fig)


# 5. Top 10 Countries

col1, col2 = st.columns(2)

with col1:

    st.subheader("Top 10 Countries")

    country_counts = df['country'].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.barh(
        country_counts.index,
        country_counts.values,
        color='#E50914'
    )

    ax.set_title("Top 10 Countries by Number of Shows")
    ax.set_xlabel("Number of Shows")
    ax.set_ylabel("Country")

    st.pyplot(fig)


# 6. Top 10 Genres

with col2:

    st.subheader("Top 10 Genres")

    genre_counts = (
        df['listed_in']
        .str.split(', ')
        .explode()
        .value_counts()
        .head(10)
    )

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.barh(
        genre_counts.index,
        genre_counts.values,
        color='#222222'
    )

    ax.set_title("Top 10 Genres on Netflix")
    ax.set_xlabel("Number of Shows")
    ax.set_ylabel("Genre")

    st.pyplot(fig)


# 7. Movies Released Per Year

col1, col2 = st.columns(2)

with col1:

    st.subheader("Movies Released Per Year")

    content_by_year = (
        df.pivot_table(
            index='release_year',
            columns='type',
            values='show_id',
            aggfunc='count'
        )
    )

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.plot(
        content_by_year.index,
        content_by_year['Movie'],
        color='#E50914',
        linewidth=2
    )

    ax.set_title("Movies Released Per Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Movies")

    st.pyplot(fig)


# 8. TV Shows Released Per Year

with col2:

    st.subheader("TV Shows Released Per Year")

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.plot(
        content_by_year.index,
        content_by_year['TV Show'],
        color='#222222',
        linewidth=2
    )

    ax.set_title("TV Shows Released Per Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Shows")

    st.pyplot(fig)


# Run:
# python -m streamlit run app.py