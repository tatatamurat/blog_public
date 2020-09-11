# blog_public
## file_util.py
### ファイル名変更
python file_util.py "c:\xyz\" プレフィックス（変更前） プレフィックス（変更後）
最後の\も忘れずに設定すること。
指定したプレフィックスの連番ファイルを変更後のプレフィックスのファイル名に変更する。
## image_util.py
### 画像切り取り
python image_util.py "c:\xyz\target.png" [L|R] (--overwrite)
指定した画像ファイルの左または右半分を切り取って保存する。
--overwriteをつけると指定したファイルを上書きし、つけない場合はc:\xyz\target_L.pngのように新規ファイルとして保存する。