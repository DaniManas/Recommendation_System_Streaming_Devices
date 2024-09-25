import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split

class RecommendationSystem:
    def __init__(self):
        # Load MovieLens dataset (replace with the actual path to the large dataset)
        self.ratings = pd.read_csv('data/ratings_large.csv')  # Placeholder for large dataset
        self.movies = pd.read_csv('data/movies_large.csv')    # Placeholder for large dataset

        # Initialize SVD model for collaborative filtering
        self.model = SVD()

        # Train the collaborative filtering model on large data
        self.train_model()

    def train_model(self):
        # Use 'surprise' to load the dataset
        reader = Reader(rating_scale=(1, 5))
        data = Dataset.load_from_df(self.ratings[['userId', 'movieId', 'rating']], reader)
        trainset, testset = train_test_split(data, test_size=0.2)
        self.model.fit(trainset)

    def get_recommendations(self, user_id):
        # SVD based recommendations (Collaborative filtering)
        svd_recommendations = self.svd_recommend(user_id)
        content_recommendations = self.content_based_recommend(user_id)

        # Combine both collaborative and content-based filtering recommendations
        return svd_recommendations + content_recommendations

    def svd_recommend(self, user_id):
        # Placeholder logic for SVD-based recommendations (Assuming model has been trained)
        return [("Movie 1", 4.5), ("Movie 2", 4.2)]

    def content_based_recommend(self, user_id):
        # Content-based filtering using movie descriptions
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(self.movies['description'])
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

        idx = self.movies.index[self.movies['movieId'] == user_id].tolist()[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        movie_indices = [i[0] for i in sim_scores[:5]]

        return [(self.movies['title'].iloc[i], sim_scores[i][1]) for i in movie_indices]
