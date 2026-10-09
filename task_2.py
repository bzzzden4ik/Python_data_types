text = input()

words = text.lower().split()

words_counter = dict()

for word in words:
    if word in words_counter:
        words_counter[word] += 1
    else:
        words_counter[word] = 1

sorted_words = sorted(words_counter.items(), key=lambda item: item[1], reverse=True)

for word, count in sorted_words[:5]:
    print(f"{word}: {count}")