from q3 import count_pattern

def test_case_insensitive_overlap():
    assert count_pattern("AbABaBa", "aba") == 3
