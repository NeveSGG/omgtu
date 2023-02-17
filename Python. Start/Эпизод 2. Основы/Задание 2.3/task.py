# todo: replace this with an actual task
def task_1(str):
    words = str.split()
    last_word = words[-1]
    last_word_length = len(last_word)
    return last_word_length


def task_2(str):
    words = str.split()
    new_words = []
    for i in range(len(words)):
        if i % 2 == 0 and i < len(words) - 1:
            new_words.append(words[i + 1])
        elif i % 2 != 0:
            new_words.append(words[i - 1])
        else:
            new_words.append(words[i])
    new_str = " ".join(new_words)
    print(new_str)
    return new_str


def task_3(str):
    words = str.split()
    count = 0
    for i in range(1, len(words)):
        if words[i][0].lower() == words[i - 1][-1].lower():
            count += 1
    print(count)
    return count
