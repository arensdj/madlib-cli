from madlib_module import adjective  

def test_madlib_file():
    with open('sample_template.txt', 'r') as fd:
        count = len(open('sample_template.txt', 'r').readlines())
        assert count > 0

# def test_madlib_output():
#     """
#     This is a test function for the test_madlib_output function 
#     Attributes: 
#       mad_lib_template: A string containing the Madlib template.
#       input_reponses: A list of strings representing responses for the Madlib template.
#     Test passes if assert evaluates to true
#     """
#     mad_lib_template_string = 'Make Me A Video Game!  
    
#     I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb} {A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!  What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name's} Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find.'
    
#     responses = ''
#     actual = 
#     expected = 4
#     assert expected == actual