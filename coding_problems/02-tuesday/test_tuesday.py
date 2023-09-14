from tuesday import multi_table


def test_multi_table_with_5():
    assert multi_table(
        5) == '1 * 5 = 5\n2 * 5 = 10\n3 * 5 = 15\n4 * 5 = 20\n5 * 5 = 25\n6 * 5 = 30\n7 * 5 = 35\n8 * 5 = 40\n9 * 5 = 45\n10 * 5 = 50'


def test_multi_table_with_1():
    assert multi_table(
        1) == '1 * 1 = 1\n2 * 1 = 2\n3 * 1 = 3\n4 * 1 = 4\n5 * 1 = 5\n6 * 1 = 6\n7 * 1 = 7\n8 * 1 = 8\n9 * 1 = 9\n10 * 1 = 10'


def test_multi_table_with_10():
    assert multi_table(
        10) == '1 * 10 = 10\n2 * 10 = 20\n3 * 10 = 30\n4 * 10 = 40\n5 * 10 = 50\n6 * 10 = 60\n7 * 10 = 70\n8 * 10 = 80\n9 * 10 = 90\n10 * 10 = 100'


def test_multi_table_with_2():
    assert multi_table(
        2) == '1 * 2 = 2\n2 * 2 = 4\n3 * 2 = 6\n4 * 2 = 8\n5 * 2 = 10\n6 * 2 = 12\n7 * 2 = 14\n8 * 2 = 16\n9 * 2 = 18\n10 * 2 = 20'
