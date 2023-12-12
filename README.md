# Data in the Wild

This repository contains the code for the project for the course Data in the Wild: Wrangling and Visualising Data (Autumn 2023 - KSDWWVD1KU).

### Team Members:

Niclas Claßen (niclc@itu.dk), Marek Gala (galg@itu.dk), Manuel Knepper (mkne@itu.dk) & Steinar Slette(stsl@itu.dk)

---

# Get started

This project is split up into 4 main parts:

1. [Data collection](#data-collection)
2. [Data processing](#data-processing)
3. [Data analysis](#data-analysis)
4. [Data visualization](#data-visualization)

This README.md documents describes which files are responsible for what parts, and how to replicate our results. For a full project overview, see [Repository overview](#repository-overview).

---

# Results

TODO:

# First steps

## API keys

For the data collection from 'The Guardian' and 'Pytrends' we make use of the provided APIs. Therefore you need your own API keys. The keys are stored in a .env file which can be created from the .env.sample file. The .env file should be placed in the root directory of the project. You can create the .env file with the following command:

```
cp .env.sample .env
```

Then you can add your API keys to the .env file.

## Python environment

We use a virtual environment to run our code. To create the environment run the following command in the root directory of the project:

```
python3 -m venv .venv
source .venv/bin/activate

# You can deactivate the environment with:
source .venv/bin/deactivate
```

To install the required packages run:

```
pip install -r requirements.txt
```

# Data collection

The data collection can be split up into the following two parts:

1. [Collection of articles](#collection-of-articles)
2. [Collection of Google Trends](#collection-of-google-trends)

## Collection of articles

We collect data from different news sources and apply different methods which are described in the following sections.

### The Guardian

The Guardian provides an API to access their articles. If you followed the [First steps](#first-steps) you should have your API key in the .env file. To collect the data from The Guardian run the sections of the [notebook](notebooks/1_data_collection/articles/guardian_api.ipynb) top to bottom.

Keep following things in mind:

- The API has a limit of 500 requests per day. Therefore you might need to run the notebook multiple times.
- The date variables in the notebook are set to 2023-01-01 and 2023-01-31. You can change it to any date you want.
- The notebook saves the data in the same folder as the notebook. The data is saved in a csv file with the name 'YYYY-MM-DD_guardian.csv'.

### Sky News

Sky News does not provide an API or an archive. Therefore we use a web scraper for the Wayback Machine mainly based on the libraries Newspaper3k and Beautiful Soup. To collect the data from Sky News run the sections of the [notebook](notebooks/1_data_collection/articles/skynwes_scraper.ipynb) top to bottom.

Keep following things in mind:

- The date variables in the notebook can be changed to any date you want. The default values are set to 20230101 and 20230201.
- Add the correct path to your the local cache for the scraped results as mentioned in the notebook.
- The notebook saves the data in the same folder as the notebook. The data is saved in a csv file with the name '_timestamp_\_skynews_articles.csv'.
- The notebook also saves the failed scraping attempts in a csv file with the name '_timestamp_\_skynews_failed.csv'.

### BBC

For BBC we tried a similar approach as for Sky News. However, we were not able to scrape the articles from BBC with a satisfactory result. The main problem was that the articles are loaded dynamically. As reference and for future work we added the [notebook](notebooks/1_data_collection/articles/bbc_scraper.ipynb) to the repository.

## Google Trends

To get the Google Trends data we use the 'interest_over_time' method of the pytrends library. To collect the data from Google Trends run the sections of the following two notebooks top to bottom:

1. [Initialize pytrends](notebooks/1_data_collection/google_trends/initialize_google_trends_api.ipynb)
2. [Collect Google Trends data](notebooks/1_data_collection/google_trends/get_google_trends_data.ipynb)

## Keep following things in mind:

- To run this process we first need the data from the articles. Therefore you need to run the [Collection of articles](#collection-of-articles) first. You also need to change the path to the data in the notebook depending on the location you choose for the data of the articles.
- The date variables in the notebook [Collect Google Trends data](notebooks/1_data_collection/google_trends/get_google_trends_data.ipynb) can be changed to any date you want. The default values are set to 2023-01-01 and 2023-01-31.
- There might be some issues with the 429 error code. See the notebook [Initialize pytrends](notebooks/1_data_collection/google_trends/initialize_google_trends_api.ipynb) for more details.

# Repository overview

The following tree structure shows the files and folders, their purpose and their location within this repository. The main parts of the project are described in the [Get started](#get-started) section.

```

```
