from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.figure import Figure
import typing as tp
class YouTube:
    def __init__(self, path_to_df: str = "RUvideos_short.csv"):
        self.df = pd.read_csv(path_to_df)
        self.df['trending_date'] = pd.to_datetime(self.df['trending_date'],format="%y.%d.%m")
    def task1(self) -> pd.DataFrame:
        return self.df
    def task2(self) -> pd.DataFrame:
        df = self.df
        pr = df[['trending_date', 'category_id', 'views', 'likes', 'dislikes', 'comment_count']]
        pr['trending_date'] = df['trending_date'].dt.day
        return pr
    def task3(self) -> Figure:
        df=self.df
        sns.boxplot(x=df['trending_date'].dt.day,y=df['views']).set_title('BoxPlot distr')
        return plt.gcf()
    def task4(self) -> Figure:
        df=self.df
        sns.boxplot(x=df['trending_date'].dt.day,y=df['views'], showfliers = False).set_title('BoxPlot distr')
        return plt.gcf()
    def task5(self) -> Figure:
        df=self.df
        sns.jointplot(data = df,x=df['views'], y=df['likes']).fig.suptitle('JoinPlot distr')
        return plt.gcf()
    def task6(self) -> Figure:
        df=self.df
        pr_view=df.loc[df['views'] <= 4e5]
        pr_like=pr_view.loc[pr_view['likes'] <= 4e4]
        sns.jointplot(x=pr_like['views'], y=pr_like['likes']).fig.suptitle('JoinPlot distr')
        return plt.gcf()
