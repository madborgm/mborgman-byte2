# Import libraries.
import csv
import httplib2
from apiclient.discovery import build
import urllib
import json
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


fp = open("data.json")
response = json.load(fp)

# Check how many rows we have.
print len(response['rows'])

data_df = pd.DataFrame(response[u'rows'], columns = response[u'columns'])

# Show a few rows.
data_df.head()