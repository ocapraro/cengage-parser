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
  x = re.findall('href="[^-]*-([^"]*)"|<\/rect><g([^g]*)<\/g><[^\/]|<\/rect><use([^\/]*)<\/use><[^\/]', code)
  char_values = []
  for i in x:
    if i[0]:
      char_values.append(i[0])
    elif i[1] or i[2]:
      char_values.extend(strip_code(i[1] or i[2]))
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

def common_sense(equation:str)->str:
  '''
  A function that implements certain common sense formatting into the equation.

  Args:
  equation(str): the equation to be changed.

  Returns:
  str: the modified equation.
  '''
  for match in re.findall('([a-z])([0-9])',equation):
    equation = re.sub('([a-z])([0-9])',match[0]+"^"+match[1],equation,1)
  return equation
  


def main():
  # code = input("paste mathjax here: ")
  code = """
<svg xmlns:xlink="http://www.w3.org/1999/xlink" width="13.998ex" height="5.351ex" viewBox="0 -1446.1 6027 2303.9" role="img" focusable="false" style="vertical-align: -1.992ex;"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><use xlink:href="#MJMATHI-79" x="0" y="0"></use><use xlink:href="#MJMAIN-3D" x="778" y="0"></use><g transform="translate(1837,0)"><g transform="translate(120,0)"><rect stroke="none" width="3949" height="60" x="0" y="220"></rect><g transform="translate(1033,676)"><use xlink:href="#MJMAIN-73"></use><use xlink:href="#MJMAIN-69" x="397" y="0"></use><use xlink:href="#MJMAIN-6E" x="679" y="0"></use><use xlink:href="#MJMATHI-74" x="1518" y="0"></use></g><g transform="translate(60,-686)"><use xlink:href="#MJMAIN-31" x="0" y="0"></use><use xlink:href="#MJMAIN-2B" x="725" y="0"></use><g transform="translate(1729,0)"><use xlink:href="#MJMAIN-74"></use><use xlink:href="#MJMAIN-61" x="392" y="0"></use><use xlink:href="#MJMAIN-6E" x="896" y="0"></use></g><use xlink:href="#MJMATHI-74" x="3464" y="0"></use></g></g></g></g></svg>
  """
  stripped_code = strip_code(code)
  # print(stripped_code)
  translated = translate(stripped_code)
  print(translated)
  common_sense_added = common_sense(translated)
  print(common_sense_added)

if __name__ == "__main__":
  main()