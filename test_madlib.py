from madlib_module import adjective  

def test_madlib_file():
    with open('sample_template.txt', 'r') as fd:
        count = len(open('sample_template.txt', 'r').readlines())
        assert count > 0

