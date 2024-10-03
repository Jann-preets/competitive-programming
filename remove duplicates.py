def remove_duplicates(arr):
    if len(arr) == 0:  
        return []

    unique_arr = [arr[0]]  

    for i in range(1, len(arr)):  
        if arr[i] != arr[i - 1]:  
            unique_arr.append(arr[i])  

    return unique_arr
input_string = input()
input_array = list(map(int, input_string.split(',')))
output_array = remove_duplicates(input_array)
print(output_array)
