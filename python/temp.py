filename = "temp.txt"

with open(filename) as f:
    content = f.readlines()
content = str([string.strip().replace(' ','') for string in content])

# read char
char_list = list()
count_list = list()
i = 0

for ch in content:
    # if in list, count and update
    if ch not in char_list:
        char_list.append(ch)
        count_list.append(content.count(ch))
        i += 1;
    else:
        # pass
        continue

# Mapping lists
map_dict = {k: v for k, v in zip(char_list, count_list)}

# Sorting lists
sort_dict = {k: v for k, v in sorted(map_dict.items(), key=lambda item:item[1], reverse=True)}

# Printing
#print(sort_dict)

for keys,values in sort_dict.items():
    print(keys, ':', values)
