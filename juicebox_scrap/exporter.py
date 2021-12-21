
import pandas as pd
import numpy as np
from db_util import getter_juice

def juice_comments():
    all_data = getter_juice()
    df = pd.DataFrame(all_data)
    df['amount'] = df['amount'].str.replace('Ξ', '')
    # print(df.head())
    df.to_csv('juice_comments.csv', index=False)


# juice_comments()