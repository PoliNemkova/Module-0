from minitorch import operators
from hypothesis import given
from hypothesis.strategies import lists
from .strategies import small_floats, assert_close
import pytest


@pytest.mark.task0_1
@given(small_floats, small_floats)
def test_add_and_mul(x, y):
    assert_close(operators.mul(x, y), x * y)
    assert_close(operators.add(x, y), x + y)
    assert_close(operators.neg(x), -x)


@pytest.mark.task0_1
@given(small_floats)
def test_relu(a):
    if a > 0:
        assert operators.relu(a) == a
    else:
        assert operators.relu(a) == 0.0


## Task 0.2
## Property Testing


@pytest.mark.task0_2
@given(small_floats, small_floats)
def test_symmetric(x, y):
    """
    Write a test that ensures that :func:`minitorch.operators.mul` is symmetric, i.e.
    gives the same value regardless of the order of its input.
    """
    assert_close(operators.mul(x, y), y * x)


@pytest.mark.task0_2
@given(small_floats, small_floats, small_floats)
def test_distribute(z, x, y):
    r"""
    Write a test that ensures that your operators distribute, i.e.
    :math:`z \times (x + y) = z \times x + z \times y`
    """
    value = operators.add(x, y)
    assert_close(operators.mul(z, value), operators.mul(z, x) + operators.mul(z, y))
    # assert z*(x+y) == z*x+z*y
    # None
    # TODO: Implement for Task 0.2.
    # raise NotImplementedError('Need to implement for Task 0.2')


@pytest.mark.task0_2
@given(small_floats, small_floats)
def test_other(x, y):
    """
    Write a test that ensures some other property holds for your functions.
    """
    if x > y:
        assert_close(operators.max(x, y), x)
    else:
        assert_close(operators.max(x, y), y)

    None
    # TODO: Implement for Task 0.2.
    # raise NotImplementedError('Need to implement for Task 0.2')


# HIGHER ORDER


@pytest.mark.task0_3
@given(small_floats, small_floats, small_floats, small_floats)
def test_zip_with(a, b, c, d):
    assert_close(operators.addLists([a, b], [c, d]), [a + c, b + d])


@pytest.mark.task0_3
@given(
    lists(small_floats, min_size=5, max_size=5),
    lists(small_floats, min_size=5, max_size=5),
)
def test_property(ls1, ls2):

    sum = []
    for i in range(len(ls1)):
        sum.append(ls1[i] + ls2[i])
    assert_close(operators.addLists(ls1, ls2), sum)
    """
    Write a test that ensures that the sum of `ls1` plus the sum of `ls2`
    is the same as the sum of each element of `ls1` plus each element of `ls2`.
    """
    # TODO: Implement for Task 0.3.
    # raise NotImplementedError('Need to implement for Task 0.3')


@pytest.mark.task0_3
@given(lists(small_floats))
def test_sum(ls):
    assert_close(operators.sum(ls), sum(ls))


@pytest.mark.task0_3
@given(small_floats, small_floats, small_floats)
def test_prod(x, y, z):
    assert_close(operators.prod([x, y, z]), x * y * z)
