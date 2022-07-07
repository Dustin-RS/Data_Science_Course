import json
import typing as tp

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime
from matplotlib.figure import Figure
class YouTube2:
    def __init__( # task0
        self,
        trends_df_path: str="RUvideos_short.csv",
        categories_df_path: str="RU_category_id.json"
    ):
        self.trends_df = pd.read_csv(trends_df_path)
        self.trends_df['trending_date'] = pd.to_datetime(self.trends_df['trending_date'],format="%y.%d.%m")
        
        with open(categories_df_path) as json_file:
              json_data = json.load(json_file)
          
        self.categories_df = pd.DataFrame(columns=['id', 'name'])

        for item in json_data['items']:
              self.categories_df = self.categories_df.append(
                  {'id': int(item['id']),
                  'name': item['snippet']['title']},
                  ignore_index=True
              )
          
        self.categories_df['id'] = self.categories_df['id'].astype(int)
    
    def task1(self) -> pd.DataFrame:
        self.merged_df = self.trends_df.merge(self.categories_df,left_on='category_id',right_on='id')
        return self.merged_df
    def task2(self) -> pd.DataFrame:
        df = self.merged_df
        table = pd.pivot_table(df, index='name', values='views', columns=['trending_date'], aggfunc=np.sum)
        return table
    def task3(self) -> Figure:
        df = self.merged_df.copy()
        df['views'] = df['views'].div(1e6)
        table = pd.pivot_table(df, index='name', values='views', columns=['trending_date'], aggfunc=np.sum)
        sns.heatmap(table, annot=True).set_title('Category')
        return plt.gcf()
    def task4(self) -> pd.DataFrame:
        df = self.merged_df
        table = pd.pivot_table(df, index='name', values='views', columns=['trending_date'], aggfunc=np.sum, margins_name='Всего просмотров', margins=True)
        return table
    def task5(self) -> pd.DataFrame:
        df = self.merged_df.copy()
        df['views'] = df['views'].div(1e6)
        table = pd.pivot_table(df, index='name', values='views', columns=['trending_date'], aggfunc=np.sum, margins_name='Всего просмотров', margins=True)
        sns.heatmap(table, annot=True,vmax=3).set_title('Category')
        return plt.gcf()
