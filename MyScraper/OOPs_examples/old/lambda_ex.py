# This module contains examples of Lambda function
class ExamplesLambda:
    
    def ex_one():
        x = lambda a : a + 10
        print(x(5))
    
    def ex_on_list(outcome):
        yield
        print(outcome)
        

if __name__ == '__main__':
    ExamplesLambda.ex_one()