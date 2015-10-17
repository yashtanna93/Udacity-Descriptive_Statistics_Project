import pandas
df = pandas.read_csv('dataset.csv', header=None)
x = -1.28 * df.std(ddof=False)[0] + df.mean()[0]
print('Range where one can expect approximately 90% of the draw values to fall : ' + str(int(x)) + ' to ' + str(df.max()[0]))