import configparser
import os
import math



# iniファイル読み込み
def ini_read():
    # グローバル変数
    global input_path
    global output_path
    global x_inclination
    global y_inclination
    global x_scaling
    global y_scaling
    global z_shift

    # 初期化
    ini_file = configparser.ConfigParser()
    ini_file.read("k1_correction.ini", encoding="utf-8")

    # 読み込み
    input_path = ini_file["path"]["input"]
    output_path = ini_file["path"]["output"]

    x_inclination = math.radians(float(ini_file["parameter"]["x_inclination"])) # ラジアンに変換する
    y_inclination = math.radians(float(ini_file["parameter"]["y_inclination"])) # ラジアンに変換する
    x_scaling = float(ini_file["parameter"]["x_scaling"])
    y_scaling = float(ini_file["parameter"]["y_scaling"])
    z_shift = float(ini_file["parameter"]["z_shift"])


def gcode_str(value):

    result_str = '{:.3f}'.format(value)

    while True:
        if result_str == "0":
            break

        if result_str[-1] == "0":
            result_str = result_str[:-1]
            continue

        if result_str[-1] == ".":
            result_str = result_str[:-1]
            break

        if len(result_str) == 3 and result_str[0] == "0":
            result_str = result_str[1:]
            continue

        break

    return result_str


def correction(data_list):

    global x_inclination
    global y_inclination
    global x_scaling
    global y_scaling
    global z_shift

    result = []

    value_x = 0
    value_y = 0
    value_z = 0

    for data in data_list:

        if data[:1] not in ["G", "M"]:
            #print(data)
            result.append(data)
            continue

        s_data_list = data.split()
        #print(s_data_list)
        
        if s_data_list[0] not in ["G0", "G1", "M205"]:
            continue

        r_sdata = ""

        # 一回値を拾う
        for sdata in s_data_list:

            if sdata[0] == "X":
                value_x = float(sdata[1:]) 

            elif sdata[0] == "Y":
                value_y = float(sdata[1:]) 

            elif sdata[0] == "Z":
                value_z = float(sdata[1:]) 

        # 数値演算
        for sdata in s_data_list:

            if sdata[0] == "X":

                sdata = "X" + gcode_str((float(sdata[1:]) + value_y * math.sin(x_inclination)) * x_scaling) 
                #print(math.sin(x_inclination))

            elif sdata[0] == "Y":

                sdata = "Y" + gcode_str((float(sdata[1:]) + value_x * math.sin(y_inclination)) * y_scaling)
                #print(math.sin(y_inclination))

            elif sdata[0] == "Z":

                sdata = "Z" + gcode_str(float(sdata[1:]) + z_shift) 

            r_sdata += sdata + " "

        r_sdata = r_sdata[:-1] + "\n"
        result.append(r_sdata)

        #print(value_x,value_y,value_z)

    return result


def main():
    # グローバル変数
    global input_path
    global output_path

    # iniファイル読み込み
    ini_read()

    file_list = os.listdir(input_path)
    #print(file_list)

    for file_name in file_list:

        data_list = []

        with open(input_path + "/" + file_name, mode="r", encoding="utf-8") as f:
            data_list = f.readlines()
        
        #print(data_list)

        result = correction(data_list)
        with open(output_path + "/c_" + file_name, mode="w", encoding="utf-8") as f:
            f.writelines(result)



if __name__ == "__main__":
    main()

    