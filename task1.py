import pandas
import matplotlib.pyplot as plt
cards = list(range(1, 11)) + [10, 10, 10]
cards = cards * 4
df = pandas.DataFrame(data = cards)
plt.figure()
ax = df.plot(kind='hist', bins=10, legend=False)
ax.set_xlabel('Value of cards')
ax.set_ylabel('Number of cards')