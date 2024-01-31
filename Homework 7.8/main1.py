class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_list = list_of_lists
        self.index_main = 0
        self.index_nested = 0
        self.max_index_main = len(self.list_of_list)
        self.max_index_nested = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.max_index_nested and self.max_index_nested <= self.index_nested:
            self.index_main += 1
            self.index_nested = 0
        if self.index_main >= self.max_index_main:
            raise StopIteration
        extract_items = self.list_of_list[self.index_main]
        self.max_index_nested = len(extract_items)

        item = extract_items[self.index_nested]
        self.index_nested += 1

        return item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e',
                                                   'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
