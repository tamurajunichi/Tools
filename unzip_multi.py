import zipfile
import os
import concurrent.futures
import time

path = './'
files = os.listdir(path)
files_file = [f for f in files if os.path.isfile(os.path.join(path, f))]
files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]

def unzip(zip_file):
    if zip_file in files_dir:
        print("「" + zip_file + ".zip」をスキップ")
    else:
        print("「" + zip_file + ".zip」を展開中...")
        try:
            with zipfile.ZipFile("./" + zip_file +".zip") as existing_zip:
                existing_zip.extractall('./' + zip_file)
        except zipfile.BadZipFile as bze:
            print(bze)
    print("process"+zip_file+'.zip'+"を終了")


def main():
    zip_files = [file.replace('.zip', '') for file in files_file if '.zip' in file]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(unzip, z) for z in zip_files]
        for future in concurrent.futures.as_completed(futures):
            pass

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed_time = time.time() - start
    print("かかった時間:{0}".format(elapsed_time) + "[sec]")