def task_1(text):
    sentences = text.split('. ')
    result = {}
    for i, sentence in enumerate(sentences):
        if i == len(sentences) - 1:
            sentence = sentence.rstrip('.')
        words = sentence.split()
        sentence_key = ' '.join(words)
        word_count = len(words)
        result[sentence_key] = word_count
    return result


def task_2(x1, y1, x2, y2):
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance
