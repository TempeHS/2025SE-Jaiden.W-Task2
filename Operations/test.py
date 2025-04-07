from model import MLModel

# Initialize the MLModel with no model initially
MLmodel = MLModel(model=None)

# Load the saved model
MLmodel.load_model("../Model_Testing_and_Validation/my_saved_model_v1.sav")

# Example user input data
user_input = {
    "budget": 19000000,
    "release_date": "2025-04-07",
    "rating": "PG-13",
    "is_sequel": 1,
    "runtime": 120,
    "genre": "Action"
}

# Preprocess the input data
prediction = MLmodel.predict(user_input)

# Print the preprocessed data to verify
print(prediction)