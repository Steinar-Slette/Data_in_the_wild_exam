from trends import *    
import ast

#Read the csv file
file_path = './skyNews/1699917947_articles.csv'
df = pd.read_csv(file_path, sep=';')

#When csv is loaded, the Tags array is recognized as a string, this casts it to an array
df['Tags'] = df['Tags'].apply(ast.literal_eval)

#Get unique tags
unique_tags = []
for tags in (df['Tags']):
    for element in tags:
        if element not in unique_tags:
            unique_tags.append(element)


results = build_request(unique_tags, '2022-01-01 2022-01-31')
results = get_average(results)
results = normalize(results)
build_csv(results)