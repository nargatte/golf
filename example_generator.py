import random
import data_preparation
import sys


def generate_example(num_of_pairs, seed=None):
    random.seed(seed)
    return [(random.random(), random.random()) for _ in range(num_of_pairs)], \
           [(random.random(), random.random()) for _ in range(num_of_pairs)]


def generate_to_file(num_of_pairs, path):
    a, b = generate_example(num_of_pairs)
    text = data_preparation.a_b_to_text(a, b)
    with open(path, "w") as f:
        f.write(text)


if __name__ == "__main__":
    n = int(sys.argv[1])
    path = sys.argv[2]
    generate_to_file(n, path)

