# Movie-Recommendation-System
A simple Movie Recommendation System that suggests similar movies based on content similarity using Python and Streamlit.

# 🎬 Movie Recommendation System

## 📌 Description

A simple Movie Recommendation System that suggests similar movies based on content similarity using Machine Learning.

---

## 🚀 Features

* 🔍 Search for movies
* 🎯 Get top 5 similar movie recommendations
* 🎬 Simple and interactive UI using Streamlit

---

## 🛠 Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit

---

## 📂 Project Structure

```
Movie-Recommendation-System/
│
├── app.py
├── model.py
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── requirements.txt
└── README.md
```

---

### ▶️ How to Run the Project
*1️⃣ Clone the repository
git clone https://github.com/your-username/Movie-Recommendation-System.git
cd Movie-Recommendation-System
*2️⃣ Install dependencies
pip install -r requirements.txt
*3️⃣ Run the application
streamlit run app.py

---

## ⚙️ How It Works

* Uses movie overview text to calculate similarity
* Converts text into vectors using CountVectorizer
* Applies cosine similarity
* Recommends top 5 similar movies

---

## 🎯 Future Improvements

* Add movie posters
* Show movie details (overview, ratings)
* Improve UI design


