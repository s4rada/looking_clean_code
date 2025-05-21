data = [['Ben', 'Manager', 3000],
           ['James', 'Cleaner', 1000],
           ['Ken', 'Supervisor', 2000]]

# Dictionary mapping old names → new names
name_changes = {
    'Ben': 'Josh',
    'James': 'ddg',
    'Ken': 'Josdgsdsh'
}
converted = []
# Loop through each sublist and check every element
for sublist in data:
    sub_list = []
    for i, item in enumerate(sublist):
        if item in name_changes:
            sub_list.append(name_changes[item])
    converted.append(sub_list)
zawg = []
for i in converted:
    new = " ".join(i)
    zawg.append(new)
print(zawg)
