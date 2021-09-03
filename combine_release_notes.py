import os
from typing import List

def create_release_note_file():
    sorted_files, mapping = _sort_filenames(os.listdir("./release_notes"))
    with open("./source/Release_Note_Log.md", "w") as rewrite:
        rewrite.write('Release Note Log\n')
        rewrite.write('---------------------------------')
        rewrite.close()
    with open("./source/Release_Note_Log.md", "a") as new_file:
        for version_name in sorted_files:
            full_filename = mapping[version_name]
            new_file.write("\n******************************")
            new_file.write("\n### Version: " + version_name + "\n")
            curr_release_file = open("./release_notes/" + full_filename, "r")
            new_file.write(curr_release_file.read())
            new_file.write("\n")
            curr_release_file.close()
    new_file.close()


def _sort_filenames(files):
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

def _sort_filenames2(filenames: List[str]):
    filenames.remove("release_notes_summary.md")
    versions = list()
    for filename in filenames:
        try:
            version = pysemver.parse(filename[1:-3])
            versions.append(version)
        catch:
            pass
    versions.sort()
    return versions


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


if __name__ == '__main__':
    try:
        create_release_note_file()
        print("Successfully created full release notes!")
    except:
        print("Unable to create full release notes. Make sure the milestone titles follow the version scheme of v#.#.#")