import numpy as np


def split_string(word, indices):
    return [word[i: j] for i, j in zip([0] + indices, indices + [None])]

def numpy_split(word, indices):
    word_array = np.array(list(word))
    parts = np.split(word_array, indices)
    return [''.join(part) for part in parts]


def new_split(input:str, indices: list[int]):
    result = []
    for i in range(len(indices)):
        if i == 0:
            result.append(input[:indices[i]])
        else:
            result.append(input[indices[i-1]:indices[i]])
    result.append(input[indices[-1]:])
    return result

print("new",new_split('abcdefgh', [2, 4, 7]))
print("split",split_string('abcdefgh', [2, 4, 7]))