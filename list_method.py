stringList = ['zeki+kanar', 'ali+durmus', 'mehmet+doner', 'salim+yanar']
# Create 2 different lists that contain separately names and surnames
# Capitalize names
# Uppercase surnames
names = []
surnames = []


def myFunc():
    stringList.sort()  # Sort the List Alphabetically
    for i in stringList:
        a, b = i.split('+')  # Split the items
        # Capitalize name and put it into the names list
        names.append(a.capitalize())
        # Uppercase surname and put it into the surnmes list
        surnames.append(b.upper())
    return names, surnames

print(myFunc())
