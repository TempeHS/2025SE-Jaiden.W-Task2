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

    def load_scaler(self):
        """Load the saved scaler."""
        return joblib.load('../Model_Testing_and_Validation/scaler.pkl')

    def map_rating(self, input_df):
        """Map the 'rating' column to numerical values."""
        rating_order = ['G', 'TV-PG', 'PG', 'Approved', 'Unrated', 'Not Rated', 'PG-13', 'TV-14', 'R', 'TV-MA', 'NC-17', 'X']
        rating_mapping = {rating: idx for idx, rating in enumerate(rating_order)}
        if 'rating' in input_df:
            input_df['rating'] = input_df['rating'].map(rating_mapping)
        return input_df

    def extract_release_quarter(self, input_df):
        """Extract the release quarter from the release date."""
        if 'release_date' in input_df:
            input_df['release_date'] = pd.to_datetime(input_df['release_date'], errors='coerce')
            input_df['release_quarter'] = input_df['release_date'].dt.quarter
            input_df.drop(columns=['release_date'], inplace=True)
        return input_df

    def ensure_numerical_features(self, input_df, numerical_features):
        """Ensure all numerical features are present in the input."""
        for feature in numerical_features:
            if feature not in input_df:
                input_df[feature] = 0  # Add missing numerical features with default value 0
        return input_df

    def scale_numerical_features(self, input_df, numerical_features, scaler):
        """Scale numerical features using the provided scaler."""
        input_df[numerical_features] = scaler.transform(input_df[numerical_features])
        return input_df

    def one_hot_encode_genre(self, input_df):
        """One-hot encode the 'genre' column."""
        if 'genre' in input_df:
            genre_dummies = pd.get_dummies(input_df['genre'], prefix='genre')
            genre_dummies = genre_dummies.astype(int)  # Ensure values are integers (0 or 1)
            input_df = pd.concat([input_df, genre_dummies], axis=1)
            input_df.drop(columns=['genre'], inplace=True)
        return input_df

    def ensure_genre_columns(self, input_df, genre_columns):
        """Ensure all required genre columns exist, even if missing in input."""
        for col in genre_columns:
            if col not in input_df:
                input_df[col] = 0  # Add missing genre columns with default value 0
        return input_df

    def reorder_columns(self, input_df, column_order):
        """Reorder columns to match the model's expected input order."""
        input_df = input_df.reindex(columns=column_order, fill_value=0)
        return input_df

    def preprocess_input(self, input_data):
        """Main method to preprocess input data."""
        # Load the scaler
        scaler = self.load_scaler()

        # Convert input_data to a DataFrame for processing
        input_df = pd.DataFrame([input_data])

        # Define numerical features and genre columns
        numerical_features = ['budget', 'runtime', 'gross', 'votes', 'score']
        genre_columns = [
            'genre_Action', 'genre_Adventure', 'genre_Animation', 'genre_Biography', 'genre_Comedy',
            'genre_Crime', 'genre_Drama', 'genre_Family', 'genre_Fantasy', 'genre_Horror',
            'genre_Music', 'genre_Musical', 'genre_Mystery', 'genre_Romance', 'genre_Sci-Fi',
            'genre_Sport', 'genre_Thriller', 'genre_Western'
        ]
        column_order = [
            'budget', 'release_quarter', 'rating', 'is_sequel', 'runtime',
            'genre_Action', 'genre_Adventure', 'genre_Animation', 'genre_Biography', 'genre_Comedy',
            'genre_Crime', 'genre_Drama', 'genre_Family', 'genre_Fantasy', 'genre_Horror',
            'genre_Music', 'genre_Musical', 'genre_Mystery', 'genre_Romance', 'genre_Sci-Fi',
            'genre_Sport', 'genre_Thriller', 'genre_Western'
        ]

        # Apply preprocessing steps
        input_df = self.extract_release_quarter(input_df)
        input_df = self.ensure_numerical_features(input_df, numerical_features)
        input_df = self.scale_numerical_features(input_df, numerical_features, scaler)
        input_df = self.map_rating(input_df)
        input_df = self.one_hot_encode_genre(input_df)
        input_df = self.ensure_genre_columns(input_df, genre_columns)
        input_df = self.reorder_columns(input_df, column_order)

        # Return the preprocessed input
        return input_df

    def predict(self, input_data):
        preprocessed_data = self.preprocess_input(input_data)
        preprocessed_array = preprocessed_data.to_numpy() # Convert preprocessed data to a NumPy array
        prediction = self.model.predict(preprocessed_array)
        scaler = self.load_scaler()
        
        # Create a placeholder array with the same shape as the scaler's training data
        placeholder = np.zeros((1, scaler.n_features_in_))  # Ensure the array matches the scaler's input shape
        placeholder[0, 2] = prediction[0]  # Place the prediction in the 2nd position (index 2 for 'gross')
        unscaled_prediction = scaler.inverse_transform(placeholder)[0, 2]
        formatted_prediction = f"${round(unscaled_prediction):,}"     
        # Return the prediction as a dictionary
        return {"formatted": formatted_prediction, "raw": unscaled_prediction}
