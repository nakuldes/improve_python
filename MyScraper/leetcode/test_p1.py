import unittest
import random
from p1 import HappyNumber


class TestHappyNumber(unittest.TestCase):

    def test_01_happy_number(self):
        res = HappyNumber.code_snippet(19)
        assert res == True

    def test_02_sad_number(self):
        res = HappyNumber.code_snippet(4)
        assert res == False

    def test_03_list_of_happy_number(self):
        r_list = []
        for r in range(0, 5):
            n = random.randint(1, 99)
            r_list.append(n)
        print('Below numbers will tested if happy or not\n{0}'.format(r_list))
        for n in r_list:    
            res = HappyNumber.code_snippet(n)
        
            #assert type(res) == 'bool'


if __name__ == '__main__':
    unittest.main()