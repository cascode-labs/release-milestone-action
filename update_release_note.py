import datetime
import sys
from typing import List
from pathlib import PurePath


def update_release_note(input_filepath: str, output_filepath: str):
    with open(input_filepath, 'r') as input_file:
        input_lines = input_file.readlines()
    output_lines = _update_file(input_lines, input_filepath)
    with open(output_filepath, 'w') as output_file:
        output_file.writelines(output_lines)


def _update_file(input_lines: List[str], input_filepath: str) -> List[str]:
    today = datetime.datetime.now()
    filepath = PurePath(input_filepath)
    version = filepath.name[1:-3]
    header_lines = [
        f"## {version}\n",
        f"Release Date: {today:%m/%d/%Y}\n",
    ]
    output_lines = list()
    for line in input_lines:
        output_lines.append(line.replace("## ", "### ", 1))
    return header_lines + output_lines


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Error: Wrong number of inputs to update_release_note.py!")
        print(sys.argv)
        print("\nNumber of inputs:")
        print(len(sys.argv))
        sys.exit(1)
    else:
        raw_release_note_filepath = sys.argv[1]
        release_note_filepath = sys.argv[2]
    update_release_note(raw_release_note_filepath, release_note_filepath)
    print("Successfully updated release note!")
