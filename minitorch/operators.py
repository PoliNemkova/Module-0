import math


## Task 0.1
## Mathematical operators


def mul(x: object, y: object) -> object:
    ":math:`f(x, y) = x * y`"
    return x * y
    # TODO: Implement for Task 0.1.
    # raise NotImplementedError('Need to implement for Task 0.1')


def id(x):
    ":math:`f(x) = x`"
    return x
    # TODO: Implement for Task 0.1.
    # raise NotImplementedError('Need to implement for Task 0.1')


def add(x, y):
    ":math:`f(x, y) = x + y`"
    return x + y
    # TODO: Implement for Task 0.1.
    # raise NotImplementedError('Need to implement for Task 0.1')


def neg(x):
    ":math:`f(x) = -x`"
    return -x
    # TODO: Implement for Task 0.1.
    # raise NotImplementedError('Need to implement for Task 0.1')


def lt(x, y):
    ":math:`f(x) =` 1.0 if x is less than y else 0.0"
    if x < y:
        return 1.0
    else:
        return 0.0
    # TODO: Implement for Task 0.1.
    # raise NotImplementedError('Need to implement for Task 0.1')


def eq(x, y):
    ":math:`f(x) =` 1.0 if x is equal to y else 0.0"
    if x == y:
        return 1.0
    else:
        return 0.0
    # TODO: Implement for Task 0.1.
    # raise NotImplementedError('Need to implement for Task 0.1')


def max(x, y):
    ":math:`f(x) =` x if x is greater than y else y"
    if x > y:
        return x
    else:
        return y
    # TODO: Implement for Task 0.1.
    # raise NotImplementedError('Need to implement for Task 0.1')


def sigmoid(x):
    r"""
    :math:`f(x) =  \frac{1.0}{(1.0 + e^{-x})}`

    (See `<https://en.wikipedia.org/wiki/Sigmoid_function>`_ .)

    Calculate as

    :math:`f(x) =  \frac{1.0}{(1.0 + e^{-x})}` if x >=0 else :math:`\frac{e^x}{(1.0 + e^{x})}`

    for stability.

    """
    if x >= 0:
        return 1.0 / (1.0 + exp(-x))
    else:
        return 1.0 / (exp(x) / 1.0 + exp(x))
    # TODO: Implement for Task 0.1.
    # raise NotImplementedError('Need to implement for Task 0.1')


def relu(x):
    """
    :math:`f(x) =` x if x is greater than 0, else 0

    (See `<https://en.wikipedia.org/wiki/Rectifier_(neural_networks)>`_ .)
    """
    if x > 0:
        return x
    else:
        return 0
    # TODO: Implement for Task 0.1.
    # raise NotImplementedError('Need to implement for Task 0.1')


def relu_back(x, y):
    ":math:`f(x) =` y if x is greater than 0 else 0"

    if x > 0:
        return y
    else:
        return 0
    # TODO: Implement for Task 0.1.
    # raise NotImplementedError('Need to implement for Task 0.1')


EPS = 1e-6


def log(x):
    ":math:`f(x) = log(x)`"
    return math.log(x + EPS)


def exp(x):
    ":math:`f(x) = e^{x}`"
    return math.exp(x)


def log_back(a, b):
    return b / (a + EPS)


def inv(x):
    ":math:`f(x) = 1/x`"
    return 1.0 / x


def inv_back(a, b):
    return -(1.0 / a ** 2) * b


## Task 0.3
## Higher-order functions.


def map(fn):
    def higher_order(ls):
        ls_new = []
        for item in ls:
            for i in range(ls.len()):
                ls_new[i] = fn(item)
        return ls_new

    return higher_order

    """
    Higher-order map.

    .. image::   figs/Ops/maplist.png


    See `<https://en.wikipedia.org/wiki/Map_(higher-order_function)>`_

    Args:
        fn (one-arg function): process one value

    Returns:
        function : a function that takes a list and applies `fn` to each element
    """

    # TODO: Implement for Task 0.3.
    # raise NotImplementedError('Need to implement for Task 0.3')


def negList(ls):
    "Use :func:`map` and :func:`neg` to negate each element in `ls`"
    return map(neg)(ls)


def zipWith(fn):
    def new_zip(ls1, ls2):
        if len(ls1) != len(ls2):
            return "List1 and List2 are not of the same length"
        else:
            return_list = []
            for i in range(0, len(ls1)):
                c = fn(ls1[i], ls2[i])
                return_list.append(c)

        return return_list

    return new_zip

    """
    Higher-order zipwith (or map2).

    .. image:: figs/Ops/ziplist.png

    See `<https://en.wikipedia.org/wiki/Map_(higher-order_function)>`_

    Args:
        fn (two-arg function): combine two values

    Returns:
        function : takes two equally sized lists `ls1` and `ls2`, produce a new list by
        applying fn(x, y) one each pair of elements.

    """
    # TODO: Implement for Task 0.3.
    # raise NotImplementedError('Need to implement for Task 0.3')


def addLists(ls1, ls2):
    "Add the elements of `ls1` and `ls2` using :func:`zipWith` and :func:`add`"
    return zipWith(add)(ls1, ls2)


def reduce(fn, start):
    def new_reduce(ls=[], cumulative=start):
        for i in ls:
            cumulative = fn(i, cumulative)
        return cumulative

    return new_reduce

    r"""
    Higher-order reduce.

    .. image:: figs/Ops/reducelist.png


    Args:
        fn (two-arg function): combine two values
        start (float): start value :math:`x_0`

    Returns:
        function : function that takes a list `ls` of elements
        :math:`x_1 \ldots x_n` and computes the reduction :math:`fn(x_3, fn(x_2,
        fn(x_1, x_0)))`

    """
    # TODO: Implement for Task 0.3.
    # raise NotImplementedError('Need to implement for Task 0.3')


def sum(ls):
    return reduce(add, 0)(ls)
    """
    Sum up a list using :func:`reduce` and :func:`add`.
    """
    # TODO: Implement for Task 0.3.
    # raise NotImplementedError('Need to implement for Task 0.3')


def prod(ls):
    return reduce(mul, 1)(ls)
    """
    Product of a list using :func:`reduce` and :func:`mul`.
    """
    # TODO: Implement for Task 0.3.
    # raise NotImplementedError('Need to implement for Task 0.3')
