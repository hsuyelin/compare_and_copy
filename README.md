# compare_and_copy
This python script will compare two folders. and copy differences which in new folder to destination folder

* displaying filenames which added in new folder.
* computing secure hashes to find and display common files whose content differ.
* the first and second folder had better created in advance. or script show error in terminal.
* the third folders can be created without prior.


usage: compare_and_copy.py [-h] oldDir newDir dstDir

positional arguments:

* oldDir
* newDir
* dstDir

optional arguments:
  -h, --help  show this help message and exit

example usage:
python compare_and_copy.py test1 test2 test3
