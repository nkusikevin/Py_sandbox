def create_acronym(phrase):
    words = phrase.split()  # Split the phrase into a list of words
    acronym = ""

    for word in words:
        acronym += word[0].upper()  # Add the first character of each word to the acronym

    return acronym

# Example usage
phrase = "James Bullough Lansing"
acronym = create_acronym(phrase)
print(acronym)  # Output: PNG
