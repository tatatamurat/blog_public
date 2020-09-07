import glob
import os
import sys

if len(sys.argv) != 4:
    print('引数の数が違います')
    print('usage: python file_util.py [ROOT_PATH] [Before File Prefix] [After File Prex]')
    print('ex) python file_util.py "C:\\xyz\\\\" XXXX YYYY')
    sys.exit(1)

root_path = sys.argv[1]
before_prefix = sys.argv[2]
after_prefix = sys.argv[3]

if not os.path.exists(root_path):
    print('フォルダが存在しません')
    sys.exit(1)

files = glob.glob(root_path + before_prefix + '*')
if len(files) < 1:
    print(root_path + before_prefix + '* のファイルが存在しません')
    sys.exit(1)

files.sort()
i = 1
for f in files:
    os.rename(f, os.path.join(root_path, after_prefix.zfill(4) + '_' + str(i).zfill(3) + '.png'))
    i += 1