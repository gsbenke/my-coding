import blah

def count_words(mystring):
    print(mystring)
    words = mystring.split()
    print(words)
    numwords = len(words)
    print(numwords)
    return numwords

if __name__ == "__main__":
    count_words("watermelon \t mango apple orange \nhello\nhi")
    count_words("different stuff in here")
    count_words("Happy Halloween")
    count_words("These are some words")
    with open("book.txt", encoding="utf8") as f:
        words = f.read()
        num_chars = len(words)
        num_words = count_words(words)
        print(f"The book has {num_chars} characters and {num_words} words.")
