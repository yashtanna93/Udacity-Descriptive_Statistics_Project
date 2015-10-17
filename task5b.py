import pandas
df = pandas.read_csv('dataset.csv', header=None)
z = (20 - df.mean()[0])/df.std()[0]
p_values = 0.52979037447 #Z(0.074742928658) = 0.52979037447
print('Approximate probability that one will get a draw value of at least 20 : ' + str(p_values))