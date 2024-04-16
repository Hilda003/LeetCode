class Solution:
    def reverse_words(text):
        # Split word
        words = text.split(' ')

        reverse_words = []

        for i in words:
            reverse_words.append(i[::-1])
        
        reverse_sentence = ' '.join(reverse_words)
        return reverse_sentence

    print(reverse_words("Hallo this is World!"))

        