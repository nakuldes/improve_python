"""
This file conetains the list comprehension examples

"""

class ListComprehension:

    def ex1_common_nos(self):
        a = [1,2,3,4,5,6]
        b = [2,4,6,8]

        print(a, b)

        result = [i for i in a if i in b]
        print("Common nos are "+ str(result))

if __name__ =='__main__':
    run_example = ListComprehension()
    run_example.ex1_common_nos()