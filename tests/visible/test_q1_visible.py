from q1 import transform_string

def test_q1_1():
    assert transform_string(" Hello World !") == " hEllO wOrld !"

def test_q1_2():
    assert transform_string(" Python123 ") == " pythOn123 "

def test_q1_3():
    assert transform_string("") == ""
