import sys
import os
import shutil
from os.path import walk, join, normpath
import hashlib
import argparse
import random
import uuid

# config filters list, and files or folders which in the list will be excluded
filters = ['.git', '.svn', '.DS_Store', '.idea']
def visit(arg, dirName, names):
    for name in filters:
        if name in names:
            names.remove(name)
    new_dir = dirName[len(newDir) + 1:]
    old_dir = os.path.join(oldDir, new_dir)
    dst_dir = os.path.join(dstDir, new_dir)

    if os.path.isdir(old_dir):
        for file in names:
            src = os.path.join(dirName, file)
            old = os.path.join(old_dir, file)
            dst = os.path.join(dst_dir, file)
            if os.path.isfile(src) and ( not os.path.exists(old) or os.path.isfile(old)):
                    if hash_file(src) != hash_file(old):
                        if not os.path.isdir(dst_dir):
                            os.makedirs(dst_dir)
                        shutil.copy2(src, dst)
                        print "file %s copy successfull" % src
            elif os.path.isdir(src) and not os.path.isdir(old):
                if not os.path.isdir(dst):
                    os.makedirs(dst)
    else:
        if not os.path.isdir(dst_dir):
            os.makedirs(dst_dir)
        for file in names:
            src = os.path.join(dirName, file)
            old = os.path.join(old_dir, file)
            if os.path.isfile(src) and hash_file(src) != hash_file(old):
                if not os.path.isdir(dst_dir):
                        os.makedirs(dst_dir)   
                shutil.copy2(src, os.path.join(dst_dir,file))
                print "file %s copy successfull" % src

def hash_file(filepath):
    hasher = hashlib.sha1()
    if os.path.isfile(filepath):
        with open(filepath, 'rb') as f:
            while True:
                buf = f.read(0x100000)
                if not buf:
                    break
                hasher.update(buf)
    else:
        hasher.update(str(uuid.uuid4()))
    return hasher.hexdigest()

# parsing arguments
parser = argparse.ArgumentParser(description = "Directories to compare. and copy difference to destination folder")
parser.add_argument("oldDir")
parser.add_argument("newDir")
parser.add_argument("dstDir")

args = parser.parse_args()

if not os.path.isdir(args.oldDir):
    print(args.oldDir + " is not a valid directory")
    exit(-1)
if not os.path.isdir(args.newDir):
    print(args.newDir + " is not a valid directory")
    exit(-1)
if not os.path.isdir(args.dstDir):
    os.makedirs(args.dstDir)
    
oldDir = args.oldDir
newDir = args.newDir
dstDir = args.dstDir
walk(newDir, visit, 0)