def capitalize_first_word(sentence):
    if not sentence:
        return sentence

    # Split the sentence into words
    words = sentence.split()

    # Capitalize the first word
    words[0] = words[0].capitalize()

    # Reconstruct the sentence
    capitalized_sentence = ' '.join(words)
    return capitalized_sentence

if __name__ == "__main__":
    input_sentence = 'color field painting since futuristic megacity with a ethereal chessboard'
    result = capitalize_first_word(input_sentence)
    print("Capitalized Sentence:", result)