from madlib_module import create_mad_lib_story, get_prompts 

def test_madlib_template():
    with open('output.txt', 'r') as sample_output_file:
        expected = sample_output_file.read()

    with open('sample_template.txt', 'r') as sample_template_file:
        template = sample_template_file.read()

    with open('test_input.txt', 'r') as sample_input_file:
        responses = sample_input_file.read().split(', ')

    actual = create_mad_lib_story(template, responses)

    assert actual == expected 

def test_get_prompts():
    with open('sample_template.txt', 'r') as sample_template_file:
        template = sample_template_file.read()

    with open('prompts.txt', 'r') as sample_prompts_file:
        expected = sample_prompts_file.read()

    actual = get_prompts(template)

    # print(str(actual))
    # print()
    # print(str(expected))

    assert actual == expected
