# Get Papers List

This Python project fetches research papers from the PubMed API based on a user-specified search query. It filters the results to identify papers where at least one author is affiliated with a pharmaceutical or biotech company. The filtered results are then saved in a CSV file.

## Features

- Fetches research papers from the PubMed API using the specified search query.
- Filters the papers based on author affiliations to identify pharmaceutical or biotech company ties.
- Outputs the filtered results into a CSV file with relevant details such as:
  - PubMed ID
  - Title of the paper
  - Publication date
  - Non-academic authors (if any)
  - Company affiliations of the authors
  - Corresponding author email

## Installation

### Option 1: **Using Poetry (Recommended)**

Poetry is used for managing dependencies in this project. To install dependencies, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/gundetinihal/get-papers-list.git
   cd get-papers-list
Install Poetry if you haven't already. If Poetry is not installed, follow the Poetry installation instructions.

Install the dependencies using Poetry:
poetry install

Once installed, you can run the program using Poetry's virtual environment.

Usage
After installing the required dependencies, you can use the program by running the following command from the project directory:
python get_papers_list.py "search query" -f output.csv

Command-Line Arguments:
"search query": The search term you want to use to fetch papers from PubMed (e.g., "cancer", "vaccines", "biotech").
-f output.csv: The file path where the output will be saved (e.g., output.csv). If you don't specify this flag, the results will be printed to the console.

Optional Flags:
-h or --help: Display usage instructions for the command-line interface.
-d or --debug: Print debug information during execution to help troubleshoot any issues.
License
This project is licensed under the MIT License.

Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request. Contributions are always welcome!

Tools and Libraries Used
PubMed API: Used to fetch research papers from the PubMed database.
Poetry: Dependency management tool used to handle project dependencies.
Requests: Library used for making HTTP requests to the PubMed API.
CSV: Built-in Python module for reading and writing CSV files.

