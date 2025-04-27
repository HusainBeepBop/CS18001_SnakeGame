# 14

def search_element():
    n = int(input("Enter the number of strings: "))
    strings = []
    for i in range(n):
        strings.append(input("Enter string " + str(i + 1) + ": "))
    element = input("Enter the element to search for: ")
    if element in strings:
        print("Element found at index", strings.index(element))
    else:
        print("Element not found in the list.")

search_element()