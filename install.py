"""
██░ ██▓██   ██▓▓█████▄ ▓█████
▓██░ ██▒▒██  ██▒▒██▀ ██▌▓█   ▀
▒██▀▀██░ ▒██ ██░░██   █▌▒███
░▓█ ░██  ░ ▐██▓░░▓█▄   ▌▒▓█  ▄
░▓█▒░██▓ ░ ██▒▓░░▒████▓ ░▒████▒
 ▒ ░░▒░▒  ██▒▒▒  ▒▒▓  ▒ ░░ ▒░ ░
 ▒ ░▒░ ░▓██ ░▒░  ░ ▒  ▒  ░ ░  ░
 ░  ░░ ░▒ ▒ ░░   ░ ░  ░    ░
 ░  ░  ░░ ░        ░       ░  ░
        ░ ░      ░

Based on the amazing Hyde for Jekyll by @mdo: https://github.com/poole/hyde

Run this file from your Jackman project to import Hyde automatically.

(c) 2021 - Job Veldhuis and Hyde collaborators
"""

from distutils.dir_util import copy_tree
import pathlib

hyde = str(pathlib.Path(__file__).parent.absolute()) + '/src/'
target = str(pathlib.Path().absolute())
copy_tree(hyde, target)
