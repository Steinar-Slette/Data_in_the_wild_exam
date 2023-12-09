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


request_args = {
    "headers": {
        "authority": "trends.google.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en,sk-SK;q=0.9,sk;q=0.8,cs;q=0.7,en-US;q=0.6",
        "content-type": "application/json;charset=UTF-8",
        # 'cookie': '__utmc=10102256; __utmz=10102256.1700567728.5.3.utmcsr=trends.google.com^|utmccn=(referral)^|utmcmd=referral^|utmcct=/; __utma=10102256.1690297462.1699016378.1700567732.1700589318.7; __utmt=1; __utmb=10102256.5.9.1700589334188; CONSENT=PENDING+881; SOCS=CAISHAgCEhJnd3NfMjAyMzAyMTQtMF9SQzEaAnNrIAEaBgiA8MqfBg; SEARCH_SAMESITE=CgQIu5kB; OTZ=7278540_52_52_123900_48_436380; SID=dAhSdWG7aalkeKGgjjD7C-g51XmmpjUUzTy1Ph7oMdEEdBrPsGq6N5kXb4uE-W2xvECYiw.; __Secure-1PSID=dAhSdWG7aalkeKGgjjD7C-g51XmmpjUUzTy1Ph7oMdEEdBrPVr81QzHIEp7oN_iWwtumPQ.; __Secure-3PSID=dAhSdWG7aalkeKGgjjD7C-g51XmmpjUUzTy1Ph7oMdEEdBrPvvP2hpAbbLE9l9UjpRk9GA.; HSID=AfSglJfePb4qu_iEN; SSID=AwTD5h6LJydyqmYSs; APISID=RMlu3kIv3F6JoAwX/AjMPKsgBuCDMS9H0l; SAPISID=BiDKfuRNRpMNpmsg/AUnEDCM52mDRpHduR; __Secure-1PAPISID=BiDKfuRNRpMNpmsg/AUnEDCM52mDRpHduR; __Secure-3PAPISID=BiDKfuRNRpMNpmsg/AUnEDCM52mDRpHduR; 1P_JAR=2023-11-19-20; AEC=Ackid1Tq8Q7dBf__dy6Cv0xsYh4_-hFHNGZIoXEYytd_cfZggwG0i4YzKFw; _gid=GA1.3.483678575.1700567710; __Secure-1PSIDTS=sidts-CjEBNiGH7hYVQ9OszXk-UGeyiFD9AFUMHEoU3aSKvk1HNJip3gxQneqPs1PzE0PRkQuCEAA; __Secure-3PSIDTS=sidts-CjEBNiGH7hYVQ9OszXk-UGeyiFD9AFUMHEoU3aSKvk1HNJip3gxQneqPs1PzE0PRkQuCEAA; NID=511=NmfWsyb7jspepMM76DjOS_kCEYC_eTipxrMCDWpxUuSLW0BF8eeJoxUSs5xaUOoXVrokRmm_Ivlgibs1v5Vft2-u4KKuFf4MrQiz6GzdJjmVCZJM595c6xF76vICt4KHYw9BF1-vbVBMN-OV_vRtL5fkZnU9NDsfmT8AbT1WnV8uYPCbnrnMGZOJq55E_DgHy8Fp34YrTMtnmX9di1C1by32XaumOOg7MEjYTd7XUAjWd9IHh8oPZWmtzZbw8g3l3mtDwFTWJ60hb6lAKhfslWThfzVNPhWQkDca6BygcmhLAPuyAyppdO_xeSJSRGn3wheo9IGm_mz3n7wIm9uuXk-UpfKNhNYBBjSOrjYIVWUAy66awWC1RCE7sOndoBJh23xSjgNFW331vwv-FeVZXJT-UFDtotXNV0b7gqlHWdbdxNcaFrDVWetjn6HBrJGoUwqDcw2ACIQCPwGvFEDEKOTi2FPjvqgBPQ2EGkiAl595PNrE1et5fizvEJEDCvNwqG-zvNZpA1bxUWq5Bzs27cizsCLwupDxqHW6FgpjjbIpzdzAV2vQzrdytEn4NJUe-SZTDbw-n4MUA5aTaHlIa43bAc0LZfpSl2Viw30cOJ3C64skswZurl4Al0g1q2KL3z1-tSV_4f03fiSdctpK-3NuSt_T6AaQ06oFRhe7BfezxTQ9kAX5C4auqnWYTBklDOpubpJku3k0hmosM6vuq9drM-NY1MSLkS0yllOLq0EN8b5IV09oHEXfFx3B-4I15JEtUPKJBoqQgBaqQfYG5KPnClp4KP5POMKlUeer0p717qDRdP2DMJQdtPAvpn1iEC93dE6JLy9PtW_qoUVC8ISmyHoSZX-s_dS2kIZJKPomlxp7s0txf5H36pd941XOMa5gChZN1TXmQZRsRtehNgM; _ga=GA1.3.1690297462.1699016378; _gat_gtag_UA_4401283=1; SIDCC=ACA-OxOTj86dF9EexrmkXhfZ8T1bTpTihs3YmuWmoHTC5It2ujI7bHlhPTYH1C-uNPqCqUw1lqw; __Secure-1PSIDCC=ACA-OxP-kHVLG4-HY68QWOIuEgLkZka3JZrbXqf60UJB0UfK-ejfJbTmNTfZm-HtUkE-ZkB-rZw; __Secure-3PSIDCC=ACA-OxNoY2i-vA_3CuESjJdh8fMkZq2DW3luWG0UUb2yz47NtlG2_JBHlG-0cbaKqmh68NHmfEQ; _ga_VWZPXDNJJB=GS1.1.1700589220.9.1.1700589349.0.0.0',
        "origin": "https://trends.google.com",
        "referer": "https://trends.google.com/trends/explore?geo=DK&q=kokotina&hl=sk",
        "sec-ch-ua": "^\\^Chromium^^;v=^\\^118^^, ^\\^Opera^^;v=^\\^104^^, ^\\^Not=A?Brand^^;v=^\\^99^^",
        "sec-ch-ua-arch": "^\\^^^",
        "sec-ch-ua-bitness": "^\\^64^^",
        "sec-ch-ua-full-version": "^\\^104.0.4944.54^^",
        "sec-ch-ua-full-version-list": "^\\^Chromium^^;v=^\\^118.0.5993.118^^, ^\\^Opera^^;v=^\\^104.0.4944.54^^, ^\\^Not=A?Brand^^;v=^\\^99.0.0.0^^",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-model": "^\\^Nexus",
        "sec-ch-ua-platform": "^\\^Android^^",
        "sec-ch-ua-platform-version": "^\\^6.0^^",
        "sec-ch-ua-wow64": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36",
    }
}

req = TrendReq(timeout=(10, 25), retries=2, backoff_factor=0.1)


## First, we must determine an appropriate pre-defined element
# The method will combine two approaches:
# Approach 1 - We send 5 batches, one *arbitrary* element in each batch is pre-defined. We take median for each response (tag).
# We do this because we want to maintain consistency of relative scores when choosing our pre-defined element
# Approach 2 - We send 5 batches that contain independent elements
# We do this because we also want to reduce bias in case our arbitrary pre-defined element is heavily biased.
# We combine the 10 tags with their median value, and choose a median value from this set
def find_predefined_element(unique_elements, timeframe):
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
        time.sleep(0.5)
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
        time.sleep(5)
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
