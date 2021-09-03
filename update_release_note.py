import datetime
from typing import Union, List
from pathlib import PurePath


def update_release_note(input_filepath: str,
                        output_filepath: Union[str, None] = None) -> None:
    with open(input_filepath) as input_file:
        input_lines = input_file.readlines()
    output_lines = _update_file(input_lines, input_filepath)
    with open(output_filepath,'w') as output_file:
        output_file.writelines(output_lines)


def _update_file(input_lines: List[str], input_filepath: str) -> List[str]:
    today = datetime.date()
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
    try:
        update_release_note()
        print("Successfully created full release notes!")
    except:
        print("Unable to create full release notes. Make sure the milestone titles follow the version scheme of v#.#.#")