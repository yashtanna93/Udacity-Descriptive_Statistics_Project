
# coding: utf-8

# # Descriptive Statistics Project

# The following experiment is carried of with the use of a standard deck of playing cards. This is a deck of fifty-two cards divided into four suits (spades (♠), hearts (♥), diamonds (♦), and clubs (♣)), each suit containing thirteen cards (Ace, numbers 2-10, and face cards Jack, Queen, and King). For the purposes of this task, each card is assigned a value: The Ace takes a value of 1, numbered cards take the value printed on the card, and the Jack, Queen, and King each take a value of 10.

# In[1]:

import random
import pandas
cards = list(range(1, 11)) + [10, 10, 10]
cards = cards * 4
dataset_size = 0
dataset = []
while(dataset_size<1000):
    dataset.append(sum(random.sample(cards, 3)))
    dataset_size+=1
df = pandas.DataFrame(data = dataset)
df.to_csv('dataset.csv', index=False, header=False)


# ## Task 1
# 
# Create a histogram depicting the relative frequencies of the card values.

# In[ ]:

import pandas
import matplotlib.pyplot as plt
cards = list(range(1, 11)) + [10, 10, 10]
cards = cards * 4
df = pandas.DataFrame(data = cards)
plt.figure()
ax = df.plot(kind='hist', bins=10, legend=False)
ax.set_xlabel('Value of cards')
ax.set_ylabel('Number of cards')


# ## Task 2
# 
# Now, we will get samples for a new distribution. To obtain a single sample, shuffle your deck of cards and draw three cards from it. (You will be sampling from the deck without replacement.) Record the cards that you have drawn and the sum of the three cards’ values. Repeat this sampling procedure a total of at least thirty times.

# In[ ]:

import random
import pandas
cards = list(range(1, 11)) + [10, 10, 10]
cards = cards * 4
dataset_size = 0
dataset = []
while(dataset_size<1000):
    dataset.append(sum(random.sample(cards, 3)))
    dataset_size+=1
df = pandas.DataFrame(data = dataset)
df.to_csv('dataset.csv', index=False, header=False)


# ## Task 3
# 
# Let’s take a look at the distribution of the card sums. Report descriptive statistics for the samples you have drawn. Include at least two measures of central tendency and two measures of variability.

# In[ ]:

import pandas
df = pandas.read_csv('dataset.csv', header=None)
print('Measure of Central Tendancy are:')
print('Mean   : ' + str(df.mean()[0]))
print('Median : ' + str(df.median()[0]))
print('Mode   : ' + str(df.mode()[0][0]))
print('\nMeasure of Variability are:')
print('Range               : ' + str(df.max()[0] - df.min()[0]))
factor=pandas.qcut(df, [.25, .75])
temp = factor[0][0]
temp = temp.replace('[', '')
temp = temp.replace(']', '')
quartile = temp.split(', ')
print('Interquartile Range : ' + str(int(quartile[1]) - int(quartile[0])))
print('Variance            : ' + str(df.var(ddof=False)[0]))
print('Standard Deviation  : ' + str(df.std(ddof=False)[0]))


# ## Task 4
# 
# Create a histogram of the sampled card sums you have recorded. Compare its shape to that of the original distribution. How are they different, and can you explain why this is the case?

# In[ ]:

import pandas
import matplotlib.pyplot as plt
df = pandas.read_csv('dataset.csv', header=None)
plt.figure()
ax = df.plot(kind='hist', bins=13, legend=False)
ax.set_xlabel('Sampled Card Sums') 
ax.set_ylabel('Frequency of Sampled Card Sums')


# The histogram of original distribution was almost uniform except the cards with value 10 had more frequency. The sampled card distribution can be understood from the original distribution. Since the original distribution has a unevenly high frequency on the right side of the histogram, the sample card sums becomes a left skewed histogram.

# ## Task 5
# 
# Make some estimates about values you will get on future draws. Within what range will you expect approximately 90% of your draw values to fall? What is the approximate probability that you will get a draw value of at least 20? Make sure you justify how you obtained your values.

# Since it a left skewed histogram, the probability to get a value would lie more in right side of the histogram. Hence for approximately 90% or more, the draws values can be calulated by finding the value for Z-Score having probability as 0.1 and then considering all the values to the right of it. ( Z(-1.28) = 0.1003 )

# In[ ]:

import pandas
df = pandas.read_csv('dataset.csv', header=None)
x = -1.28 * df.std(ddof=False)[0] + df.mean()[0]
print('Range where one can expect approximately 90% of the draw values to fall : ' + str(int(x)) + ' to ' + str(df.max()[0]))


# The approximate probability to get a value of 20 can again be calculated using Z table but this probability would less than the expected probability since the histogram is a left skewed histogram.

# In[ ]:

import pandas
import scipy as sc
df = pandas.read_csv('dataset.csv', header=None)
z = (20 - df.mean()[0])/df.std()[0]
p_values = sc.special.ndtr(z)
print('Approximate probability that one will get a draw value of at least 20 : ' + str(p_values))

