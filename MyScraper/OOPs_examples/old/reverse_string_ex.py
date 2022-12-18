class new_class():
    def new_func():
        row = 1
        dig = 1
        for i in range(1, 5, 1):
            print()
            for j in range(row):
                print(str(dig) + " ", end='')
                dig = dig + 1
            row = row + 1

class StringReverse():
    def reverse_string():
        inpt_str = 'string'
        print(inpt_str[::-1])


    


if __name__ == '__main__':
    #new_class.new_func()
    StringReverse.reverse_string()
    ls = ['sys', 'os', 'htmlHelper', 'flask', 'routes', 'start']

    print([f for f in ls if f.startswith('s')])
