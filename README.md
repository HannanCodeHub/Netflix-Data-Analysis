````markdown
# 🎬 Netflix Data Analysis & Visualization Dashboard

A Python-based **Netflix Data Analysis and Visualization project** that explores the Netflix Titles dataset through data cleaning, exploratory data analysis (EDA), statistical insights, and an interactive Streamlit dashboard.

The project includes both a **Matplotlib-based visualization dashboard** and a **Dockerized Streamlit application**, making the dashboard easy to run across different environments.

## 📊 Project Overview

This project analyzes Netflix movies and TV shows to identify patterns and trends related to:

- 🎬 Movies vs TV Shows
- 🔞 Content ratings
- ⏱️ Movie duration
- 🎥 Top 10 directors
- 🌍 Top 10 countries
- 🎭 Top 10 genres
- 📅 Movies released per year
- 📺 TV Shows released per year

The analysis was performed using Python data analysis and visualization libraries, while the final dashboard was built using **Streamlit and Matplotlib**.

## 🛠️ Technologies Used

- **Python**
- **Pandas** – Data manipulation and analysis
- **NumPy** – Numerical operations
- **Matplotlib** – Data visualization and dashboard creation
- **Seaborn** – Exploratory data visualization
- **Streamlit** – Interactive web dashboard
- **Docker** – Application containerization
- **Git & GitHub** – Version control

## 🧹 Data Cleaning

The Netflix dataset was cleaned and prepared before analysis and visualization.

The cleaning process included:

- Handling missing values in important columns
- Handling missing ratings, countries, durations, and release years
- Separating movie duration into numerical values
- Processing multiple countries and genres
- Removing or handling unnecessary data
- Preparing the data for analysis and visualization

## 📈 Visualizations

The project contains eight major visualizations:

1. **Movies vs TV Shows** – Compares the number of movies and TV shows available.
2. **Content Rating Distribution** – Shows the distribution of Netflix content ratings.
3. **Movie Duration Distribution** – Analyzes movie durations in minutes.
4. **Top 10 Directors** – Identifies directors with the highest number of titles.
5. **Top 10 Countries** – Shows countries producing the highest number of Netflix titles.
6. **Top 10 Genres** – Highlights the most common genres.
7. **Movies Released Per Year** – Shows the yearly trend of movie releases.
8. **TV Shows Released Per Year** – Shows the yearly trend of TV show releases.

## 🎨 Matplotlib Dashboard

A Netflix-themed dashboard was created using Matplotlib with:

- Custom subplot layout
- Netflix-inspired styling
- Donut chart
- Horizontal bar charts
- Line charts
- Histogram
- Custom typography
- Grid and axis styling
- Netflix watermark
- High-resolution PNG export

## 🌐 Streamlit Dashboard

The project also includes a **Streamlit web application** that presents the Netflix analysis through an interactive dashboard.

The Streamlit application can be launched locally using:

```bash
streamlit run app.py
````

The application will then be available at:

```text
http://localhost:8501
```

## 🐳 Docker Support

The Streamlit application has been **containerized using Docker**, allowing the project to run without manually configuring the Python environment.

### Build the Docker Image

```bash
docker build -t netflix-streamlit .
```

### Run the Container

```bash
docker run -d -p 8501:8501 --name netflix-container netflix-streamlit
```

Then open:

```text
http://localhost:8501
```

### Docker Hub

The Docker image is available on Docker Hub:

**hannanahmed07/netflix-streamlit**

### Pull the Docker Image

```bash
docker pull hannanahmed07/netflix-streamlit:latest
```

### Run from Docker Hub

```bash
docker run -d -p 8501:8501 hannanahmed07/netflix-streamlit:latest
```

## 📁 Project Structure

```text
Netflix-Data-Analysis/
│
├── Dockerfile
├── README.md
├── app.py
├── requirents.txt
├── netflix_titles.csv
│
├── netflix-analysis.py
├── netflix-dashboard.py
│
├── Netflix_Logomark.png
├── Netflix Data Analysis Dashboard .png
├── content_ratings.png
├── movie_duration_histogram.png
├── movies_tv_shows_comparison.png
├── movies_vs_tvshows.png
├── release_year_Scatter.png
└── top10_countries.png
```

## 🚀 How to Run Locally

### Without Docker

Install the required dependencies:

```bash
pip install -r requirents.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

Open the application in your browser:

```text
http://localhost:8501
```

### Using Docker

Make sure Docker Desktop is running, then:

```bash
docker build -t netflix-streamlit .
docker run -d -p 8501:8501 --name netflix-container netflix-streamlit
```

Open the application:

```text
http://localhost:8501
```

## 🎯 Project Goals

The main goals of this project are to:

* Practice data cleaning with Pandas
* Perform exploratory data analysis
* Understand patterns in Netflix content
* Develop effective data visualizations
* Build dashboards using Python
* Learn Streamlit application development
* Learn Docker containerization
* Understand Docker image and container workflows
* Practice sharing applications through Docker Hub

## 👨‍💻 Author
**Hannan Ahmed**

GitHub: **HannanCodeHub**

```
```
