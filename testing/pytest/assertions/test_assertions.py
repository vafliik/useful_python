def test_numeric_assertion_fail():
    assert 2156123.1 == 2156233.2


def test_similar_text_assertion_fail():
    assert 'Nobody expects the Spanish Inquisition' == 'Nobody expefts the Spanifwh InquiFition'


def test_different_text_assertion_fail():
    knight_quote = 'It\'s just a flesh wound. I\'ve had worse.'
    arthur_quote = 'The Knights Who Say Ni.'

    assert knight_quote == arthur_quote


def test_item_not_in_text_fail():
    silly_text = "I'm sorry to have kept you waiting, but I'm afraid my walk has become rather sillier recently."
    assert 'afraid' not in silly_text


def test_list_assertion_fail():
    list_from_string = list("My hovercraft")
    expected_list = ['M', 'y', ' ', 'h', 'o', 'v', 'e', 'n', 'c', 'r', 'a', 'n', 't']

    # The assert will look better with "pytest -v"
    assert list_from_string == expected_list, "The lists do not match"


def test_item_in_list_fail():
    my_list = list(range(1, 5))
    assert 5 in my_list


def test_set_assertion_fail():
    set1 = set("15965")
    set2 = set("15674")

    assert set1 == set2


def test_set_assertion_pass():
    set1 = set("15965")
    set2 = set("5169")

    assert set1 == set2


def test_dict_assertion_fail():
    assert {'a': 0, 'b': 1, 'c': 0} == {'a': 0, 'b': 2, 'd': 0}
