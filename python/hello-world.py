# https://docs.python.org/3/library/unittest.html
# https://docs.python.org/3/library/configparser.html

import configparser

def is_none_or_whitespace(string):
    if string == None:
        return True

    if not isinstance(string, str):
        return False

    if string == '':
        return True

    if string.isspace():
        return True
    
    return False

configfile = 'settings.ini'
config = configparser.ConfigParser()
config.read(configfile)

boolean = bool()
number = int()
floating = float()
text = str()

try:
    boolean = config.getboolean('DEFAULT', 'Boolean', fallback=False)
    number = config.getint('DEFAULT', 'Number', fallback=1)
    floating = config.getfloat('DEFAULT', 'Floating', fallback=1.0)
    text = config.get('DEFAULT', 'Text', fallback="Fallback!")
except ValueError as e:
    print("There are invalid values in the configuration '{0}': {1}".format(configfile, str(e)))

if is_none_or_whitespace(text):
    text = "Another Fallback!"

print(boolean)
print(number)
print(floating)
print(text)