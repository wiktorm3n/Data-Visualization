from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

'''Create a three D6'''
die1 = Die()
die2 = Die()
die3 = Die()

'''Make some rolls, and store results in a list'''
results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll() + die3.roll()
    results.append(result)

'''Analize the results'''
frequencies = []
max_result = die1.num_sides + die2.num_sides + die3.num_sides
for values in range(3, max_result + 1):
    frequency = results.count(values)
    frequencies.append(frequency)

'''Visualize the results'''
x_values = list(range(3, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Results'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling three D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_d6.html')


