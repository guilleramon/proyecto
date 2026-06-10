import pandas as pd
import seaborn as sns

datos = pd.read_csv("titanic.csv")

g = sns.countplot(x = "Sex", hue = "Survived", data = datos)
g.figure.savefig("scripts/plot.png")

g = sns.countplot(x = "Sex", hue = "Pclass", data = datos)
g.figure.savefig("scripts/plot2.png")