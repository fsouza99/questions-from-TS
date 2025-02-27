# The dataset as a dictionary.
data = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
    }

# Start by printing the total sum.
total = sum(data.values())
print('Total:', total)

# Now print the portion of each state.
for key, value in data.items():
    print(f"{key}: {value * 100 / total:.2f}%")

"""
Output:
Total: 180759.98
SP: 37.53%
RJ: 20.29%
MG: 16.17%
ES: 15.03%
Outros: 10.98%
"""
