
# csv loader

from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path='Social_Network_Ads.csv',
)

data = loader.load()

# print(f"CSV file data: {data}")

# print(f"Length of CSV file data: {len(data)}")

print(f"CSV file each data : {data[0]}")