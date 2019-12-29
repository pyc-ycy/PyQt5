# PyCharm
# PyQt5
# SeabonTest
# 御承扬
# 2019/12/29
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame
from sklearn.datasets import load_iris

if __name__ == '__main__':
    iris = load_iris()
    df = DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    sns.set(color_codes=True)
    sns.distplot(df["petal length (cm)"], bins=15)
    plt.show()
