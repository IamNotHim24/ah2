# main.py
import q10 as stats

numbers = [1, 2, 3, 4, 4, 5, 6, 6, 6]

# Calculate mean, median, and mode using the module functions
mean_value = stats.mean(numbers)
median_value = stats.median(numbers)
mode_value = stats.mode(numbers)

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
