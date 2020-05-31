import zipfile
import os
import time

start = time.time()
print("***************unzipプログラムを開始します***************")

print("ファイルとフォルダのリストを取得中...")
path = './'
files = os.listdir(path)
files_file = [f for f in files if os.path.isfile(os.path.join(path, f))]
files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]
zip_files = [file for file in files_file if '.zip' in file]

for extract_zipfile in zip_files:
    target = extract_zipfile.replace('.zip','')
    target_folder = './'+target+'/'
    if target in files_dir:
        print("「"+extract_zipfile+"」をスキップ")
    else:
        print("「"+extract_zipfile+"」を展開中...")
        try:
            with zipfile.ZipFile("./"+extract_zipfile) as existing_zip:
                existing_zip.extractall('./'+target_folder)
        except zipfile.BadZipFile as bze:
            print(bze)

print("***************unzipプログラムを終了します***************")
elapsed_time = time.time() - start
print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
