def popular_words(text, words):
    word_counts = {}
    text_words = text.lower().split()
    for word in words:
        word_counts[word] = text_words.count(word)

    return word_counts

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')