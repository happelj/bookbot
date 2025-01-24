with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def count_words(file_contents):
    """Counts the number of words in the file."""
    return len(file_contents.split())

def count_characters(file_contents):
    """Counts the occurrences of each character in the file."""
    text = file_contents.lower()
    char_counts = {}

    for char in text:
        if char.isalpha():  # Consider only alphabetic characters
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts

def generate_report(file_contents):
    """Generates a nicely formatted report."""
    # Count words and characters
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)

    # Sort character counts in descending order
    sorted_char_counts = sorted(
        [{"char": char, "num": count} for char, count in char_count.items()],
        key=lambda x: x["num"],
        reverse=True
    )

    # Print the report
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    for item in sorted_char_counts:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

# Call the report generation function
generate_report(file_contents)
