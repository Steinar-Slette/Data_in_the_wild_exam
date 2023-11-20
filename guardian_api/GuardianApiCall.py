import requests
import json

#specify parameters for API Call to make customization easier
api_endpoint = 'https://content.guardianapis.com/search'
api_key = '893fdc44-1c2b-4683-9bef-b550ed0b6b51'
from_date = '2023-01-01'
to_date = '2023-01-31'
page_size = '50'
max_number_of_pages = 120

for i in range (1,  max_number_of_pages):
        response = requests.get(api_endpoint,
                                params={'api-key': api_key,
                                        'from-date': from_date,
                                        'to-date': to_date,
                                        'page-size': page_size,
                                        'type': 'article',
                                        'show-blocks': 'body',
                                        'show-tags': 'all',
                                        'page': i})

        file_name = "2023_response_page%d.json" % i
        with open(file_name, "w") as write_file:
                json.dump(response.json(), write_file)