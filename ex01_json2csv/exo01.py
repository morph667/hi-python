import pandas as pd

df = pd.read_json (r'./ex01_json2csv/sample.json')
df.to_csv (r'./ex01_json2csv/file.csv', index = None)
