```Python

'''
Implemente a função filtra por forma a filtrar as strings que concordam com um padrão.
Uma string concorda com um padrão se for possível obtê-la a partir
do padrão substituindo cada caracter '?' por uma letra e cada caracter '*' por um
número arbitrário de letras. Por exemplo, 'aabxaxb' concorda com o padrão 'a*?b',
enquanto que 'ab' já não.
'''


#####################
#        50%        #
#####################

def encontra(padrao):
    i=0
    
    if padrao=="":
      return 0
    
    for letra in padrao:
        if letra != '*':
            return i
        i+=1
            
    return -1
    
def aceite(padrao, palavra):
    if encontra(padrao)==(-1):
        return 1
        
    elif palavra == "":
        if padrao == "":
            return 1
        else:
            return 0
            
    elif padrao == "":
        return 0
       
    else:
        if padrao[0] == '?':
            r = aceite(padrao[1:], palavra[1:])
        elif padrao[0] == '*':
            res = encontra(padrao)
            r = aceite(padrao[1:], palavra[res:])
        else:
            if(padrao[0] == palavra[0]):
                r = aceite(padrao[1:], palavra[1:])
            else:
                return 0

    return r
    
def filtra(padrao, strings):
    r = []
    if strings==[]:
        return []
    for palavra in strings:
        if aceite(padrao, palavra)== 1:
            r.append(palavra)
        
    return r



#####################
# Solução com regex #
#        80%        #
#####################

import re
    
def filtra(padrao, strings):
    regex = ""
    
    for letra in padrao:
        
        if letra == '?':
            regex += "[a-zA-Z ]"
            
        elif letra == '*':
            regex += "[a-zA-Z ]*"
            
        else:
            regex += letra
            
    regex += "$"
            
    r = []
    
    for string in strings:
        
        y = re.match(regex, string)
        
        if y:
            r.append(string)
        
    return r


'''
##
# Main function of the Python program.
#
##
from filtra import filtra
def main():
    print("<h3>filtra</h3>")
    padrao = "a?*"
    strings = ["abc","aabbc","a","baaa"]
    print("filtra(",padrao,",",strings,") =")
    print(filtra(padrao,strings))
    
if __name__ == '__main__':
    main()
##
#
# All tests in the folder "test" are executed
# when the "Test" action is invoked.
#
##
from Root.src.filtra import filtra
import unittest
class filtraTest(unittest.TestCase):
    def test_filtra_0(self):
        with test_timeout(self,1):
            padrao = "a?*"
            strings = ["abc","aabbc","a","baaa"]
            self.assertEqual(filtra(padrao,strings), ['abc','aabbc'])
    def test_filtra_1(self):
        with test_timeout(self,1):
            padrao = "??a*"
            strings = ["abc","aaabc","aba","baaa"]
            self.assertEqual(filtra(padrao,strings), ['aaabc','aba','baaa'])
if __name__ == '__main__':
    unittest.main()
import time
import signal
class TestTimeout(Exception):
    pass
class test_timeout:
  def __init__(self, test, seconds, error_message=None):
    if error_message is None:
      error_message = 'test timed out after {}s.'.format(seconds)
    self.seconds = seconds
    self.error_message = error_message
    self.test = test
  def handle_timeout(self, signum, frame):
    raise TestTimeout(self.error_message)
  def __enter__(self):
    signal.signal(signal.SIGALRM, self.handle_timeout)
    signal.alarm(self.seconds)
  def __exit__(self, exc_type, exc_val, exc_tb):
    signal.alarm(0)
    if exc_type is not None and exc_type is not AssertionError:
        self.test.fail("execution error")
'''

```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)