import os

CLI_PATH = os.path.join('src', 'cli.py')
os.system('pipenv shell')
os.system(f'python3 {CLI_PATH}')