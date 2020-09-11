import os
import sys

from PIL import Image

def check_args():
    # 引数の数チェック
    arg_len = len(sys.argv)
    if arg_len != 3 and arg_len != 4:
        print('引数の数が違います')
        print('usage: python image_util.py [FILE_PATH] [L|R] (--overwrite)')
        print('ex) python image_util.py "C:\\xyz\\target.png" L')
        sys.exit(1)

    img_path = sys.argv[1]
    img_range = sys.argv[2]
    overwrite_flag = False
    if arg_len == 4 and sys.argv[3] == '--overwrite':
        overwrite_flag = True

    # パス存在チェック
    if not os.path.exists(img_path):
        print('指定したファイルが存在しません')
        sys.exit(1)

    # 切り取り範囲の指定文字チェック
    if not img_range == 'L' and not img_range == 'R':
        print('第2引数にはLまたはRを指定してください')
        sys.exit(1)

    return img_path, img_range, overwrite_flag

def get_image_range(img_range, w):
    if img_range == 'L':
        left = 0
        right = w / 2
    else:
        left = w / 2
        right = w

    return left, right

def get_new_file_path(img_path, img_range, overwrite_flag):

    if overwrite_flag:
        return img_path

    basename_wo_ext = os.path.splitext(os.path.basename(img_path))[0]
    ext = os.path.splitext(os.path.basename(img_path))[1]
    return os.path.dirname(img_path) + '/' + basename_wo_ext + '_' + img_range + ext

img_path, img_range, overwrite_flag = check_args()
img = Image.open(img_path)
w, h = img.size

left, right = get_image_range(img_range, w)

crop_img = img.crop((left, 0, right, h))

new_file_path = get_new_file_path(img_path, img_range, overwrite_flag)
# print(new_file_path)
crop_img.save(new_file_path, quality=95)
