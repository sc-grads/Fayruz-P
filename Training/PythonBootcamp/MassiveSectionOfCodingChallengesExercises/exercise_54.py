salaries = {'John': 50000, 'Anne': 66000, 'Antonio': 48000}

taxes = {k: v * 0.1 for k, v in salaries.items()}
print(taxes)  # => {'John': 5000.0, 'Anne': 6600.0, 'Antonio': 4800.0}