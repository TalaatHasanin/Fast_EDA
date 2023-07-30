# Fast Exploratory Data Analysis (EDA) App


## Introduction
------------
The Fast Exploratory Data Analysis (EDA) App is a Python application that allows you to Explore your data files through EDA process. You can add your .csv files, and the application will explore your data based on the content of the documents. Please note that the app will change its state each time you change data settings.


## How It Works
------------
The application follows these steps to provide responses about your data:

1. CSV Loading: The app reads only one .csv document and converts it to a data frame.

2. Select Specific Columns: You can filter your data columns and run EDA process only on these columns.

3. Multiple Charts: The application provides you with plot settings such as {Boxplot, Lineplot, Histogram, and Scatterplot}.


## Dependencies and Installation
----------------------------
To install the Fast Exploratory Data Analysis (EDA) App, please follow these steps:

1. Clone the repository to your local machine.

2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```


## Usage
-----
To use the Fast Exploratory Data Analysis (EDA) App, follow these steps:

1. Ensure that you have installed the required dependencies.

2. Run the `app.py` file using the Streamlit CLI. Execute the following command:
   ```
   streamlit run app.py
   ```

3. The application will launch in your default web browser, displaying the user interface.

4. Load the .csv document into the app by following the provided instructions.

5. Click on 'Process' after you ensure about your data settings.


## Contributing
------------
This repository is intended for educational purposes and does not accept further contributions.


## License
-------
The Fast Exploratory Data Analysis (EDA) App is released under the [MIT License](https://opensource.org/licenses/MIT).
