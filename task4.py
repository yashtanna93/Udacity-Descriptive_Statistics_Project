import pandas
import matplotlib.pyplot as plt
df = pandas.read_csv('dataset.csv', header=None)
plt.figure()
ax = df.plot(kind='hist', bins=13, legend=False)
ax.set_xlabel('Sampled Card Sums') 
ax.set_ylabel('Frequency of Sampled Card Sums')