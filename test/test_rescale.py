import numpy as np
from example_package_andres9403.rescale import rescale
def test_rescale():
    np.testing.assert_allclose(rescale(np.array([1, 2, 3])), np.array([0, 50, 100]))
    assert rescale(np.array([1, 2, 3])).shape == (3,)
    