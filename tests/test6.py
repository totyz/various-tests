# Create function get_files(folder: Path) -> List[str]
# which run ls/dir command with folder as param and returns all files and folders in list form.
# Print results one entry after another
# What happens when invalid folder has been passed. How to secure program (in such situation we should get empty list?
import subprocess
from pathlib import Path


def get_files(folder: Path):
    try:
        ret = subprocess.check_output(['ls', '-al', folder]).decode('utf-8').split('\n')
    except subprocess.CalledProcessError:
        ret = []
    return ret

if __name__ == '__main__':
    for el in get_files(Path('/t')):
        print(el)
