# Create a simple algorithm that determines whether the following dataset contains a float (decimal), deletes it from the dataset, 
# and returns the final array: [30583,283830.10,3948830930,1839.20,29483.1]

def decimalDelete(lst):
    new_arr = []
    for num in lst:
        if isinstance(num, float):
            new_arr.append(int(num))
        else:
            new_arr.append(num)
    return new_arr

print(decimalDelete([30583,283830.10,3948830930,1839.20,29483.1]))
