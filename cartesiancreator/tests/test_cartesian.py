"""Run test cases for the functions that compute the Cartesian product."""


from cartesiancreator import cartesian


def test_cartesian_product_two_empty_sets():
    """Ensure that the Cartesian product works for two empty sets."""
    # TODO: write a test case that ensures an empty set results from the
    # cartesian product of two empty sets


def test_cartesian_product_one_empty_set_first():
    """Ensure that the Cartesian product works for one empty set."""
    first_set = set()
    second_set = set([1, 2])
    cartesian_product_set = cartesian.cartesian_product(first_set, second_set)
    cartesian_product_set_list = list(cartesian_product_set)
    assert len(cartesian_product_set_list) == 0


def test_cartesian_product_one_empty_set_second():
    """Ensure that the Cartesian product works for one empty set."""
    # TODO: write a test case that ensures that when the second input set
    # is the empty set that the output of cartesian_product is the empty set


def test_cartesian_product_two_small_sets():
    """Ensure that the Cartesian product works for example on page 127 of DMWP by Saha."""
    # TODO: write a test case that ensure that the cartesian_product function
    # works for the example that is on page 127 of the DMWP book by Saha
