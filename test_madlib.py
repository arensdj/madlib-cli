from madlib_module import create_mad_lib_story

def test_madlib_template():
    with open('output.txt', 'r') as sample_output_file:
        expected = sample_output_file.read()

    with open('sample_template.txt', 'r') as sample_template_file:
        template = sample_template_file.read()

    with open('test_input.txt', 'r') as sample_input_file:
        responses = sample_input_file.read().split(', ')

    actual = create_mad_lib_story(template, responses)

    assert actual == expected 
