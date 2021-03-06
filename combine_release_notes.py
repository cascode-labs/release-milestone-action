import os
import sys


def create_release_note_file(folder_path: str, summary_path: str):
    sorted_files, mapping = _sort_filenames(os.listdir(folder_path), os.path.basename(summary_path))
    print(sorted_files)
    with open(summary_path, "w") as summary_file:
        summary_file.write('Release Notes\n')
        summary_file.write('==============\n\n')
        for version_name in sorted_files:
            full_filename = mapping[version_name]
            with open(os.path.join(folder_path, full_filename), "r") as curr_release_file:
                summary_file.write(curr_release_file.read())
                summary_file.write("\n")
            summary_file.write("---\n\n")


def _sort_filenames(files, summary_filename):
    versions = list()
    version_files = dict()
    for file in files:
        new_name = file
        if new_name != summary_filename:
            try:
                float(file[0])
            except:
                new_name = new_name[1:-3]
            versions.append(str(new_name))
            version_files[new_name] = file
    versions.sort(key=lambda s: list(map(int, s.split("."))))
    return versions[::-1], version_files


"""
def _sort_filenames2(filenames: List[str]):
    filenames.remove("release_notes_summary.md")
    versions = list()
    for filename in filenames:
        try:
            #version = pysemver.parse(filename[1:-3])
            versions.append(version)
        except:
            pass
    versions.sort()
    return versions


def _sort_filename3(filenames: List[str]):
    versions = list()
    version_files = dict()
    for file in files:
        new_name = file.name
        if new_name != "Release_Note_Log.md":
            try:
                float(file[0])
            except:
                new_name = new_name[1:-3]
            versions.append(str(new_name))
            version_files[new_name] = file.name
    versions.sort(key=lambda s: list(map(int, s.split("."))))
    return versions[::-1], version_files
"""


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Error: Wrong number of inputs to combine_release_notes.py!")
        print(sys.argv)
        print("\nNumber of inputs:")
        print(len(sys.argv))
        sys.exit(1)
    else:
        release_notes_folder_path = sys.argv[1]
        release_notes_summary_path = sys.argv[2]

    create_release_note_file(release_notes_folder_path, release_notes_summary_path)
    print("Successfully created full release notes!")
    # print(os.listdir(release_notes_folder_path))
    # print("----------------release_notes directory")
