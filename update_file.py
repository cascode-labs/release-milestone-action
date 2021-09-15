import datetime
import sys
from typing import List
from pathlib import PurePath


def _update_release_note_contents(input_lines: List[str], input_filepath: str) -> List[str]:
    today = datetime.datetime.now()
    filepath = PurePath(input_filepath)
    version = filepath.name[1:-3]
    header_lines = [
        f"## Version v{version}\n",
        f"Release Date: {today:%m/%d/%Y}\n",
    ]
    output_lines = list()
    for line in input_lines:
        output_lines.append(line.replace("## ", "### ", 1))
    return header_lines + output_lines


def _update_readme_contents(input_lines: List[str], version: str) -> List[str]:
    output_lines = list()
    for line in input_lines:
        if "](https://img.shields.io/badge/v-" in line and \
                line.strip().startswith("![") and \
                line.strip().endswith("-blue)") and \
                line.count("![") == 1:
            output_lines.append(f"![{version}](https://img.shields.io/badge/v-{version}-blue)")
        else:
            output_lines.append(line)
    return output_lines


def update_release_note(input_filepath: str, output_filepath: str):
    input_lines = read_file_lines(input_filepath)
    output_lines = _update_release_note_contents(input_lines, input_filepath)
    write_file_lines(output_filepath, output_lines)


def update_readme(readme_filepath: str, version: str):
    input_lines = read_file_lines(readme_filepath)
    output_lines = _update_release_note_contents(input_lines, version)
    write_file_lines(readme_filepath, output_lines)


def read_file_lines(input_filepath: str) -> List[str]:
    with open(input_filepath, 'r') as input_file:
        return input_file.readlines()


def write_file_lines(output_filepath: str, output_lines: List[str]) -> None:
    with open(output_filepath, 'w') as output_file:
        output_file.writelines(output_lines)


def check_num_inputs(correct_number: int):
    if len(sys.argv) != correct_number:
        print("Error: Wrong number of inputs to update_file.py!")
        print(sys.argv)
        print("\nNumber of inputs:")
        print(len(sys.argv))
        sys.exit(1)


if __name__ == '__main__':
    file_type = sys.argv[1]
    check_num_inputs(3)
    if file_type == "readme":
        readme_filepath = sys.argv[2]
        version = sys.argv[3]
        update_readme(readme_filepath, version)
        print("Successfully updated readme!")
    elif file_type == "release_note":
        raw_release_note_filepath = sys.argv[2]
        release_note_filepath = sys.argv[3]
        update_release_note(raw_release_note_filepath, release_note_filepath)
        print("Successfully updated release note!")
