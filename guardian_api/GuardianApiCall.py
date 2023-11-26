import requests
import json
import pandas as pd

#specify parameters for API Call to make customization easier
api_endpoint = 'https://content.guardianapis.com/search'
api_key = 'your_api_key_should_be_here'
from_date = '2023-01-01'
to_date = '2023-01-31'
page_size = '50'
max_number_of_pages = 120


#data structures for storing response data
article_title = str()
article_date = str()
article_text = str()
article_url = str()
article_authors = []
article_keywords = []
collection_of_responses = []



for i in range (1,  max_number_of_pages):
    response = requests.get(api_endpoint,
                            params={'api-key': api_key,
                                    'from-date': from_date,
                                    'to-date': to_date,
                                    'page-size': page_size,
                                    'type': 'article',
                                    'show-blocks': 'body',
                                    'show-tags': 'keyword,contributor',
                                    'page': i})
    for k in range(50):
        try:
            json_response = json.loads(response.content.decode('utf8'))
            article_title = json_response['response']['results'][k]['webTitle']
            article_date = json_response['response']['results'][k]['webPublicationDate']
            article_text = json_response['response']['results'][k]['blocks']['body'][0]['bodyTextSummary']
            article_url = json_response['response']['results'][k]['webUrl']
        except IndexError:
            break
        for j in range(50):
            try:
                if json_response['response']['results'][k]['tags'][j]['type'] == "keyword":
                    article_keywords.append(json_response['response']['results'][k]['tags'][j]['webTitle'])
                elif json_response['response']['results'][k]['tags'][j]['type'] == "contributor":
                    article_authors.append(json_response['response']['results'][k]['tags'][j]['webTitle'])
            except IndexError:
                break

        #clean data for authors and keywords
        if not article_authors:
            article_authors.append("N/A")
        if not article_keywords:
            article_keywords.append("N/A")

        collection_of_responses.append([article_title,
                                        article_date,
                                        article_authors,
                                        article_keywords,
                                        article_text,
                                        article_url])

        #reset authors and keywords for next iteration
        article_authors = []
        article_keywords = []


api_responses_df = pd.DataFrame(collection_of_responses, columns=["Title", "Date", "Authors", "Tags", "Text", "Url"])
api_responses_df.to_csv(f'{to_date}_guardian.csv', sep=';')
