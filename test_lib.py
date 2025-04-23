import pytest
import numpy as np

import aqua_blue_hyperopt


def test_max_singular_value():

    # make a rotation matrix, ensure its max singular value is 1
    angle = 0.25 * np.pi
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    bar = aqua_blue_hyperopt.bar.Bar(matrix=rotation_matrix)
    singular_values = bar.singular_values(phrase="AAAAAAAAAA")
    assert np.isclose(singular_values.max(), 1.0)


def test_matrix_multiplication():

    rng = np.random.default_rng(seed=0)
    a = rng.uniform(size=(30, 50))
    b = rng.uniform(size=(50, 10))
    foo = aqua_blue_hyperopt.foo.Foo(first_matrix=a, second_matrix=b)
    result = foo.multiply_matrices()

    assert np.all(np.isclose(a @ b, result))


def test_raises_shape_mismatch_error():

    rng = np.random.default_rng(seed=0)
    a = rng.uniform(size=(20, 40))
    b = rng.uniform(size=(50, 15))
    with pytest.raises(aqua_blue_hyperopt.foo.ShapeMismatchError):

        _ = aqua_blue_hyperopt.foo.Foo(first_matrix=a, second_matrix=b)
