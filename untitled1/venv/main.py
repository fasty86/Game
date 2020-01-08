import cs50

test = []
for i in range(3):
    test.append(cs50.get_string("Input something: "))
popped = test.pop(-1)
print(test)
print(f"some example : {popped=}")
test.insert(1, 'koko')
print(test)
remove = cs50.get_string("to delete: ")
test.remove(remove)
print(test)
