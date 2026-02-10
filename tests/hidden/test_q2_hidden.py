from q2 import analyze_list
import random

def test_large_list():
    nums = [random.randint(-1000, 1000) for _ in range(1000)]
    result = analyze_list(nums)

    assert result['sum'] == sum(nums)
    assert result['even_count'] + result['odd_count'] == len(nums)
