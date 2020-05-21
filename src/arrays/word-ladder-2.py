from collections import defaultdict


def generate_graph(word_list):
    graph = defaultdict(set)

    for word in word_list:
        for i in range(len(word)):
            new_word = word[:i] + '*' + word[i + 1:]
            graph[new_word].add(word)
            graph[word].add(new_word)

    return graph


def get_neighbours(graph, word):
    neighbours = set()
    for star_word in graph[word]:
        for neighbour in graph[star_word]:
            neighbours.add(neighbour)
    neighbours.remove(word)
    return neighbours


def solve(begin_word, end_word, word_list):
    graph = generate_graph([begin_word, *word_list])

    if end_word not in graph:
        return []

    result = []
    queue = [(begin_word, [begin_word])]
    visited = set()
    while len(queue) > 0:
        next_level = []

        for word, path in queue:
            visited.add(word)
            for neighbour in get_neighbours(graph, word):
                if neighbour in visited:
                    continue
                if neighbour == end_word:
                    result.append(path + [end_word])
                    continue
                next_level.append((neighbour, path + [neighbour]))

        if len(result) > 0:
            break

        queue = next_level

    return result
