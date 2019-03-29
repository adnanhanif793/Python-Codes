from email._header_value_parser import ListSeparator


print("Selenium is working")

s="adnan"
print(sorted(s))

print(s)

print(s[::-1])


lists=[1,2,3,4,5,'Adnan']
lists.append('hanif')
print(lists)
print(lists[0:-1])#upper limit is not included and from the reverse side the index starts with -1
print(lists[-4:-1])
print(lists[::-1])# reverse the list but not saved
print(lists[::-2])
lists.append(5)
lists.append(5)
lists.remove('hanif')
print(lists)
print(lists.count(5))
print(lists.index(4))
lists.reverse() # reverse the list and saves the list
print(lists)

