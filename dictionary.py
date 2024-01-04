import string

def word_frequency(sentence):
    # Remove punctuation and convert to lowercase
    translator = str.maketrans("", "", string.punctuation)
    cleaned_sentence = sentence.translate(translator).lower()

    # Split the sentence into words
    words = cleaned_sentence.split()

    # Count the frequency of each word using a dictionary
    frequency_dict = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1

    return frequency_dict

# Test case
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
