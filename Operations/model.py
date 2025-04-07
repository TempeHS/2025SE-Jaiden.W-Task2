import pickle
import numpy as np
import joblib
import pandas as pd

class MLModel:
    def __init__(self, model):
        self.model = model

    def load_model(self, model_path):
        try:
            with open(model_path, "rb") as model_file:
                self.model = pickle.load(model_file)
            print(f"Model loaded successfully from {model_path}")
        except FileNotFoundError:
            print(f"Error: Model file not found at {model_path}")
        except Exception as e:
            print(f"Error loading model: {e}")

    def preprocess_input(self, input_data):
        # Load the saved scaler
        scaler = joblib.load('../Model_Testing_and_Validation/scaler.pkl')

        # Define the custom rating order
        rating_order = ['G', 'TV-PG', 'PG', 'Approved', 'Unrated', 'Not Rated', 'PG-13', 'TV-14', 'R', 'TV-MA', 'NC-17', 'X']
        rating_mapping = {rating: idx for idx, rating in enumerate(rating_order)}

        # Convert input_data to a DataFrame for processing
        input_df = pd.DataFrame([input_data])

        # Extract release quarter from release_date
        if 'release_date' in input_df:
            input_df['release_date'] = pd.to_datetime(input_df['release_date'], errors='coerce')
            input_df['release_quarter'] = input_df['release_date'].dt.quarter
            input_df.drop(columns=['release_date'], inplace=True)

        # Ensure all numerical features expected by the scaler are present
        numerical_features = ['budget', 'runtime', 'gross', 'votes', 'score']
        for feature in numerical_features:
            if feature not in input_df:
                input_df[feature] = 0  # Add missing numerical features with default value 0

        # Scale numerical features
        input_df[numerical_features] = scaler.transform(input_df[numerical_features])

        # Encode the 'rating' column
        if 'rating' in input_df:
            input_df['rating'] = input_df['rating'].map(rating_mapping)

        # One-hot encode the 'genre' column
        if 'genre' in input_df:
            genre_dummies = pd.get_dummies(input_df['genre'], prefix='genre')
            input_df = pd.concat([input_df, genre_dummies], axis=1)
            input_df.drop(columns=['genre'], inplace=True)

        # Ensure 'is_sequel' is binary
        if 'is_sequel' in input_df:
            input_df['is_sequel'] = input_df['is_sequel'].astype(int)

        # Ensure all required genre columns exist, even if missing in input
        genre_columns = [
            'genre_Action', 'genre_Adventure', 'genre_Animation', 'genre_Biography', 'genre_Comedy',
            'genre_Crime', 'genre_Drama', 'genre_Family', 'genre_Fantasy', 'genre_Horror',
            'genre_Music', 'genre_Musical', 'genre_Mystery', 'genre_Romance', 'genre_Sci-Fi',
            'genre_Sport', 'genre_Thriller', 'genre_Western'
        ]
        for col in genre_columns:
            if col not in input_df:
                input_df[col] = 0  # Add missing genre columns with default value 0

        # Reorder columns to match the model's expected input order
        mx_col = [
            'budget', 'release_quarter', 'rating', 'is_sequel', 'runtime',
            'genre_Action', 'genre_Adventure', 'genre_Animation', 'genre_Biography', 'genre_Comedy',
            'genre_Crime', 'genre_Drama', 'genre_Family', 'genre_Fantasy', 'genre_Horror',
            'genre_Music', 'genre_Musical', 'genre_Mystery', 'genre_Romance', 'genre_Sci-Fi',
            'genre_Sport', 'genre_Thriller', 'genre_Western'
        ]
        input_df = input_df.reindex(columns=mx_col, fill_value=0)

        # Return the preprocessed input
        return input_df

    def predict(self, input_data):
        preprocessed_data = self.preprocess_input(input_data)
        preprocessed_array = preprocessed_data.to_numpy() # Convert preprocessed data to a NumPy array
        prediction = self.model.predict(preprocessed_array)
        scaler = joblib.load('../Model_Testing_and_Validation/scaler.pkl')
        
        # Create a placeholder array with the same shape as the scaler's training data
        placeholder = np.zeros((1, scaler.n_features_in_))  # Ensure the array matches the scaler's input shape
        placeholder[0, 2] = prediction[0]  # Place the prediction in the 2nd position (index 2 for 'gross')
        unscaled_prediction = scaler.inverse_transform(placeholder)[0, 2]
        return unscaled_prediction

    def train_model(self, training_data, labels):
        # Logic to train the machine learning model
        pass