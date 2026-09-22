import urllib.request

URL = "https://raw.githubusercontent.com/eli5-org/eli5/master/notebooks/titanic-train.csv"
OUTPUT = "titanic.csv"

print("Downloading Titanic training dataset...")
urllib.request.urlretrieve(URL, OUTPUT)
print("Downloaded:", OUTPUT)
