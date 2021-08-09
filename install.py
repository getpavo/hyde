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

Run this file from your Pova project to import Hyde automatically.

TODO: Fix overwriting issues with this setup.

(c) 2021 - Job Veldhuis and Hyde collaborators
"""

import shutil
import os
import glob
import pathlib
import re

hyde = str(pathlib.Path(__file__).parent.absolute()) + '/src/'
target = str(pathlib.Path().absolute())

if not os.path.isfile(f'{target}/.povaconfig'):
    raise ImportError('Could not import templates into target: not a project.')

failed_files = []

for file in glob.glob(f'{hyde}/*/*'):
    try:
        resolved_path = str(pathlib.Path(file).resolve())
        file_name = resolved_path.split('/')[-1]
        file_dir = re.search("(?<=\/src\/).*$", resolved_path)[0].split('/')[:-1][0] + '/'
        target_path = f'{target}/{file_dir}'

        if not os.path.exists(f'{target_path}/{file_name}'):
            pathlib.Path(target_path).mkdir(exist_ok=True)
            shutil.copy(resolved_path, target_path)
        else:
            failed_files.append(file)

    except IndexError:
        failed_files.append(file)

if len(failed_files) != 0:
    raise ImportError(f'{len(failed_files)} files failed to copy: {failed_files}')

