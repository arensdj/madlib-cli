
import re

def open_file():
    with open('sample_template.txt', 'r') as sample_file:
        count = len(open('sample_template.txt', 'r').readlines())
        file_input_string = sample_file.read()

    return file_input_string

def write_file(madlib_result):
    # Write the mad lib story
    with open('output.txt', 'w') as writer:
        writer.write(madlib_result)

    return

def create_mad_lib_story(mad_lib_string, prompts):
  """
    Summary of create_mad_lib_story function:  

    Parameters:
    mad_lib_string (string): mad lib story from input file
    prompts (string): the prompts in the mad lib story
    
    Returns:
    madlib_result (string): Returns new mad lib story with user reponses
  """

    madlib_result = mad_lib_string

    MESSAGE = f"""
        *****************************************
        **      Welcome to Mad Libs            **
        *****************************************
        """

    print(MESSAGE)

    for prompt in prompts:
        # print(prompt)
        found = re.search(r'{(.*)}', prompt)
        # print(found.group(), found.group(1))

        # Prompt user for responses
        print('Please enter a -> ' + found.group(1).lower() + ': ', end='')
        new_string = input()
        madlib_result = re.sub(prompt, new_string, madlib_result, 1)
        # print(madlib_result)

    return madlib_result
    
# Open input file and assign contents into string
mad_lib_string = open_file()

# Extract the prompts
prompts = re.findall(r'{[^}]+}', mad_lib_string)

madlib_result = create_mad_lib_story(mad_lib_string, prompts)

write_file(madlib_result)

# print(madlib_result)