import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv('./iris.csv')
    df['sepal length in cm'].value_counts()
