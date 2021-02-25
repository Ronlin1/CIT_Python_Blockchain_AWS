# string character's can be accessed by indexing like lists

city = "Kampala"

print(len(city))

for i in range(len(city)):
    print("string element: "+city[i]+", index: "+str(i))

for i in range(len(city)):
    print(f'The letter {city[i]} is at index {i}')
