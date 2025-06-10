def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content
    
def word_count(file_path):
    file_content = get_book_text(file_path)
    words = file_content.split()
    return len(words)