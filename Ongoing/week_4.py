# Assignment #1
# -------------
# my_list = [1, 2, 3, 3, 4, 5, 1]
# unique_list = set(my_list)  # set elements are unique, removes every occurences
# unique_list = list(unique_list)
# print(unique_list)
# print(type(unique_list))
# unique_list.pop(-1)
# print(unique_list)
# Assignment #2
# -------------
# nums = {1, 2, 3}
# letters = {"A", "B", "C"}
# print(nums | letters)  # method 1
# print(nums.union(letters))  # method 2
# nums.update(letters) # method 3 --> nums has now the new set, the function itself does not return the new set but only iterates it.
# print(nums)
# -------------
# Assignment #3
# my_set = {1, 2, 3}
# letters = {"A", "B", "C"}
# print(my_set)
# my_set.clear()
# print(my_set)
# my_set.add("A")
# my_set.add("B")
# my_set.discard("C")
# print(my_set)
# -------------
# Assignment #4
# set_one = {1, 2, 3}
# set_two = {1, 2, 3, 4, 5, 6}
# print(set_one.issubset(set_two)) # one is part of two.
# print(set_two.issuperset(set_one)) # two contains one
# -------------
# Assignment #5
mydict = {
    "HTML": "90%",
    "CSS": "80%",
    "Python": "30%",
    "AI": "20%"
}
keys = mydict.keys()
values = mydict.values()
print(keys)
# -------------
