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
      char_values.append("{")
      char_values.extend(strip_code(i[1] or i[2]))
      char_values.append("}")
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
  for match in re.findall('([a-n|p-z])([0-9])',equation):
    equation = re.sub('([a-n|p-z])([0-9])',match[0]+"^"+match[1],equation,1)
  for match in re.findall('lim([a-z])\\\\to(0|\\\\infty)',equation):
    equation = re.sub('lim([a-z])\\\\to(0|\\\\infty)',"{"+match[0]+"\\\\lim"+match[1]+"}",equation,1)
  return equation
  


def main():
  # code = input("paste mathjax here: ")
  code = """
<span class="equation" id="JWNUDMVM45J4QVZGA551" id-sequence="545"> <div><span class="MathJax_Preview" style="display: none;"></span><div class="MathJax_SVG_Display"><span class="MathJax_SVG" id="MathJax-Element-83-Frame" tabindex="0" style="font-size: 85%; display: inline-block;"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="13.294ex" height="6.083ex" viewBox="0 -1670.1 5723.6 2618.9" role="img" focusable="false" style="vertical-align: -2.204ex;"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><g transform="translate(134,0)"><use xlink:href="#MJMAIN-6C"></use><use xlink:href="#MJMAIN-69" x="281" y="0"></use><use xlink:href="#MJMAIN-6D" x="563" y="0"></use></g><g transform="translate(0,-735)"><use transform="scale(0.8)" xlink:href="#MJMATHI-68" x="0" y="0"></use><use transform="scale(0.8)" xlink:href="#MJMAIN-2192" x="579" y="0"></use><use transform="scale(0.8)" xlink:href="#MJMAIN-30" x="1583" y="0"></use></g><g transform="translate(1669,0)"><g transform="translate(286,0)"><rect stroke="none" width="3647" height="60" x="0" y="220"></rect><g transform="translate(60,676)"><use xlink:href="#MJMAIN-32"></use><use xlink:href="#MJMAIN-2E" x="503" y="0"></use><use xlink:href="#MJMAIN-37" x="785" y="0"></use><use transform="scale(0.707)" xlink:href="#MJMATHI-68" x="1822" y="579"></use><use xlink:href="#MJMAIN-2212" x="2020" y="0"></use><use xlink:href="#MJMAIN-31" x="3024" y="0"></use></g><use xlink:href="#MJMATHI-68" x="1534" y="-686"></use></g></g></g></svg></span></div><script type="math/mml" id="MathJax-Element-83"><m:math xmlns:m="http://www.w3.org/1998/Math/MathML" display="block"> <m:mrow> <m:munder> <m:mi mathvariant="normal">lim</m:mi> <m:mstyle scriptsizemultiplier="0.8"> <m:mrow> <m:mi>h</m:mi> <m:mo>→</m:mo> <m:mn>0</m:mn></m:mrow></m:mstyle></m:munder> <m:mfrac> <m:mrow> <m:msup> <m:mn>2.7</m:mn> <m:mi>h</m:mi></m:msup> <m:mo>-</m:mo> <m:mn>1</m:mn></m:mrow> <m:mi>h</m:mi></m:mfrac></m:mrow></m:math></script></div> <button>TEST TEXT</button></span>
  """
  stripped_code = strip_code(code)
  # print(stripped_code)
  translated = translate(stripped_code)
  print(translated)
  common_sense_added = common_sense(translated)
  print(common_sense_added)

if __name__ == "__main__":
  main()