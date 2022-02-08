topic=["Physics","CompSci","Math","Art"]

print(topic)
print(type(topic))

colors=["red", "orange", "green"]
print(colors)
print(colors[2])
print(colors[-1])

colors[2]="yellow"
print(colors)

#.append()

colors.append("blue")
print(colors)

newColors=[]
newColors.append("red")
newColors.append("black")
newColors.append("brown")
print(newColors)

print(newColors[1])
newColors.insert(1,"purple")
print(newColors[1])

newColors.remove("purple")
print(newColors)

#.pop()
colored=["red", "orange", "green","purple", "blue"]
removedColor = colored.pop()
print(removedColor)

badColor=colored.pop(2)
print(badColor)

#del
