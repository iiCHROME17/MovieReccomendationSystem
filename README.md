# Movie Recommendation System

## Abstract
This project is a full-stack Movie Recommendation System designed to help users discover movies similar to their interests. By leveraging movie metadata and natural language processing techniques, the system provides personalized recommendations based on content similarity. The backend processes and cleans movie data, while the frontend offers an interactive and visually appealing user experience.

## Intended Audience
- Movie enthusiasts seeking new recommendations
- Developers and data scientists interested in recommender systems
- Educators and students learning about machine learning and web development
- Anyone looking to explore content-based filtering techniques

## System Overview
The Movie Recommendation System consists of two main components:

### Backend
- **Language:** Python
- **Libraries:** Pandas (for data processing), scikit-learn (for feature extraction and similarity)
- **Functionality:**
  - Loads and preprocesses movie metadata
  - Cleans and extracts relevant features (genres, keywords, overview, etc.)
  - Computes similarity between movies using text-based features
  - Provides API endpoints for movie data, recommendations, and user favourites

### Frontend
- **Framework:** React (planned)
- **Styling:** Tailwind CSS or Bootstrap (planned)
- **Functionality:**
  - Displays movies as interactive cards
  - Allows users to add favourites and view recommendations
  - Communicates with the backend via REST API

## Data Source
- The movie metadata used in this project is sourced from Kaggle:
  - [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?resource=download&select=tmdb_5000_movies.csv)

---

Feel free to explore, contribute, or use this project as a learning resource for building recommendation systems! 