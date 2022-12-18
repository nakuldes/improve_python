import os

def execute_commands(command):
    """
    Run all commands
    """
    print("\nExecuting Command:\n{0}".format(command))
    os.system(command)

if __name__ == '__main__':
    command = 'pip install -r requirements.txt'
    execute_commands(command)