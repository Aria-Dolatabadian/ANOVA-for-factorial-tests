import pandas as pd
df = pd.read_csv (r'factorial.csv')
print (df)
import statsmodels.api as sm
from statsmodels.formula.api import ols
formula= 'Yield ~C(Water)+ C(Nitrogen)+C(Water):C(Nitrogen)'
model=ols(formula,df).fit()
aov_table= sm.stats.anova_lm(model, typ=2)
print(aov_table)
