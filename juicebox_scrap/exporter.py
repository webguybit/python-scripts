
import pandas as pd
import numpy as np
from db_util import getter_juice

def juice_comments():
    all_data = getter_juice()
    df = pd.DataFrame(all_data)
    df['amount'] = df['amount'].str.replace('Ξ', '')
    # print(df.head())
    df.to_excel('juice_comments_22DEC.xlsx', index=False)


juice_comments()

def read_save_csv():
    df = pd.read_csv('juice_comments_2.csv')
    # df.to_csv('juice_comments_3.csv', index=False)
    print(df.head())

# read_save_csv()
# Order #622566449287399
# Placed on 16 Dec 2021 11:14:50
# Never ever Recommended
# দুই প্যাকেট এসিআই সুরক্ষা জৈব সার অর্ডার করেছিলাম, এক প্যাকেট জৈব সার আর এক প্যাকেট রেডিমিক্স সয়েল পাঠায়ে দিছে। কাছাকাছি নামে শপ () ও একই প্রোডাক্টের(রিভিউ খারাপ থাকলে) নতুন পোস্ট এই শপের সততার বিষয়ে সন্দেহের উদ্রেকও করে।   