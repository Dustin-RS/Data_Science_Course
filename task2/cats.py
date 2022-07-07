import pandas as pd
import matplotlib.pyplot as plt
import typing as tp
from matplotlib.axes import Axes

class CatExam:
    def __init__(self, path_to_df: str = "cat_exam_data.csv"):
        self.df = pd.read_csv(path_to_df)

    def task1(self) -> pd.DataFrame:
        df = self.df
        return df.head()

    def task2(self) -> tp.List[str]:
        df = self.df
        return df.columns[df.isna().any()].tolist()

    def task3(self) -> pd.DataFrame:
        df = self.df
        self.df = df.dropna()
        return df.dropna()

    def task4(self) -> pd.DataFrame:
        df = self.df
        return df.describe()

    def task5(self) -> int:
        df = self.df
        return df.loc[df['test_score'] == 100].count()['number_of_students']
    
    def task6(self) -> pd.DataFrame:
        df = self.df
        pd = df.loc[df['test_score'] == 100].groupby(['school', 'number_of_students']).count().sort_values(
            by=['test_score', 'school'], ascending=False)
        pd_new = pd.rename(columns={'test_score': 'cnt_100'})
        return pd_new.reset_index()

    def task7(self) -> pd.DataFrame:
        df = self.df
        pr = df.groupby(['school']).mean().sort_values(by=['test_score'], ascending=False)
        return pr.reset_index().head(10)

    def task8(self) -> pd.DataFrame:
        df = self.df
        pr = df.groupby(['school']).mean().sort_values(by=['test_score'], ascending=False)
        return pr.reset_index().tail(10)

    def task9(self) -> Axes:
        df = self.df
        lit_school = df.loc[df['number_of_students'] <= 1000]
        big_school = df.loc[df['number_of_students'] > 1000]
        plt.hist(big_school['test_score'],bins=10, color='r', alpha=0.5)
        plt.hist(lit_school['test_score'],bins=10, alpha=0.5)
        plt.title('Test score distribution')
        plt.xlabel('test_score')
        plt.ylabel('number_of_students')
        plt.legend(['Big School', 'Small School'])
        return plt.gca()
