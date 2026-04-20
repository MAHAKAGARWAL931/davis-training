# Define dictionary
data = {"b": 2, "a": 1}

# Sort dictionary by keys
sorted_dict = {}

# Get sorted keys
for key in sorted(data):
    sorted_dict[key] = data[key]

# Display result
print(sorted_dict)