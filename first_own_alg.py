# find the lowest value in a list
data = [
    665575,65,34,232,322,53,3345,6556
]

def find_lowest_value(data):
    if not data:
        return "No data provided";
    min_value = data[0];
    for value in data:
        if value < min_value:
            min_value = value
    return min_value

min_value = find_lowest_value(data)

def find_highest_value(data):
    if not data:
        return "No data provided";
    maxValue = data[0];
    for value in data:
        if value > maxValue:
            maxValue = value
    return maxValue

max_value = find_highest_value(data);

print("Lowest value:", min_value)
print("Highest value:", max_value)




