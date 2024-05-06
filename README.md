# Squirrel Census

## Introduction
Using squirrel-sighting data gathered in Central Park in 2018, this program sorts and simplifies the data to show us the number of squirrels seen with each fur color. This data is written to a new csv file, and to a MongoDB database.
More information about the data we're using can be found here: https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/about_data

## Installation
To run the squirrel census, follow these steps:

1. **Clone the repository:**
- git clone https://github.com/evanjamesc/squirrel-census.git
- cd squirrel-census
- Run "main.py" locally on your machine

## How to Use
- Change the client connection string if you would like the information written to your own database.
- Launch the application using the instructions above.
- You can see the raw data in the "2018_Central_Park_Squirrel_Census" csv file.
- Sorted data will be written to "squirrel_count.csv" and to a MongoDB database.

## Technologies Used
- Python 3, including the following libraries:
- Pandas
- Pymongo

## Contact
For more information, please contact Evan Christianson at evanjameschristianson@gmail.com
