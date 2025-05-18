def get_num_words(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read()
        words = file_contents.split()
        num_words = len(words)
        print(f"{num_words} words found in the document")
        
def get_num_letters(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read()
        
        countAlpha = {}
        
        for letter in file_contents:
            for char in letter:
                countAlpha.setdefault(char.lower(), 0)
                countAlpha[char.lower()] += 1
        
        print(countAlpha)