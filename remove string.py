def remove_common_words(str1, str2):
    words1 = str1.split()
    words2 = str2.split()

    unique_words1 = []
    unique_words2 = []

    for word in words1:
        if word not in words2:
            unique_words1.append(word)

    for word in words2:
        if word not in words1:
            unique_words2.append(word)

    unique_str1 = ' '.join(unique_words1)
    unique_str2 = ' '.join(unique_words2)

    return unique_str1, unique_str2

# Test case
string1 = "hello world python"
string2 = "hello python programming"
unique_str1, unique_str2 = remove_common_words(string1, string2)
print("Unique words in string 1:", unique_str1)
print("Unique words in string 2:", unique_str2)
