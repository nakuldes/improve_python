# Finding happy number

class HappyNumber:
    # input n - positive integer
    # output - bool
    def code_snippet(n:int):
        try:
            # start your code from here
            print('Given Number is :\t{0}'.format(n))
            sad = True
            out_list = []
            def get_square_sum_digits(n):  
                d = 0
                exp_alg = ''
                while (n!=0):
                    c = n%10 
                    n = n//10
                    d = d + c*c
                    exp_alg += '+ {0}*{0} '.format(c)
                exp_alg += ' = {0}'.format(d)
                print(exp_alg[1:])
                return d #New number may be 'Happy' one
            def is_happy(n, sad):
                while(sad):
                    if out_list.__contains__(n):
                        break
                    if not out_list.__contains__(n):    
                        out_list.append(n)
                    if n == 1:
                        # Happy number found
                        print('happy number :)')
                        return True 
                    else:
                        n = get_square_sum_digits(n)
                print('Not happy Number :(')
                return False

            return is_happy(n, sad)


        except Exception as e:
            print('*Falied with below Error*\n{0}'.format(e.__doc__))
            return False


if __name__ == '__main__':
    res = HappyNumber.code_snippet(91)
    if(res):
        print('This is Happy number... :)')
    else:
        print('not happy :(')
    print('_'*85)