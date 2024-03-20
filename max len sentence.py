def max_words_in_sentence(sentences):
    max_words = 0
    for sentence in sentences:
        words = sentence.split()
        max_words = max(max_words, len(words))
    return max_words

# Test case
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
output = max_words_in_sentence(sentences)
print("Output:", output)

