from matplotlib import pyplot as plt

variance = list(2 ** i for i in range(9))
bias_squared = list(reversed(variance))
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

print(variance, bias_squared, total_error, xs)

plt.plot(xs, variance, '-g', label="variance")
plt.plot(xs, bias_squared, 'r-.', label="bias^2")
plt.plot(xs, total_error, 'b:', label='total error')

plt.legend(loc=9)
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()
