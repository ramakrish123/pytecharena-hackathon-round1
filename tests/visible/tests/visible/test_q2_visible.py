from q2 import analyze_list

def test_q2_1():
    assert analyze_list([1,2,3,4,5]) == {
        'sum': 15,
        'mean': 3.0,
        'even_count': 2,
        'odd_count': 3
    }

def test_q2_2():
    assert analyze_list([7]) == {
        'sum': 7,
        'mean': 7.0,
        'even_count': 0,
        'odd_count': 1
    }
