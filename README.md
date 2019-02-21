# madlib-cli
# This is a command line game that similates a Madlib game.  It prompts the user
# for a series of words to fit each required component of a Madlib template.  The
# user input responses will be used to populate the template in the proper position.
# The Madlib is displayed to the user on the command line.  It is also written to an
# output file.

## Challenge
# Given the Madlib templete the challenge was parsing through the template to extract
# all the prompts.  These prompts needed to be displayed to the user so that the 
# user can enter a list of words that fit the prompt (e.g. adjective, noun, name).
# Once the list of responses from the user was collected, another challenge was to
# place each response into the proper location in the Madlib template.

## Approach & Efficiency
# The regex library was used to handle the extraction of the prompts in the Madlib
# template.  The list of prompts was used when prompting the user for a list of
# words (e.g. adjective, noun).  The regex libray was used to replace each prompts
# in the Madlib template with the user response.
 
## Solution
#  