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