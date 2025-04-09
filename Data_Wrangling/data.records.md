# Data Records

Recordings of all scaling/encoding processes applied during data wrangling and feature engineering or the approach taken to engineering new features or feature interactions.

## Scalled Data

| Data    | Min/Max                     | Scale Min/Max |
| ------- | --------------------------- | ------------- |
| budget  | 3.000000e+03 / 3.560000e+08 | 0 / 1         |
| gross   | 3.090000e+02 / 2.847246e+09 | 0 / 1         |
| runtime | 63 / 366                    | 0 / 1         |
| votes   | 3.500000e+01 / 2.400000e+06 | 0 / 1         |

## Encoded Data

| Data     | Unencoded                                                                                                                                                                                                                                                                                  | Encoded                                                                                                      |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| rating   | 'G', 'TV-PG', 'PG', 'Approved', 'Unrated', 'Not Rated', 'PG-13', 'TV-14', 'R', 'TV-MA', 'NC-17', 'X'                                                                                                                                                                                       | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11                                                                         |
| genre    | <li>Action</li><li>Adventure</li><li>Animation</li><li>Biography</li><li>Comedy</li><li>Crime</li><li>Drama</li><li>Family</li><li>Fantasy</li><li>Horror</li><li>Music</li><li>Musical</li><li>Mystery</li><li>Romance</li><li>Sci-Fi</li><li>Sport</li><li>Thriller</li><li>Western</li> | True/False                                                                                                   |
| company  | Paramount Pictures                                                                                                                                                                                                                                                                         | Frequency encoding, calculating each unique evalue then mapping those frequencies back to the original data. |
| country  | Australia                                                                                                                                                                                                                                                                                  | Frequency encoding, calculating each unique evalue then mapping those frequencies back to the original data. |
| released | June 13, 1980                                                                                                                                                                                                                                                                              | 1980-06-13                                                                                                   |

## Engineered Features

| Data            | Engineering                                                                                                    |
| --------------- | -------------------------------------------------------------------------------------------------------------- |
| release_quarter | `data_frame['release_quarter'] = pd.to_datetime(data_frame['released']).dt.quarter`                            |
| release_month   | `data_frame['release_month'] = pd.to_datetime(data_frame['released']).dt.month`                                |
| is_sequel       | `data_frame['name'].str.contains(r'\b(?:2&#124;3&#124;4&#124;II&#124;III&#124;IV)\b', regex=True).astype(int)` |
