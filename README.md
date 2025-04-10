# Machine Learning Task

## 1. MLOps Design Phase

### 1.1 Defining the business problem to be solved

- Universal Pictures, a leading film production company, faces challenges in accurately predicting movie revenue despite rising production costs. To address this, Universal Pictures has commissioned me to develop a machine-learning model that predicts movie revenue using pre-production data. This model will help executives forecast earnings, optimize budgets, and assess project risks more effectively.

### 1.2 Refactoring the business problem into a machine learning problem

- To build a supervised linear regression model that predicts a movie’s revenue using features like budget, genre, cast, and audience metrics. The model will learn patterns from historical movie data (1980–2020) to provide accurate revenue forecasts for future films.

### 1.3 Defining success metrics

- Model generalises well to training, testing and new data.
- Should be easily updatable with new movie data to adapt to changing industry trends.

### 1.4 Researching available data.

- I have sourced a raw data set from [Kaggle](https://www.kaggle.com/). The data is saved in the CSV file [movies.csv](/Data_Wrangling/movies.csv).

- The data columns are:

  | Column   | Data                                                                           |
  | -------- | ------------------------------------------------------------------------------ |
  | name     | The title of the movie.                                                        |
  | rating   | The movie's age rating (e.g., PG, R).                                          |
  | genre    | The primary genre of the movie (e.g., action, drama).                          |
  | released | The release date of the movie in the United States (in YYYY-MM-DD format).     |
  | score    | The IMDb user rating (typically on a scale from 0 to 10).                      |
  | votes    | The number of user votes the movie received on IMDb.                           |
  | director | The director of the movie.                                                     |
  | star     | The main actor/actress of the movie                                            |
  | writer   | The primary scriptwriter(s) for the movie.                                     |
  | country  | The country where the movie was produced.                                      |
  | budget   | The production cost of the movie (in USD).                                     |
  | gross    | The total revenue earned by the movie (in USD). (Target variable for my model) |
  | company  | The production company responsible for making the movie.                       |
  | runtime  | The duration of the movie (in minutes).                                        |

## 2. MLOps Model Development Phase

### 2.1 Data Wrangling

- The [Data Preview Jupiter Notebook](/Data_Wrangling/data_preview.ipynb) provides a better overciew and understanding of the dataset using snapshots, data summaries, graphs and descriptive statistics.
- The [Data Wrangling Jupiter Notebook](/Data_Wrangling/data_wrangling.ipynb) shows my data wrangling processes using the Pandas library and Matplotlib.
- The [Data Records Jupiter Notebook](/Data_Wrangling/data.records.md) contains documentation of all scaling and encoding steps performed during data wrangling and feature engineering, including the methods used to create new features or model feature interactions.

### 2.2 Feature Engineering

- The [Feature Engineering Jupiter Notebook](/Feature_Engineering/feature_engineering.ipynb) shows how I've feature engineered my dataset by creating new features or modifying existing ones to improve model performance.

### 2.3 Model Training

- The [Spliting Training and Testing Data Jupiter Notebook](Model_Training/split_training_and_testing_data.ipynb) shows how I've divided the real-world dataset into two parts: the training set for model training and the testing set for model evaluation.
- The [Linear Regression Jupiter Notebook](Model_Training/linear_regression.ipynb) demonstrates how I trained a linear regression model using the engineered features to predict the gross revenue based on various factors.

### 2.4 Model Testing and Validation

- The [Model Testing and Validation Jupiter Notebook](Model_Testing_and_Validation/model_evaluation.ipynb) shows the way I've evaluated, tested and validated my model using a second set of test data to refine my model.

## 3. MLOps Operations Phase

### How to use my model

#### Running required files

```bash
cd Operations
python main.py
```

```bash
cd Operations
python api.py
```
