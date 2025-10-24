import pandas as pd

survey = pd.read_csv("enterprise.csv")
#print(survey.head())
print(survey.shape)
sliced = survey.iloc[-5:].notnull()
survey.rename(columns={'industry_code_ANZSIC':'ind_cd_ANZSIC'})
print(survey['ind_cd_ANZSIC'])