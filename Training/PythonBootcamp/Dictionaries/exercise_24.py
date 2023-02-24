visits = {'Monday': 5000,
          'Tuesday': 3000,
          'Wednesday': 4000,
          'Thursday': 4500,
          'Friday': 5000,
          'Saturday': 2000,
          'Sunday': 1500
          }

## YOUR CODE STARTS HERE
total_visits = 0
for values in visits.values():
    total_visits += values

percentage = {k: (v / total_visits) * 100 for k, v in visits.items()}
print(percentage)
