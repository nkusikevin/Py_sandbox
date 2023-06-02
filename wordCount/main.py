def counter(text):
    word_counts = {}
    words = text.split()

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


text = input("Enter the text: ")
word_counts = counter(text)

# Display the word counts
for word, count in word_counts.items():
    print(f"{word}: {count}")
