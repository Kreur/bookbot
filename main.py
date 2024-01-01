def main():
    book_path = "books/frankenstein.txt"
    book_text = get_file_text(book_path)
    print(book_text)


def get_file_text(path):
    with open(path) as file:
        return file.read()




main()
