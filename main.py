import sys
import os

root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(root, 'src','vendor'))

from src.SwitAC import main

if __name__ == '__main__':
    main()