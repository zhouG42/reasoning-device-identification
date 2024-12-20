import matplotlib.pyplot as plt
import numpy as np

# Data for the bar diagram
categories = ['2-hop', '3-hop', '4-hop', '5-hop']
bars1 = np.array([30, 20, 18, 10])  # Values for the first set of bars
#bars2 = np.array([10, 5, 8, 4])  # Values for the second set of bars
bars3 = np.array([20, 16, 14, 9])  # Values for the third set of bars


# Normalize: Jena is full score (1), others scaled relative to Jena
#bars2 = bars2 / bars1  
bars3 = bars3 / bars1  
bars1 = bars1 / bars1  

# y axis normalize to percentage
# X positions for bars
x = np.arange(len(categories))

# Bar width
bar_width = 0.25

# Plotting the bars
plt.bar(x - bar_width, bars1, width=bar_width, color='#1f77b4', label='Jena')  # Light green
#plt.bar(x, bars2, width=bar_width, color='#ff7f0e', label='llama3')  # light blue --> empty for now as llama3 doesn't give any meaningful results, maybe some prompt changes
plt.bar(x + bar_width, bars3, width=bar_width, color='#2ca02c', label='GPT4')  # Light yeloow
# Adding labels, title, and legend
plt.xlabel('Rule Complexity')
plt.ylabel('Percentage of Correctness')
plt.title('Reasoning results based on number of hops')
plt.xticks(x, categories)
plt.legend()

plt.tight_layout()
plt.show()
