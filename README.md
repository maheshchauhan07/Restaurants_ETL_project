# Restaurant Data Analytics ETL Project

This project showcases the process of Extract, Transform, and Load (ETL) for restaurant data collected from TripAdvisor.com. It employs various technologies such as Google Cloud VM Instances, Google BigQuery, Looker Studio, and Mage Data Pipeline software to perform data analytics and visualization.

## Table of Contents

- [Introduction](#introduction)
- [Data Collection](#data-collection)
- [ETL Process](#etl-process)
- [Technologies Used](#technologies-used)
- [Data Schema](#data-schema)
- [Analytics and Visualization](#analytics-and-visualization)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project focuses on analyzing restaurant data to derive meaningful insights that can aid decision-making processes in the food industry. It demonstrates the entire ETL pipeline, from data collection to visualization, using real-world data obtained from TripAdvisor.com.

## Data Collection

Data for this project was collected by scraping restaurant information from TripAdvisor.com using Python and Beautiful Soup. The scraped data includes restaurant names, locations, ratings, reviews, and other relevant details.

## ETL Process

The ETL process consists of three main steps:

1. **Extract**: Data is extracted from the web using web scraping techniques and stored in a structured format.

2. **Transform**: The extracted data undergoes transformations to clean, format, and enrich it. This includes data validation, handling missing values, and creating a consistent data structure.

3. **Load**: The transformed data is loaded into Google BigQuery, a cloud-based data warehousing platform, for efficient storage and querying.

## Technologies Used

- **Google Cloud VM Instances**: Virtual machines were used for web scraping, data preprocessing, and ETL tasks.

- **Google BigQuery**: A powerful data warehousing platform used for storing and querying the restaurant data.

- **Looker Studio**: A data visualization and business intelligence tool used to create interactive dashboards and reports.

- **Mage Data Pipeline Software**: A data pipeline software used to automate ETL processes.

## Data Schema

The schema for the data in Google BigQuery is as follows:

- `restaurant_id` (INT64): A unique identifier for each restaurant.
- `name` (STRING): The name of the restaurant.
- `address` (STRING): The address of the restaurant.
- `City` (STRING): The city where the restaurant is located.
- `Country` (STRING): The country where the restaurant is situated.
- `reviews` (INT64): The total number of reviews for the restaurant.
- `rating` (FLOAT64): The average rating of the restaurant.
- `food` (FLOAT64): The rating for food quality (out of 5).
- `service` (FLOAT64): The rating for service quality (out of 5).
- `value` (FLOAT64): The rating for value for money (out of 5).
- `atmosphere` (FLOAT64): The rating for restaurant atmosphere (out of 5).
- `Telephone` (STRING): The telephone number of the restaurant.
- `Typology` (STRING): The type of the restaurant (e.g., fine dining, casual).
- `Pricing` (STRING): The pricing category of the restaurant.
- `About` (STRING): Information about the restaurant.
- `Latitude` (FLOAT64): The latitude coordinate of the restaurant's location.
- `Longitude` (FLOAT64): The longitude coordinate of the restaurant's location.
- `price_range` (STRING): The price range of the restaurant (e.g., $, $$, $$$).
- `min_price` (FLOAT64): The minimum price range value.
- `max_price` (FLOAT64): The maximum price range value.
- `Average_price` (FLOAT64): The average price range value.
- `cuisines` (STRING): The types of cuisines offered by the restaurant.
- `Dietary` (STRING): Dietary information about the restaurant's menu.
- `Features` (STRING): Special features of the restaurant.

## Analytics and Visualization

The project includes sample Looker Studio dashboards and reports for visualizing restaurant data, including ratings for food, service, value, and atmosphere. These visualizations can help users understand the quality of restaurants in various aspects.

## Contributing

Contributions to this project are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE.md).
