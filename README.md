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
The data in this study is scraped from Sky News, the Guardian and Google Trends by utilizing a selection of scraping procedures and API's from January 2022 and January 2023. The final data contains "ID", "article headlines", "date", "article tags", "Article text", "Article URL's", "Source", "Category", "Score" and "Average Score". the "Score" and "Average Score" is calculated by using data from Google trends for each tag contained in the datasets.

The final datasets [data_2022](data/processed/articles/2022_articles_processed.csv) and [data_2023](data/processed/articles/2023_articles_processed.csv) are located in [folder](data/processed/articles/) and can be reproduced by following the notebooks 1_data_collection and 2_data_processing located in [folder](notebooks). The subsequent analysis and reproduction of our results can then be recreated in the notebooks contained in 3_data_analysis and 4_data_visualization located in the [folder](notebooks). 



# First steps

## API keys

For the data collection from 'The Guardian' and 'Pytrends' we make use of the provided APIs. Therefore you need your own API keys. The API key for 'The Guardian' can be requested here (free developer version): https://bonobo.capi.gutools.co.uk/register/developer

The keys are stored in a .env file which can be created from the .env.sample file. The .env file should be placed in the root directory of the project. You can create the .env file with the following command:

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

- Change the path to the data in the notebooks depending on the location you choose for the data.

## Data visualization

To reconstruct our visualizations execute the following step:

1. Run [notebook](notebooks/4_data_visualization/visualizations.ipynb) generate all visualizations contained in the report.

Keep the following thing in mind:

- The notebook only contains the visualization for one category in the " Visualize the relationship between frequency of articles and popularity" section, to visualize all graphs represented in the appendix of the report - change the "Category" variable to your desired category and run the cell again.

The images of the figures located in the (report/figures) folder are manually saved from the [notebook](notebooks/4_data_visualization/visualizations.ipynb), reproducing these .png files requires manually storing them in the desired folder from the notebook.

# Repository overview

The following tree structure shows the files and folders within this repository. The main parts of the project are described in the [Get started](#get-started) section.

```
│   .env.sample
│   .gitignore
│   README.md
│
├───data
│   ├───interim
│   │   ├───annotated_articles
│   │   │   ├───automated_combined
│   │   │   │   ├───by_source
│   │   │   │   │   ├───guardian
│   │   │   │   │   │       2022_guardian_automated_annotated.csv
│   │   │   │   │   │       2023_guardian_automated_annotated.csv
│   │   │   │   │   │
│   │   │   │   │   └───skynews
│   │   │   │   │           2022_skynews_automated_annotated.csv
│   │   │   │   │           2023_skynews_automated_annotated.csv
│   │   │   │   │
│   │   │   │   └───by_year
│   │   │   │           2022_articles_automated_annotated.csv
│   │   │   │           2023_articles_automated_annotated.csv
│   │   │   │
│   │   │   ├───automated_raw
│   │   │   │   ├───guardian
│   │   │   │   │       2022_guardian_automated_annotated.csv
│   │   │   │   │       2022_guardian_automated_annotated_no_tags.csv
│   │   │   │   │       2023_guardian_automated_annotated.csv
│   │   │   │   │       2023_guardian_automated_annotated_no_tags.csv
│   │   │   │   │
│   │   │   │   └───skynews
│   │   │   │           2022_skynews_automated_annotated.csv
│   │   │   │           2022_skynews_automated_annotated_no_tags.csv
│   │   │   │           2023_skynews_automated_annotated.csv
│   │   │   │           2023_skynews_automated_annotated_no_tags.csv
│   │   │   │
│   │   │   └───manual
│   │   │       ├───2022
│   │   │       │       2022_manual_annotation_1.csv
│   │   │       │       2022_manual_annotation_2.csv
│   │   │       │       2022_manual_annotation_sample.csv
│   │   │       │
│   │   │       └───2023
│   │   │               2023_manual_annotation_1.csv
│   │   │               2023_manual_annotation_2.csv
│   │   │               2023_manual_annotation_sample.csv
│   │   │
│   │   ├───google_trends
│   │   │   │   2022_normalized_results.csv
│   │   │   │   2023_normalized_results.csv
│   │   │   │
│   │   │   ├───extra_google_trends_tags
│   │   │   │       2022_extra_google_trends_tags.csv
│   │   │   │       2023_extra_google_trends_tags.csv
│   │   │   │
│   │   │   └───missing_google_trends_tags
│   │   │           2022_missing_google_trends_tags.csv
│   │   │           2023_missung_google_trends_tags.csv
│   │   │
│   │   └───unique_tags
│   │           2022_unique_tags.csv
│   │           2023_unique_tags.csv
│   │
│   ├───processed
│   │   ├───articles
│   │   │       2022_articles_processed.csv
│   │   │       2023_articles_processed.csv
│   │   │
│   │   └───google_trends
│   │           2022_normalized_popularity.csv
│   │           2023_normalized_popularity.csv
│   │
│   └───raw
│       ├───articles
│       │   ├───bbc
│       │   │   │   2022_articles_bbc_raw.csv
│       │   │   │   2023_articles_bbc_raw.csv
│       │   │   │
│       │   │   └───cdx_results
│       │   │           2022_cdx_urls_bbc_results.csv
│       │   │           2023_cdx_urls_bbc_results.csv
│       │   │
│       │   ├───guardian
│       │   │       2022_articles_guardian_raw.csv
│       │   │       2023_articles_guardian_raw.csv
│       │   │
│       │   └───skynews
│       │       │   2022_articles_skynews_raw.csv
│       │       │   2023_articles_skynews_raw.csv
│       │       │
│       │       └───cdx_results
│       │               2022_cdx_urls_skynews_results.csv
│       │               2023_cdx_urls_skynews_results.csv
│       │
│       └───google_trends
│           ├───2022_google_trends_results
│           │       *_keywords.csv
│           │
│           └───2023_google_trends_results
│                   *_keywords.csv
│
├───notebooks
│   ├───1_data_collection
│   │   ├───articles
│   │   │       bbc_scraper.ipynb
│   │   │       guardian_api.ipynb
│   │   │       skynwes_scraper.ipynb
│   │   │
│   │   └───google_trends
│   │           get_google_trends_data.ipynb
│   │           initialize_google_trends_api.ipynb
│   │
│   ├───2_data_processing
│   │   ├───articles
│   │   │   │   draw_sample.ipynb
│   │   │   │
│   │   │   ├───annotation
│   │   │   │       gpt_annotation_batch.ipynb
│   │   │   │       gpt_annotation_single.ipynb
│   │   │   │
│   │   │   └───cleaning
│   │   │           add_id.ipynb
│   │   │           combine_data.ipynb
│   │   │           format_text_column.ipynb
│   │   │           remove_articles_without_tags.ipynb
│   │   │           sort_articles_by_date.ipynb
│   │   │           standardize_gpt_annotated_category.ipynb
│   │   │           standardize_time_format.ipynb
│   │   │
│   │   └───google_trends
│   │           check_google_trends_results.ipynb
│   │           normalize_google_trends_results.ipynb
│   │           transpose_normalized_google_trends_results.ipynb
│   │
│   ├───3_data_analysis
│   │       compare_annotation_accuracy.ipynb
│   │       get_google_trends_score.ipynb
│   │
│   └───4_data_visualization
│           visualizations.ipynb
│
└───report
    ├───paper.pdf
    └───figures
            articles_by_category_combined.png
            business_economy_frequency_interest_combined.png
            entertainment_culture_frequency_interest_combined.png
            environment_frequency_interest_combined.png
            Frequency_of_top_ten.png
            Guardian_skynews_count.png
            health_frequency_interest_combined.png
            politics_frequency_interest_combined.png
            science_technology_frequency_interest_combined.png
            sports_frequency_interest_combined.png
```
