import matplotlib.pyplot as plt

# Ownership F1 
hops = [2, 3, 4, 5]
gpt4_f1 = [0.84, 0.51, 0.73, 0.80]  
haiku_f1 = [0.83, 0.63, 0.47, 0.32]  
sonnet_f1 = [1, 0.94, 0.92, 0.93]  
llama_f1 = [0.36, 0.11, 0.36, 0.28]
# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(hops, gpt4_f1, marker='o', label='GPT-4')
plt.plot(hops, haiku_f1, marker='s', label='Haiku')
plt.plot(hops, sonnet_f1, marker='^', label='Sonnet')
plt.plot(hops, llama_f1, marker='d', label='Llama')
# Add labels, title, and legend
plt.xlabel('#hops', fontsize=12)
plt.ylabel('F1 Score', fontsize=12)
plt.title('F1 Score vs number of hops for Ownership', fontsize=14)
plt.xticks(hops)  # Ensure x-axis ticks align with hops
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Ownership', fontsize=10)
# Show the plot
plt.tight_layout()
plt.show()

# Ownership precision
hops = [2, 3, 4, 5]
gpt4_pre = [0.85, 0.51, 0.72, 0.75]
haiku_pre = [0.85, 0.54, 0.39, 0.24]
sonnet_pre = [1, 0.94, 0.86, 0.88] 
llama_pre = [0.47, 0.2, 0.4, 0.29] 
# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(hops, gpt4_pre, marker='o', label='GPT-4')
plt.plot(hops, haiku_pre, marker='s', label='Haiku')
plt.plot(hops, sonnet_pre, marker='^', label='Sonnet')
plt.plot(hops, llama_pre, marker='d', label='Llama')
# Add labels, title, and legend
plt.xlabel('#hops', fontsize=12)
plt.ylabel('Precision', fontsize=12)
plt.title('Precision vs number of hops for Ownership', fontsize=14)
plt.xticks(hops)  # Ensure x-axis ticks align with hops
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Ownership', fontsize=10)
# Show the plot
plt.tight_layout()
plt.show()

# Ownership recall
hops = [2, 3, 4, 5]
gpt4_rec_ = [0.82, 0.5, 0.75, 0.86]
haiku_rec= [0.82, 0.77, 0.63, 0.5]
sonnet_rec = [1, 0.94, 1, 1] 
llama_rec = [0.29, 0.08, 0.33, 0.29] 
# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(hops, gpt4_rec_, marker='o', label='GPT-4')
plt.plot(hops, haiku_rec, marker='s', label='Haiku')
plt.plot(hops, sonnet_rec, marker='^', label='Sonnet')
plt.plot(hops, llama_rec, marker='d', label='Llama')
# Add labels, title, and legend
plt.xlabel('#hops', fontsize=12)
plt.ylabel('Recall', fontsize=12)
plt.title('Recall vs number of hops for Ownership', fontsize=14)
plt.xticks(hops)  # Ensure x-axis ticks align with hops
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Ownership', fontsize=10)
# Show the plot
plt.tight_layout()
plt.show()

###########################
###########################

# Containment F1
hops = [2, 3, 4, 5]
gpt4_f1 = [1.0, 0.94, 0.93, 0.94]  
haiku_f1 = [0.82, 0.74, 0.89, 0.71] 
sonnet_f1 = [1, 1, 1, 1] 
llama_f1 = [0.88, 0.82, 0.92, 0.93]  
# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(hops, gpt4_f1, marker='o', label='GPT-4')
plt.plot(hops, haiku_f1, marker='s', label='Haiku')
plt.plot(hops, sonnet_f1, marker='^', label='Sonnet')
plt.plot(hops, llama_f1, marker='d', label='Llama')
# Add labels, title, and legend
plt.xlabel('#hops', fontsize=12)
plt.ylabel('F1 Score', fontsize=12)
plt.title('F1 Score vs number of hops for Containment', fontsize=14)
plt.xticks(hops)  # Ensure x-axis ticks align with hops
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Ownership', fontsize=10)
# Show the plot
plt.tight_layout()
plt.show()

# Containment presision
hops = [2, 3, 4, 5]
gpt4_pre = [1, 0.95, 0.89, 0.89]
haiku_pre = [0.94, 0.67, 0.83, 0.55]
sonnet_pre = [1, 1, 1, 1] 
llama_pre = [0.92, 0.95, 1.0, 1.0] 
# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(hops, gpt4_pre, marker='o', label='GPT-4')
plt.plot(hops, haiku_pre, marker='s', label='Haiku')
plt.plot(hops, sonnet_pre, marker='^', label='Sonnet')
plt.plot(hops, llama_pre, marker='d', label='Llama')
# Add labels, title, and legend
plt.xlabel('#hops', fontsize=12)
plt.ylabel('Precision', fontsize=12)
plt.title('Precision vs number of hops for Containment', fontsize=14)
plt.xticks(hops)  # Ensure x-axis ticks align with hops
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Ownership', fontsize=10)
# Show the plot
plt.tight_layout()
plt.show()



# Containment recall
hops = [2, 3, 4, 5]
gpt4_rec_ = [1, 0.93, 0.96, 1]
haiku_rec= [0.72, 0.84, 0.96, 1]
sonnet_rec = [1, 1, 1, 1] 
llama_rec = [0.84, 0.72, 0.85, 0.88] 
# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(hops, gpt4_rec_, marker='o', label='GPT-4')
plt.plot(hops, haiku_rec, marker='s', label='Haiku')
plt.plot(hops, sonnet_rec, marker='^', label='Sonnet')
plt.plot(hops, llama_rec, marker='d', label='Llama')
# Add labels, title, and legend
plt.xlabel('#hops', fontsize=12)
plt.ylabel('Recall', fontsize=12)
plt.title('Recall vs number of hops for Ownership', fontsize=14)
plt.xticks(hops)  # Ensure x-axis ticks align with hops
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Ownership', fontsize=10)
# Show the plot
plt.tight_layout()
plt.show()