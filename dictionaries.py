def word_frequency(sentence):  
# Define a string containing punctuation characters
    punctuation_chars = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    # Convert the sentence to lowercase and remove punctuation
    translator = str.maketrans("", "", punctuation_chars)
    cleaned_sentence = sentence.translate(translator).lower()

    # Split the cleaned sentence into words
    words = cleaned_sentence.split()

    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

# Test case
sentence = "The quick brown fox jumps over the lazy dog. The dog barks, and the fox runs."
print(word_frequency(sentence))