
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'n']

duplicates_dic = {}
dup_list = []

for item in some_list:
    counter = duplicates_dic.get(item)
    new_count = 1 if not counter else counter + 1
    duplicates_dic[item] = new_count

for key, value in duplicates_dic.items():
      if (value > 1):
            dup_list.append(key)

print(dup_list)
