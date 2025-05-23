text = """
hello world
hello hadoop
big data world
"""

def mapper(line):
    words = line.strip().split()
    return [(word, 1) for word in words]

from collections import defaultdict
mapped = []
for line in text.strip().split('\n'):
    mapped.extend(mapper(line))

shuffle_sort = defaultdict(list)
for word, count in mapped:
    shuffle_sort[word].append(count)

def reducer(shuffled_data):
    reduced = {}
    for word, counts in shuffled_data.items():
        reduced[word] = sum(counts)
    return reduced

word_counts = reducer(shuffle_sort)
for word, count in word_counts.items():
    print(f"{word}\t{count}")
