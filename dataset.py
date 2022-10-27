import pandas as pd
numbers = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
sentences = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
videos = pd.read_csv("CAvideos.csv")
videos.shape
videos.head()
