
def reverse_string(word):
    result = ""
    # traverse from last (len - 1) to first (0)
    # range(7, -1, -1) = 7…6…5…4…3…2…1…0
    for i in range(len(word) - 1, -1, -1):
        # store each character in a variable
        result += word[i]
    return result



word = "captain"
print(reverse_string(word))