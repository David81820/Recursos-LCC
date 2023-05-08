```Python

'''
Implemente uma função que calcula quantas sequências de n bits existem onde
não aparecem dois 1s seguidos.
Sugere-se que começe por definir uma função recursiva que calcula quantas 
sequências de n bits começadas por um dado bit existem onde não aparecem 
dois 1s seguidos.
'''


#####################
#        80%        #
#####################
def binario(n):
    if n == 0:
        return 0
    return aux(n-1, 0, {}) + aux(n-1, 1, {})
    
def aux(n, inicial, d):
    if (n, inicial) in d:
        return d[(n, inicial)]
    if n == 1:
        if inicial == 0:
            d[(n, inicial)] = 2
            return 2
        else:
            d[(n, inicial)] = 1
            return 1
        
    if inicial == 0:
        d[(n, inicial)] = aux(n-1, 0, d) + aux(n-1, 1, d)
        return d[(n, inicial)]
    else:
        d[(n, inicial)] = aux(n-1, 0, d)
        return d[(n, inicial)]
    
    
'''
##
# Main function of the Python program.
#
##
from binario import binario
def main():
    print("<h3>binario</h3>")
    print("binario(5) =", binario(5))
    
if __name__ == '__main__':
    main()
##
#
# All tests in the folder "test" are executed
# when the "Test" action is invoked.
#
##
from Root.src.binario import binario
import unittest
class binarioTest(unittest.TestCase):
    def test_binario_0(self):
        with test_timeout(self,1):
            self.assertEqual(binario(5),13)
    def test_binario_1(self):
        with test_timeout(self,1):
            self.assertEqual(binario(10),144)
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