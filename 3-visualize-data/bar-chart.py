from typing import Counter
from matplotlib import pyplot as plt

# movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
# num_oscars = [5, 11, 3, 8, 10]

# xs = [i + 0.1 for i, _ in enumerate(movies)]
# # xs = list(range(len(movies)))

# plt.bar(xs, num_oscars)

# plt.ylabel("# of Academy Awards")
# plt.title("My Favorite Movies")

# plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

grades = [83, 95, 91, 87, 70, 0, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

plt.bar([x for x in histogram.keys()], histogram.values(), 8)

plt.axis(( -5, 105, 0, 5 )) # x-axis -5 to 105, y-axis 0 - 5

plt.xticks([10 * i for i in range(11)]) # number of bars
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribuition of Exam 1 Grades")

plt.show()
