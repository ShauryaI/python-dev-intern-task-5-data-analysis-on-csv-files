from matplotlib import pyplot as plt

x = [5, 2, 9, 4, 7]
y = [10, 5, 8, 4, 2]

# plt.plot(x, y) # Line plot

# plt.bar(x, y) # Bar plot

data = [5, 2, 9, 4, 7, 1, 6, 8, 3, 7, 6, 4, 8, 5, 9]
# plt.hist(data, bins=5, edgecolor='black') # Histogram

plt.scatter(x, y) # Scatter Plot

plt.title("Position vs Time")
plt.xlabel("Time (hr)")
plt.ylabel("Position (Km)")

plt.show()