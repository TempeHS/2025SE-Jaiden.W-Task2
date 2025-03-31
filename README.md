# Machine Learning Task

## 1. MLOps Design Phase

1. Defining the business problem to be solved

   - Universal Pictures, a leading film production company, faces challenges in accurately predicting movie revenue despite rising production costs. Traditional methods based on budget and star power often overlook key factors like genre trends and audience engagement, leading to inaccurate forecasts and poor investment decisions. To address this, Universal Pictures has commissioned me to develop a machine-learning model that predicts movie revenue using pre-production data. This model will help executives forecast earnings, optimize budgets, and assess project risks more effectively.

2. Refactoring the business problem into a machine learning problem

   - To build a supervised linear regression model that predicts a movie’s revenue using features like budget, genre, cast, and audience metrics. The model will learn patterns from historical movie data (1980–2020) to provide accurate revenue forecasts for future films.

3. Defining success metrics

   - Model generalises well to training, testing and new data.
   - Should be easily updatable with new movie data to adapt to changing industry trends.

4. Researching available data.

   - I have sourced a raw data set from [Kaggle](https://www.kaggle.com/). The data is saved in the CSV file [movies.csv](/2.Model_Development/2.1.Data_Wrangling/movies.csv).

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

## User Input
- actor
- director
- budget
- production company
- genre
- when released
- rating