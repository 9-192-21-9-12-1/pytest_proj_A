from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 2) == 3
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]

def test_my_slice_negative_indexes():
    assert arrs.my_slice([1, 2, 3, 4], -3, -1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -2) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1, -1) == [2]

def test_my_slice_empty_list():
    assert arrs.my_slice([], 0, 2) == []

def test_my_slice_negative_index_out_of_range():
    lst = [1, 2, 3, 4, 5]
    assert arrs.my_slice(lst, -6, -2) == lst[-6:-2]