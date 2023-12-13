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

The final datasets [data_2022](data/processed/articles/2022_articles_processed.csv) and [data_2023](data/processed/articles/2023_articles_processed.csv) are located in the [folder](data/processed/articles/) and can be reproduced by following the notebooks 1_data_collection and 2_data_processing located in the [folder](notebooks). The subsequent analysis and reproduction of our results can then be recreated in the notebooks contained in 3_data_analysis and 4_data_visualization located in the [folder](notebooks). 

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

Keep the following things in mind:

- The API has a limit of 500 requests per day. Therefore you might need to run the notebook multiple times.
- The date variables in the notebook are set to 2023-01-01 and 2023-01-31. You can change it to any date you want.
- The notebook saves the data in the same folder as the notebook. The data is saved in a csv file with the name 'YYYY-MM-DD_guardian.csv'.

### Sky News

Sky News does not provide an API or an archive. Therefore we use a web scraper for the Wayback Machine mainly based on the libraries Newspaper3k and Beautiful Soup. To collect the data from Sky News run the sections of the [notebook](notebooks/1_data_collection/articles/skynwes_scraper.ipynb) top to bottom.

Keep the following things in mind:

- The date variables in the notebook can be changed to any date you want. The default values are set to 20230101 and 20230201.
- Add the correct path to your the local cache for the scraped results as mentioned in the notebook.
- The notebook saves the data in the same folder as the notebook. The data is saved in a csv file with the name '_timestamp_\_skynews_articles.csv'.
- The notebook also saves the failed scraping attempts in a csv file with the name '_timestamp_\_skynews_failed.csv'.

### BBC

For BBC we tried a similar approach as for Sky News. However, we were not able to scrape the articles from BBC with a satisfactory result. The main problem was that the articles are loaded dynamically. As reference and for future work we added the [notebook](notebooks/1_data_collection/articles/bbc_scraper.ipynb) to the repository.

## Collection of Google Trends

To get the Google Trends data we use the 'interest_over_time' method of the pytrends library. To collect the data from Google Trends run the sections of the following two notebooks top to bottom:

1. [Initialize pytrends](notebooks/1_data_collection/google_trends/initialize_google_trends_api.ipynb)
2. [Collect Google Trends data](notebooks/1_data_collection/google_trends/get_google_trends_data.ipynb)

## Keep the following things in mind:

- To run this process we first need the data from the articles. Therefore you need to run the [Collection of articles](#collection-of-articles) first. You also need to change the path to the data in the notebook depending on the location you choose for the data of the articles.
- The date variables in the notebook [Collect Google Trends data](notebooks/1_data_collection/google_trends/get_google_trends_data.ipynb) can be changed to any date you want. The default values are set to 2023-01-01 and 2023-01-31.
- There might be some issues with the 429 error code. See the notebook [Initialize pytrends](notebooks/1_data_collection/google_trends/initialize_google_trends_api.ipynb) for more details.

## Data processing

After collecting the data we need to process it. The data processing can be split up into the following two parts:

1. [Processing of articles](#processing-of-articles)
2. [Processing of Google Trends](#processing-of-google-trends)

### Processing of articles

The processing of the articles can itself be split up into the following two parts which are not necessarily dependent on each other:

1. [Annotation](#annotation)
2. [Cleaning](#cleaning)

#### Annotation

As part of our analysis we want to classify the topic of the collected articles into the following categories by looking at their headlines and tags:

- Politics
- Business and Economy
- Environment
- Sports
- Entertainment and Culture
- Science and Technology
- Health

Before we can start with we have to clean and process the collected articles as described in the following steps.

1. Run the [notebook](notebooks/2_data_processing/articles/cleaning/standardize_time_format.ipynb) to standardize the time format of the articles and filter out articles without or wrong dates.
2. Run the [notebook](notebooks/2_data_processing/articles/cleaning/remove_articles_without_tags.ipynb) to remove articles without tags.
3. Run the [notebook](notebooks/2_data_processing/articles/cleaning/combine_data.ipynbipynb) to combine the data from the different sources. We used it to combine the data from The Guardian and Sky News for each year.
4. Run the [notebook](notebooks/2_data_processing/articles/cleaning/format_text_column.ipynb) to format the text column of the articles.

Keep the following things in mind:

- For all the steps mentioned above you should change the path to the data in the notebook depending on the location you choose for the data of the articles.

##### Manual annotation

The manual annotation of the articles is done to get a better understanding of the data and estimate the accuracy of the automatic annotation. To draw a random sample of the articles for the manual annotation run the [notebook](notebooks/2_data_processing/articles/draw_sample.ipynb) top to bottom.

Keep the following things in mind:

- Change the path to the data in the notebook depending on the location you choose for the data of the articles.
- The notebook saves the data in the same folder as the notebook. The data is saved in a csv file with the name you define as output path.

##### Automatic annotation

The automatic annotation of the articles is done with the help of the openAI API. At this pont you should have your API key in the .env file and followed the steps as mentioned under [Annotation].

For the automatic annotation we tried two different approaches:

1. Annotation of the articles in batches [notebook](notebooks/2_data_processing/articles/annotation/gpt_annotation_batch.ipynb)
2. Annotation of the articles one by one [notebook](notebooks/2_data_processing/articles/annotation/gpt_annotation_single.ipynb)

We started with the annotation of the articles in batches due to API limitations. However, we were not satisfying with the results. One reason for this is that for some batches not all articles were annotated. Furthermore, sometimes a different as the defined category was annotated. Therefore we switched to the annotation of the articles one by one.

To run the automatic one by one annotation of the articles run the [notebook](notebooks/2_data_processing/articles/annotation/gpt_annotation_single.ipynb) top to bottom.

Keep the following thing in mind:

- Depending on your API limits you might need to run the notebook multiple times and decrease the number of requests.

#### Cleaning

After running the automatic annotation we need to clean Category column. To do that run the [notebook](notebooks/2_data_processing/articles/cleaning/standardize_gpt_annotated_category.ipynb) top to bottom.

Keep the following thing in mind:

- Change the path to the data in the notebook depending on the location you choose for the data of the articles.

### Processing of Google Trends

The processing of the Google Trends data can itself be split up into the following three parts:

1. Run [notebook](notebooks/2_data_processing/google_trends/check_google_trends_results.ipynb.ipynb) see if data is missing.
2. Run [notebook](notebooks/2_data_processing/google_trends/normalize_google_trends_results.ipynb) to normalize the data.
3. Run [notebook](notebooks/2_data_processing/google_trends/transpose_normalized_google_trends_results.ipynb) to transpose the data.

Keep the following thing in mind:

- Change the path to the data in the notebook depending on the location you choose for the data of the google trends results.

## Data analysis

To get started with analysis execute these two steps: (step 1 is optional, step 2 is required)
1. Run [notebook](notebooks/3_data_analysis/compare_annotation_accuracy.ipynb) get the accuracy of the manual and automatic annotations.
2. Run [notebook](notebooks/3_data_analysis/get_google_trends_score.ipynb) calculate the score and average score of each article based on the google trends data. 

Keep the following thing in mind:

- Change the path to the data in the notebook depending on the location you choose for the data of the google trends results.

## Visualization

To reconstruct our visualizations execute the following step:
1. Run [notebook](notebooks/4_data_visualization/visualizations.ipynb) generate all visualizations contained in the report. 

Keep the following thing in mind:

- The notebook only contains the visualization for one category in the " Visualize the relationship between frequency of articles and popularity" section, to visualize all graphs represented in the appendix of the report - change the "Category" variable to your desired category and run the cell again. 

## plots

The images of the plots located in the (report/plots) folder are manually saved from the [notebook](notebooks/4_data_visualization/visualizations.ipynb), reproducing these .png files requires manually storing them in the desired folder from the notebook.


# Repository overview

The following tree structure shows the files and folders, their purpose and their location within this repository. The main parts of the project are described in the [Get started](#get-started) section.

```

```
