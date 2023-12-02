import os
import time
from pytrends.request import TrendReq
import pandas as pd
import random
import statistics
import csv
from time import sleep
from random import randint
import calendar
import time


## First, we must determine an appropriate pre-defined element
# The method will combine two approaches:
# Approach 1 - We send 5 batches, one *arbitrary* element in each batch is pre-defined. We take median for each response (tag).
# We do this because we want to maintain consistency of relative scores when choosing our pre-defined element
# Approach 2 - We send 5 batches that contain independent elements
# We do this because we also want to reduce bias in case our arbitrary pre-defined element is heavily biased.
# We combine the 10 tags with their median value, and choose a median value from this set
def find_predefined_element(unique_elements, timeframe):
    req = TrendReq()
    final_dict = {}
    arbitrary_response = []
    independent_response = []
    arbitrary_median = []
    independent_median = []
    ## Just take the first 30 elements for testing
    unique_elements = unique_elements

    # TODO: why 20?
    sleep_counter = 0
    for i in range(1, 30 - 1, 4):
        print(i)
        batch = unique_elements[i : i + 4]
        print(batch)
        # Add the pre-defined element
        batch.append(unique_elements[0])
        req.build_payload(batch, geo="GB", timeframe=timeframe)
        ##Drop last column from the response
        # Last column is an unnecessary boolean

        response = req.interest_over_time()
        arbitrary_response.append(response.iloc[:, :-1])

        if sleep_counter == 5:
            sleep(randint(60, 75))
            sleep_counter = 0
        else:
            sleep(randint(16, 20))
            sleep_counter += 1

    averaged_response = get_average(arbitrary_response)
    arbitrary_median = get_median_dict(averaged_response)

    # Shuffle the array to send random elements
    random.shuffle(unique_elements)
    sleep(randint(40, 89))
    for i in range(0, 30 - 1, 5):
        batch = unique_elements[i : i + 5]
        print(i)
        print(batch)
        req.build_payload(batch, geo="GB", timeframe=timeframe)
        ##Drop last column from the response
        # Last column is an unnecessary boolean
        if sleep_counter == 5:
            sleep(randint(75, 89))
            sleep_counter = 0
        else:
            sleep(randint(8, 23))
            sleep_counter += 1
        response = req.interest_over_time()
        independent_response.append(response.iloc[:, :-1])

    averaged_response = get_average(independent_response)
    independent_median = get_median_dict(averaged_response)

    # Iterate over the union of keys from both dictionaries
    common_keys = arbitrary_median.keys() & independent_median.keys()
    print(common_keys)

    # It is possible that the keys in the two dictionaries will overlap
    # In that case, calculate the average of the medians for the key
    for k in common_keys:
        average_of_medians = (arbitrary_median[k] + independent_median[k]) / 2
        final_dict.update({k: average_of_medians})
        del arbitrary_median[k], independent_median[k]

    final_dict.update(arbitrary_median)
    final_dict.update(independent_median)

    median_value = statistics.median(final_dict.values())
    predefined_element = min(
        final_dict, key=lambda key: abs(final_dict[key] - median_value)
    )

    print(
        f"It seems that {predefined_element} is the most appropriate pre-defined element"
    )
    return predefined_element


def build_request(unique_elements, timeframe):
    sleep_counter = 0
    # Batch size is limited to 5 by Google Trends, 1st element is always pre-defined
    batch_size = 4
    req = TrendReq()
    output = []

    ## Just take the first 30 elements for testing
    unique_elements = unique_elements
    print("search")
    # predefined_element = find_predefined_element(unique_elements, timeframe)
    predefined_element = "air travel"
    print("find")
    unique_elements.remove(predefined_element)
    # Loop through the array in batches
    for i in range(48, len(unique_elements), batch_size):
        print(i)
        # Extract the batch of 4 elements
        batch = unique_elements[i : i + batch_size]
        # Add the pre-defined element
        batch.append(predefined_element)

        req.build_payload(batch, geo="GB", timeframe=timeframe)
        ##Drop last column from the response
        # Last column is an unnecessary boolean
        response = req.interest_over_time()

        current_GMT = time.gmtime()
        time_stamp = calendar.timegm(current_GMT)
        response.to_csv(f"{time_stamp}_keywords.csv", sep=";")

        output.append(response.iloc[:, :-1])

        # Wait a little so I don't overwhelm the API with requests
        sleep(randint(8, 15))
    # Returns an array of data frames, each with 5 tag columns and their score in time series
    return output


# We reshape the data by taking the average of the column for each tag
def get_average(api_results):
    results_average = []
    for analyzed_batch in api_results:
        analyzed = pd.DataFrame()
        # Skip the first column, as that is the date
        for column_name in analyzed_batch.columns:
            # As we have time series data, we get the average for the entire month for each column
            average_data = analyzed_batch[column_name].mean()
            analyzed[column_name] = pd.Series([average_data])
            # Convert DataFrame to a dictionary
        dict_data = analyzed.to_dict(orient="records")[0]
        results_average.append(dict_data)
    # Returns an array of dictionaries containing tag and its average
    return results_average


def get_median_dict(averaged_api_results):
    aux = []
    output = {}
    for dict in averaged_api_results:
        median_value = statistics.median(dict.values())
        closest_key = min(dict, key=lambda key: abs(dict[key] - median_value))
        aux.append({closest_key: dict[closest_key]})
    for dict in aux:
        output.update(dict)
    # Returns a dictionary containing tags and its medians
    return output


def normalize(averaged_api_results):
    aux = []
    normalized_dict = {}
    aux.append(averaged_api_results[0])
    for i in range(1, len(averaged_api_results)):
        # We get the pre-defined element from each dictionary (the last element)
        # It is possible that we divide by 0 here
        # In that case, it is clear that our pre-defined element was hugely relatively unpopular
        # This means that we can just divide each tag value by 1 (having no effect)
        value_to_normalize = list(averaged_api_results[i].values())[-1]
        value_to_normalize = 1 if value_to_normalize == 0 else value_to_normalize
        normalization_factor = (
            list(averaged_api_results[0].values())[-1] / value_to_normalize
        )
        averaged_api_results[i] = {
            key: value * normalization_factor
            for key, value in averaged_api_results[i].items()
        }
        aux.append(averaged_api_results[i])
    for dict in aux:
        normalized_dict.update(dict)
    return normalized_dict


def build_csv(normalized_dict):
    # Specify the file path
    subfolder = "google_trends_api"
    csv_file_name = "google_trends_popularity.csv"
    csv_file_path = os.path.join(subfolder, csv_file_name)

    # Write the dictionary to a CSV file
    with open(csv_file_path, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write header
        csv_writer.writerow(["tag_name", "relative_popularity"])

        # Write data
        for tag_name, relative_popularity in normalized_dict.items():
            csv_writer.writerow([tag_name, relative_popularity])
