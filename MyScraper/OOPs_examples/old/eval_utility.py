from cmd import Cmd

from sqlalchemy import true

class Autofill(Cmd):
    tools = ['system', 'solar']
    def do_eval(self, tool):
        if tool in self.tools:
            install_tools = tool
        print(install_tools)

    def complete_eval(self, text, line, begidx, endidx):
        if not text:
            completions = self.tools

        else:
            completions = [f for f in self.tools if f.startswith(text)]
        return completions

    def do_EOF(self, line):
        return true

if __name__ == '__main__':
    obj = Autofill()
    obj.cmdloop()