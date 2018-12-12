#nested list/multidimentional list

List = [43, [54, 75, [53, 86, 96], 75, 54], 85, 6, 53, 85, 2, 54, 'Mohon Basu']

List.append(65)
List.insert(2, 95)
List.extend([0, 1, 2, 3])
List = List + [0, 1, 2, 3]
#List.remove('Mohon Basu')
List.remove(List[9])
List.pop()
#List.sort()
print(List.index(6))
print(List.count(2))

print(List)
print(List[1])
print(List[1][2])
print(List[1][2][1])