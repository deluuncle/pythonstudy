import argparse
import os

def batch_rename(work_dir,old_ext,new_ext):
    for filename in os.listdir(work_dir):
        split_file = os.path.splittext(filename)
        root_name,file_ext = split_file
        if old_ext == file_ext:
            newfile = root_name + new_ext
            os.rename(
                os.path.join(work_dir,filename),
                os.path.join(work_dir,newfile)

            )

    print("rename is done")
    print(os.listdir(work_dir))


def get_parse():
    parser = argparse.ArgumentParser(description='change extentisoin of files in a wrking directory')
    