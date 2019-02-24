""" 
    This is a command line game that similates a Madlib game.  It prompts the user
    for a series of words to fit each required component of a Madlib template.  The
    user input responses will be used to populate the template in the proper position.
    The Madlib is displayed to the user on the command line.  It is also written to an
    output file.

    This program utilizes Python’s built in capabilities for reading and writing files 
    and the regex module that will be used to do pattern string search and replacement.
"""
import re

# Inserts the user responses into the Madlib template string
def create_mad_lib_story(mad_lib_template, responses):
    """
    Summary of create_mad_lib_story function:  The user input responses will be used to populate the template in the proper position.

    Parameters:
    mad_lib_template (string): Madlib template from input file
    responses (array): the responses entered by user
    
    Returns:
    madlib_result (string): a string containing the Madlib template with user input reponses placed in the proper position of the template.
    """
    
    madlib_result = mad_lib_template

    prompts = re.findall(r'{[^}]+}', mad_lib_template)

    # The regex sub function is invoked to replace the matching prompt in the
    # Madlib string with the user input.  It replaces just the first occurence
    # of the matching prompt.  The madlib result string is recreated each time.
    for i in range(len(responses)):
        madlib_result = re.sub(prompts[i], responses[i], madlib_result, 1)

    return madlib_result

# Extract the prompts from the template using a regular expression which will find all of the prompts inside of the {} characters.  
def get_prompts(template):
    """
    Summary of get_prompts function: extracts the prompts from the template using a regular expression which will find all of the prompts inside of the {} characters.    

    Parameters:
    template (string): the Madlib template

    Returns:
    prompts (array): an array of strings containing the prompts from the Madlib template
    """

    prompts = re.findall(r'{[^}]+}', template)

    return prompts

# Displays a welcome message to user giving a brief description of Madlib.  Prompts the user 
# for a series of words to fit each required component of a Madlib template and returns
# the reponses
def get_responses(prompts):
    """
    Summary of get_responses function: displays a welcome message to user giving a brief description of Madlib.  Prompts the user for a series of words to fit each required component of a Madlib template.  

    Parameters:
    prompts (array): an array of strings containing the prompts (e.g. adjectve, noun) from the Madlib template

    Returns:
    user_responses (array): an array of strings that contain the user responses to the prompts
    """

    MESSAGE = f"""
        *****************************************************************************
        **                                                                         **
        **                          Welcome to Madlib                              **
        **                                                                         **
        **  This is command line game which prompts the user for a list of words   **
        **  (e.g. adjective, name, pronouns).  These words will be used to         **
        **  create a Madlib story which will be displayed on the command line.     **
        **                                                                         **
        *****************************************************************************
        """

    print(MESSAGE)

    user_responses = []
    for prompt in prompts:
        # For each prompt string in the list of prompt strings scan for the regular 
        # expression pattern.  The pattern is the characters inside the {} characters.
        found = re.search(r'{(.*)}', prompt)

        # Prompt user for responses.  Use the regular expression group to display
        # the prompt to the user. 
        print('Please enter a -> ' + found.group(1).lower() + ': ', end='')
        new_string = input()

        # Append to array of user reponses
        user_responses.append(new_string)

    return user_responses
    
# Opens input file
def open_file():
    """
    Summary of open_file function:  Opens input file that contains a Madlib template for
    user input.

    Parameters:
    none
    
    Returns:
    int: Returns a string that contains a Madlib template which read from input file.
    """
    with open('sample_template.txt', 'r') as sample_file:
        # count = len(open('sample_template.txt', 'r').readlines())
        file_input_string = sample_file.read()

    return file_input_string

# Creates an output file containing the Madlib template with user responses
def write_file(madlib_result):
    """
    Summary of write_file function:  Writes input string which contains the Madlib response to an output file.

    Parameters:
    madlib_result (string): String containing the Madlib template with user responses
    
    Returns:
    Does an implicit return.
    """
    # Write the mad lib story to output file
    with open('output.txt', 'w') as writer:
        writer.write(madlib_result)

# main
if __name__ == "__main__":

    # Open input file and assign contents into string
    mad_lib_template = open_file()

    # Extract the prompts from the template   
    prompts = get_prompts(mad_lib_template)
    print(str(prompts))

    # Prompt user for responses to the prompts
    response_list = get_responses(prompts)

    # Insert the user responses into the Madlib template string
    madlib_result = create_mad_lib_story(mad_lib_template, response_list)

    write_file(madlib_result)
    print(str(madlib_result))