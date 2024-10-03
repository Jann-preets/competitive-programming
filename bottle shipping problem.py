def bottle_shipping(bottles):
    carton_sizes = [48, 24, 12, 6] 
    carton_names = ["xl", "large", "medium", "small"]
    
    results = []

    for i in range(len(carton_sizes)):
        size = carton_sizes[i]
        name = carton_names[i]
        
        if bottles >= size:  
            count = bottles // size  
            results.append(f"{count} {name}")  
            bottles -= count * size  
    
    return ', '.join(results)


bottles_to_ship =int(input())
output = bottle_shipping(bottles_to_ship)
print(output) 
