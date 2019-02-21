
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

mad_lib_string = open_file()

matches = re.findall(r'{[^}]+}', mad_lib_string)

MESSAGE = f"""
    *****************************************
    **      Welcome to Mad Libs            **
    *****************************************
    """

print(MESSAGE)

madlib_result = mad_lib_string
for match in matches:
    #    print(match)
    found = re.search(r'{(.*)}', match)
    # print(found.group(), found.group(1))
    print('Please enter a -> ' + found.group(1).lower() + ': ', end='')
    new_string = input()
    madlib_result = re.sub(match, new_string, madlib_result, 1)
    # print(madlib_result)

write_file(madlib_result)

print(madlib_result)