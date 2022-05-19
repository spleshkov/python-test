from hash_table import HashTable

hash_table = HashTable()
hash_table_2 = HashTable()
hash_table["a"] = 10
hash_table_2["a"] = 10
print(hash_table == hash_table_2)
print("a" in hash_table)
print(hash_table.values)
print(hash_table_2.items)

for item in hash_table:
    print(item)