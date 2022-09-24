import pandas as pd
from pandas_profiling import ProfileReport
from sklearn import datasets

#Getting data
wine_data = pd.DataFrame(datasets.load_wine().data)
wine_data.columns = datasets.load_wine().feature_names
wine_data.head(5)

# Generate a report of the data
profile = ProfileReport(wine_data)
profile.to_file(output_file = "export.html")