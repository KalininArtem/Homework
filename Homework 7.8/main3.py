from copy import deepcopy


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = deepcopy(list_of_list)

    def __iter__(self):
        return self

    def __next__(self):
        while self.list_of_list:
            item = self.list_of_list.pop(0)
            if isinstance(item, list):
                self.list_of_list = item + self.list_of_list
            else:
                return item
        raise StopIteration


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item
    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e',
                                                   'f', 'h', False, 1, 2, None,
                                                   '!']


if __name__ == '__main__':
    test_3()
