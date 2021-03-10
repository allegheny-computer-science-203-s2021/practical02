"""Test cases for the compute_tf_cookbook program"""

from termfrequency import compute_tf_cookbook


def test_read_file_populates_data():
    """Checks that the singleline comment count works"""
    # pylint: disable=len-as-condition
    assert len(compute_tf_cookbook.data) == 0
    compute_tf_cookbook.read_file("inputs/input.txt")
    assert len(compute_tf_cookbook.data) != 0

