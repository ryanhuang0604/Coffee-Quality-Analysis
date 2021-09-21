import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import missingno as msno

data = pd.read_csv('./arabica.csv')
data.dataframeName = 'arabica.csv'

data.head()
data.info()
msno.matrix(data)

def plotCorrelationMatrix(df, graphWidth):
	filename = df.dataframeName
	df = df.dropna('columns') # drop columns with NaN
	df = df[[col for col in df if df[col].nunique() > 1]] # keep columns where there are more than 1 unique values
	if df.shape[1] < 2:
		print(f'No correlation plots shown: The number of non-NaN or constant columns ({df.shape[1]}) is less than 2')
	df = df[['Aroma', 'Flavor', 'Aftertaste', 'Acidity', 'Body', 'Balance', 'Uniformity', 'Clean.Cup', 'Sweetness', 'Cupper.Points', 'Total.Cup.Points']]
	corr = df.corr()
	plt.figure(num=None, figsize=(graphWidth, graphWidth), dpi=80, facecolor='w', edgecolor='k')
	corrMat = plt.matshow(corr, fignum = 1)
	plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
	plt.yticks(range(len(corr.columns)), corr.columns)
	plt.gca().xaxis.tick_bottom()
	plt.colorbar(corrMat)
	plt.title(f'Correlation Matrix for {filename}', fontsize=15)
	plt.show()

plotCorrelationMatrix(data, 8)