""" 
    This is a command line game that similates a Madlib game.  It prompts the user
    for a series of words to fit each required component of a Madlib template.  The
    user input responses will be used to populate the template in the proper position.
    the Madlib is displayed to the user on the command line.  It is also written to an
    output file.

    This program utilizes Python’s built in capabilities for reading and writing files 
    and the regex module that will be used to do pattern string search and replacement.
"""
import re

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

def write_file(madlib_result):
    """
    Summary of write_file function:  Writes input string which contains the Madlib response to an output file.

    Parameters:
    madlib_result (string): String containing the Madlib response
    
    Returns:
    Does an implicit return.
    """
    # Write the mad lib story to output file
    with open('output.txt', 'w') as writer:
        writer.write(madlib_result)

    return

def create_mad_lib_story(mad_lib_string, prompts):
    """
    Summary of create_mad_lib_story function:  Displays a welcome message to user
    giving a brief description of Madlib.  Prompts the user for a series of words to fit each required component of a Madlib template.  The user input responses will be used to populate the template in the proper position.

    Parameters:
    mad_lib_string (string): Madlib template from input file
    prompts (string): the prompts (e.g. adjectve, noun) from the Madlib template
    
    Returns:
    madlib_result (string): Returns a string containing the Madlib response with user input reponses placed in the proper position of the template.
    """
    madlib_result = mad_lib_string

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

    for prompt in prompts:
        # print(prompt)
        # For each prompt string in the list of prompt strings scan for the regular 
        # expression pattern.  The pattern is the characters inside the {} characters.
        # Returns an instance of the match.
        found = re.search(r'{(.*)}', prompt)
        # print(found.group(), found.group(1))

        # Prompt user for responses.  Use the regular expression group to display
        # the prompt to the user. 
        print('Please enter a -> ' + found.group(1).lower() + ': ', end='')
        new_string = input()

        # The regex sub function is invoked to replace the matching prompt in the
        # Madlib string with the user input.  It replaces just the first occurence
        # of the matching prompt.  The madlib result string is recreated each time.
        madlib_result = re.sub(prompt, new_string, madlib_result, 1)

    return madlib_result
    
# Open input file and assign contents into string
mad_lib_string = open_file()

# Extract the prompts using a regular expression that finds all of the prompts 
# inside of the {} characters.  
prompts = re.findall(r'{[^}]+}', mad_lib_string)

madlib_result = create_mad_lib_story(mad_lib_string, prompts)

write_file(madlib_result)
print(str(madlib_result))