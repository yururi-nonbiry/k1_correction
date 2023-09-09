# K1 3Dプリンタの補正トライ用

## 内容
G-codeを書き換えて補正をかけるプログラムです

## 使い方
同じ階層に[input]フォルダと[output]フォルダを作成してください  
inputフォルダに入っているG-cordを変換します  

## iniファイル
iniファイルは下記の通りです  
  
[path]  
input=./input # ここに変換するGcodeを入れる  
output=./output # ここに変換後のものが出力される  
  
[parameter]  
x_inclination=0.0 # X軸を傾ける  
y_inclination=0.0 # Y軸を傾ける  
x_scaling=1.0 # X軸方向の伸縮  
y_scaling=1.0 # Y軸方向の伸縮  
x_diagonal=1.0 # 未使用  
y_diagonal=1.0 # 未使用  
z_shift=0.0 # Z軸補正値  

## 注意事項
このプログラムを使用して生じたありとあらゆる事象について責任は負いません。
各自、自己責任で使用できる場合のみ使用してください