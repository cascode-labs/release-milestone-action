import datetime
import sys
from typing import List
from pathlib import PurePath


def update_release_note(input_filepath: str):
    with open(input_filepath, 'r') as input_file:
        input_lines = input_file.readlines()
    output_lines = _update_file(input_lines, input_filepath)
    with open(input_filepath, 'w') as output_file:
        output_file.writelines(output_lines)


def _update_file(input_lines: List[str], input_filepath: str) -> List[str]:
    today = datetime.datetime.now()
    filepath = PurePath(input_filepath)
    version = filepath.name[1:-3]
    header_lines = [
        f"## {version}",
        f"Release Date: {today:%m/%d/%Y}",
    ]
    output_lines = list()
    for line in input_lines:
        output_lines.append(line.replace("## ", "### ", 1))
    return header_lines + output_lines


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: Wrong number of inputs to combine_release_notes.py!")
        print(sys.argv)
        print("\nNumber of inputs:")
        print(len(sys.argv))
        sys.exit(1)
    else:
        release_note_filepath = sys.argv[1]

    update_release_note(release_note_filepath)
    print("Successfully created full release notes!")
