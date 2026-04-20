# Define dictionaries
dict1 = {"a": 1}
dict2 = {"b": 2}

# Merge dictionaries
merged = {}

# Add elements of first dictionary
for key in dict1:
    merged[key] = dict1[key]

# Add elements of second dictionary
for key in dict2:
    merged[key] = dict2[key]

# Display result
print(merged)