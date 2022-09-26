'''
A module that parses mathjax objects from cengage textbooks into LaTex.

@author Oscar Capraro
'''
import json
import re

CHARACTERS = []
with open('characters.json') as json_file:
  CHARACTERS = json.load(json_file)
# print

def strip_code(code:str)->list:
  '''
  A function that removes the useless code from the mathjax objects.

  Args:
  code(str): the mathjax object

  Returns:
  list: a list of all the character values.
  '''
  x = re.findall('href="[^-]*-([^"]*)"|<\/rect>(.*)<\/g><[^\/]', code)
  char_values = []
  for i in x:
    if i[0]:
      char_values.append(i[0])
    else:
      char_values.extend(strip_code(i[1]))
      char_values.append("rect")
  return char_values

def new_character_entry(character_value:str)->str:
  '''
  Adds a new character to the database.

  Args:
  character_value(str): the value of the character.

  Returns:
  str: the new character.
  '''
  character = input(f"The code \"{character_value}\" was not found, please enter its value: ")
  CHARACTERS.append([character_value,character])
  with open('characters.json', 'w') as f:
    json.dump(CHARACTERS, f)
  return character

def translate(character_values:list)->str:
  '''
  A function that translates a list of character values into characters.

  Args:
  character_values(list): a list of all the character values.

  Returns:
  str: the translated string.
  '''
  translated_string=""
  current_character_values = [i[0] for i in CHARACTERS]
  for character in character_values:
    if character in current_character_values:
      translated_string+=CHARACTERS[current_character_values.index(character)][1]
    else:
      new_character_entry(character)
      return translate(character_values)
  return translated_string
  


def main():
  # code = input("paste mathjax here: ")
  code = """
<svg xmlns:xlink="http://www.w3.org/1999/xlink" width="14.618ex" height="2.742ex" viewBox="0 -911.2 6294 1180.7" role="img" focusable="false" style="vertical-align: -0.626ex;"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><use xlink:href="#MJMATHI-79" x="0" y="0"></use><use xlink:href="#MJMAIN-3D" x="778" y="0"></use><g transform="translate(1837,0)"><use xlink:href="#MJMATHI-78" x="0" y="0"></use><use transform="scale(0.707)" xlink:href="#MJMAIN-32" x="813" y="513"></use></g><use xlink:href="#MJMAIN-2B" x="3091" y="0"></use><g transform="translate(4095,0)"><use xlink:href="#MJMAIN-63"></use><use xlink:href="#MJMAIN-6F" x="447" y="0"></use><use xlink:href="#MJMAIN-74" x="951" y="0"></use></g><use xlink:href="#MJMATHI-78" x="5718" y="0"></use></g></svg>
"""
  stripped_code = strip_code(code)
  # print(stripped_code)
  print(translate(stripped_code))

main()