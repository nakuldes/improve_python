import configparser
import gc

class ParserHelper:
    #Static variable
    number_of_objects = 0

    @staticmethod
    def display_objects():
        print(ParserHelper.number_of_objects)


    def __init__(self):
        ParserHelper.number_of_objects+=1
    
    def createINIfile(self, config, filename):
        """
        Funtion to create INI file with config object
        returns nothing
        """
        with open(filename, 'w') as configfile:
            config.write(configfile)
            print('file created successfully')

    def readINIfile(self, config, filename):
        content = config.read(filename)
        print(content)

    def displaySectionAndKeys(self, config):
        for section in config.sections():
            print(section)
            for key in config[section]:
                print('\t'+key)
            print()
    def __del__(self):
        print("deleting objects")

if __name__=='__main__':
    print("Running parserHelper")
    config = configparser.ConfigParser()

    config['Default'] = {
    'Server': 'azntahc01p',
    'IP': '192.168.1.1',
    'Port': 5985
    }
    config['custom'] = {}
    config['custom']['user'] = 'hg'

    config['Default']['auth'] = 'Yes'

    config.set('Default', 'proxy', 'no')

    object1 = ParserHelper()
    object1.createINIfile(config, 'params.ini')
    object1.readINIfile(config, 'params.ini')

    ParserHelper.display_objects()

    print(gc.isenabled())


