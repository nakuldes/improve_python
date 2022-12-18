import unittest
from adder import AddTwoDigits as ad
import requests
import HtmlTestRunner
import os

class simpletests(unittest.TestCase):
    def setUp(self):
        """
        This is setup
        """
        print("Setup")

    def tearDown(self):
        print("tearDown")

    def test_t1(self):
        self.assertEqual(ad.add(2,4), 6)
    
    # def test_r1(self):
    #     open_url = requests.get("http://127.0.0.1:5000/arm/Nakul")
    #     print(open_url.text)

class pkgTests(simpletests):
    def run_testt1(self):
        self.test_t1()

    def test_r1(self):
        open_url = requests.get("http://127.0.0.1:5000/arm/Nakul")
        print(open_url.text)


if __name__ == '__main__':
    output_dir = os.getcwd() + "\\output\\"
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=output_dir, report_title='Test Report'))
