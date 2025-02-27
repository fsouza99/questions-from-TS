from json import load

def load_data():
    """Loads dataset from file."""
    with open('dados.json') as file:
        data = load(file)
    return data

def stats(data):
    """Returns global minimum, global maximum and mean of working days."""
    # The 'c' below stands for 'current'.
    cmin = cmax = (data[0]['dia'], data[0]['valor'])

    # Get mean manually.
    total = count = 0

    for row in data:
        day, value = row['dia'], row['valor']
        
        # Skip nil values.
        if value == 0:
            continue

        # Update stats
        cmin = (day, value) if value < cmin[1] else cmin
        cmax = (day, value) if value > cmax[1] else cmax

        # Useful info for mean.
        total += value
        count += 1

    mean = total / count
    return cmin, cmax, mean

def count_above(data, value):
    """Returns total number of values above a particular one in a dataset."""
    total = 0
    for row in data:
        if row['valor'] > value:
            total += 1
    return total

data = load_data()
gmin, gmax, gmean = stats(data)
above_mean_count = count_above(data, gmean)

print(f"""Stats on Working Days

Worst: {gmin[0]}, {gmin[1]}
Best: {gmax[0]}, {gmax[1]}
Mean: {gmean:.4f}
Better than mean: {above_mean_count}
""")

"""
Output:
Stats on Working Days

Worst: 14, 373.7838
Best: 16, 48924.2448
Mean: 20865.3702
Better than mean: 10
"""
