import configparser
import os



# iniファイル読み込み
def ini_read():
    # グローバル変数
    global input_path
    global output_path

    # 初期化
    ini_file = configparser.ConfigParser()
    ini_file.read("k1_correction.ini", encoding="utf-8")

    # 読み込み
    input_path = ini_file["path"]["input"]
    output_path = ini_file["path"]["output"]

def main():
    # グローバル変数
    global input_path
    global output_path

    # iniファイル読み込み
    ini_read()

    file_list = os.listdir(input_path)
    print(file_list)

    for file_name in file_list:
        with open(file_name, mode="r", encoding="utf-8") as f:
            print(f)



if __name__ == "__main__":
    main()