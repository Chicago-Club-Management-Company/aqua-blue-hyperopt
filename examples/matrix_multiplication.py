import numpy as np

import aqua_blue_hyperopt


def main():

    rng = np.random.default_rng(seed=0)
    first_matrix = rng.uniform(size=(100, 50))
    second_matrix = rng.uniform(size=(50, 25))
    foo = aqua_blue_hyperopt.foo.Foo(first_matrix=first_matrix, second_matrix=second_matrix)
    multiplied = foo.multiply_matrices()
    print(multiplied)


if __name__ == "__main__":

    main()
