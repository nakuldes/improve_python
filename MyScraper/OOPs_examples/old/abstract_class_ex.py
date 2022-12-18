"""
Create interface TouchScreenLaptop with Scroll and click
child ABCs HP and Dell with Scroll implementation
grandchild class HPNotebook and DellNotebood with click implementation

"""

from abc import abstractmethod, ABC

class TouchScreenLaptop(ABC):
    """
    This is interface
    """
    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass

class Hp(TouchScreenLaptop, ABC):
    def scroll(self):
        print("scrolling HP")

    @abstractmethod
    def click(self):
        pass

class Dell(TouchScreenLaptop, ABC):
    def scroll(self):
        print("scrolling Dell")

    @abstractmethod
    def click(self):
        pass

class HpNotebook(Hp):
    def scroll(self):
        print("scrolling in HP Notebook")

    def click(self):
        print("Click from Hp Notebook")

class DellNotebook(Dell):
       

    def click(self):
        print("Click from Dell Notebook")

if __name__ == '__main__':
    hp = HpNotebook()
    hp.scroll()
    hp.click()
    print('--------------------------------------------------------------------------')

    dell = DellNotebook()
    dell.scroll()
    dell.click()
    
