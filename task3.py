import pandas
import numpy as np
df = pandas.read_csv('dataset.csv', header=None)
print('Measure of Central Tendancy are:')
print('Mean   : ' + str(df.mean()[0]))
print('Median : ' + str(df.median()[0]))
print('Mode   : ' + str(df.mode()[0][0]))
print('\nMeasure of Variability are:')
print('Range               : ' + str(df.max()[0] - df.min()[0]))
print('Interquartile Range : ' + str(np.percentile(df, 75) - np.percentile(df, 25)))
print('Variance            : ' + str(df.var(ddof=False)[0]))
print('Standard Deviation  : ' + str(df.std(ddof=False)[0]))