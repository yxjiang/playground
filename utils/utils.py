import argparse
import shutil
import os

parser = argparse.ArgumentParser(description='Copy directory recursively')
parser.add_argument('--destination_path', type=str)
parser.add_argument('--source_path', type=str)

def copy_directory(src, dst):
    if os.path.isdir(src) and not os.path.exists(dst):
        os.mkdir(dst)
    if os.path.isdir(src):
        for subpath in os.listdir(src):
            copy_directory(os.path.join(src, subpath), os.path.join(dst, subpath))
    elif os.path.isfile(src):
        if os.path.islink(src):
            src = os.readlink(src)
        shutil.copy(src, dst)
        

if __name__ == "__main__":
    args = parser.parse_args()
    print('Copy files from [%s] to [%s]' % (args.source_path, args.destination_path))
    copy_directory(args.source_path, args.destination_path)
    print('Copy finished')
