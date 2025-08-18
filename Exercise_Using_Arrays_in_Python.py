import array

temperatures = array.array('f', [72.5, 74.0, 69.8, 70.2, 73.1, 75.6, 71.3])
print(temperatures)

temperatures.pop(3)
print(temperatures)

temperatures.insert(3, 70.0)
print(temperatures)

temperatures.append(78.0)
print(temperatures)

for i in range(len(temperatures)):
    temperatures[i] += 1.0
print(temperatures)

#create a string array all lowercase
string_array = ["exhausted","dead", "tiRed", "hopeless", "despondent"]
print(string_array)
#use a for loop to iterate of the array and capitalize each value
for i in range(len(string_array)):
    string_array[i] = string_array[i].capitalize()
#print the updated array
print(string_array)
