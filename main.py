def get_book_text(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read()
        print(file_contents)
        
def main():
    get_book_text("books/frankenstein.txt")
    
main()