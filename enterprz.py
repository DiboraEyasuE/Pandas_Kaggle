import pandas as pd

survey = pd.read_csv("enterprise.csv")
#print(survey.head())
print(survey.shape)
sliced = survey.iloc[-5:].notnull()
print(sliced)