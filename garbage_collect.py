# script to remove old files from the following directories:
#   - /output_data/participation
#   - /output_data/tables
# keeping only the most recent csv in each directory
# run script from root directory of project using command `python garbage_collect.py`


import os


def main():
    # delete all files in output_data/participation except the most recent
    participation_dir = "output_data/participation"
    participation_files = os.listdir(participation_dir)
    participation_files.sort()
    participation_files.reverse()
    for file in participation_files[1:]:
        os.remove(os.path.join(participation_dir, file))

    # delete all files in output_data/tables except the most recent
    tables_dir = "output_data/tables"
    tables_files = os.listdir(tables_dir)
    tables_files.sort()
    tables_files.reverse()
    for file in tables_files[1:]:
        os.remove(os.path.join(tables_dir, file))


if __name__ == "__main__":
    main()
