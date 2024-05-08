def adjust_a_an(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    words = sentence.split()
    adjusted_words = []

    for i, word in enumerate(words):
        # Check if the word starts with a vowel
        if word.lower().startswith(tuple(vowels)):
            if i > 0 and words[i - 1].lower() == 'a' and not words[i].lower().startswith(tuple(vowels)):
                # Correct the grammar by skipping 'a'
                continue
            else:
                adjusted_words.append(word)
        else:
            adjusted_words.append(word)

    adjusted_sentence = ' '.join(adjusted_words)
    return adjusted_sentence


if __name__ == "__main__":
    input_sentence = 'color field painting since futuristic megacity with a ethereal chessboard'
    corrected_sentence = adjust_a_an(input_sentence)
    print("Corrected sentence:", corrected_sentence)
