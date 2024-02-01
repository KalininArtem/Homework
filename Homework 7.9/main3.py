import datetime
import types

def logger(path):

    def __logger(old_function):
        def new_function(*args, **kwargs):
            datetime_now = datetime.datetime.now()
            return_value = old_function(*args, **kwargs)

            with open(path, 'a+', encoding='utf-8') as f:
                f.write(
                    f"{datetime_now} {old_function.__name__} {args} "
                    f"{kwargs} {return_value}\n")
            return return_value

        return new_function

    return __logger
@logger('homework_3.log')
def flat_generator(list_of_lists):
    for nested_list in list_of_lists:
        for el in nested_list:
            yield el



def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()