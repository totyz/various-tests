# Create function get_files(folder: Path) -> List[str]
# which run ls/dir command with folder as param and returns all files and folders in list form.
# Print results one entry after another
# What happens when invalid folder has been passed. How to secure program (in such situation we should get empty list?
from pathlib import Path
from typing import List


def get_files(folder: Path) -> List[str]:
    pass

if __name__ == '__main__':
    print(get_files(Path('/tmp')))
