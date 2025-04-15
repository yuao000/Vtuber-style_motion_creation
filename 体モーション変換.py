import sys
import csv
import os.path

def isfloat(string):
    try:
        float(string)  # 文字列をfloatにキャスト
        return True
    except ValueError:
        return False

def split_filepath(filepath):
    """
    ファイルパスをディレクトリとファイル名に分割します。

    Args:
        filepath (str): 分割したいファイルパス。

    Returns:
        tuple: (ディレクトリ, ファイル名) のタプル。
            ファイル名が存在しない場合は、ファイル名の部分は空文字列になります。
            ディレクトリが存在しない場合は、ディレクトリの部分は空文字列になります。
    """
    directory, filename = os.path.split(filepath)
    return directory, filename

def extract_values_from_text_file(file_path):
    """
    指定されたテキストファイルから「キー:値」形式のデータを抽出します。

    Args:
        file_path (str): 読み込むテキストファイルのパス。

    Returns:
        dict: 抽出されたキーと値を格納した辞書。
            キーは文字列、値はfloat型に変換されます。
            形式に合わない行は無視されます。
    """
    extracted_data = {}
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            for line in file:
                line = line.strip()  # 行頭と行末の空白を削除
                if '：' in line:
                    key, value_str = line.split('：', 1)  # 最初の ':' で分割
                    try:
                        if isfloat(value_str):
                            value = float(value_str)  # 値をfloat型に変換
                        else:
                            value = value_str
                        extracted_data[key] = value
                    except ValueError:
                        print(f"警告: 行 '{line}' の値 '{value_str}' を数値に変換できませんでした。")
                elif line:  # 空行でない形式に合わない行
                    # print(f"警告: 行 '{line}' は 'キー:値' 形式ではありません。")
                    pass
    except FileNotFoundError:
        print(f"エラー: ファイル '{file_path}' が見つかりませんでした。")
    return extracted_data

def output_sjis_csv(data, filename="output.csv"):
    """
    指定されたデータをSJISエンコーディングでCSVファイルに出力します。

    Args:
        data (list of list): CSVファイルに書き込むデータ (各リストが行を表す)。
        filename (str, optional): 出力するCSVファイルの名前。デフォルトは "output.csv"。
    """
    try:
        with open(filename, 'w', encoding='shift_jis', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
        print(f"CSVファイル '{filename}' を出力しました。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

def read_csv(file_path):
    with open(file_path, 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        # next(reader)  # 1行目をスキップ
        data = list(reader)
        return data

if __name__ == "__main__":
    edata = extract_values_from_text_file("settings.txt")
    
    file_path = sys.argv[1]
    # file_path = "./CameraMotionData.csv"
    data = read_csv(file_path)
    # print(data)
    
    csv_data = []
    head_data = [
                    ['Vocaloid Motion Data 0002'],
                    ['変換後モーション'],
                    ['Motion', 'bone', 'x', 'y', 'z', 'rx', 'ry', 'rz', 'x_p1x', 'x_p1y', 'x_p2x', 'x_p2y', 'y_p1x', 'y_p1y', 'y_p2x', 'y_p2y', 'z_p1x', 'z_p1y', 'z_p2x', 'z_p2y', 'r_p1x', 'r_p1y', 'r_p2x', 'r_p2y']
                ]
    body_data = []
    foot_data = [
                    ['Expression', 'name', 'fact'],
                    ['Camera', 'd', 'a', 'x', 'y', 'z', 'rx', 'ry', 'rz', 'x_p1x', 'x_p1y', 'x_p2x', 'x_p2y', 'y_p1x', 'y_p1y', 'y_p2x', 'y_p2y', 'z_p1x', 'z_p1y', 'z_p2x', 'z_p2y', 'r_p1x', 'r_p1y', 'r_p2x', 'r_p2y', 'd_p1x', 'd_p1y', 'd_p2x', 'd_p2y', 'a_p1x', 'a_p1y', 'a_p2x', 'a_p2y'],
                    ['Light', 'r', 'g', 'b', 'x', 'y', 'z']
                ]
    csv_data.extend(head_data)
    
    i = 0
    for d in data:
        if not d[0].isdigit():
            continue
        
        rx = float(d[6])
        ry = float(d[7])
        rz = float(d[8])
        
        #i+10を基準にする
        
        #頭
        para = edata["頭"]
        addData = [i+7,"頭",0,0,0,rx*para,ry*para,rz*para,20,20,107,107,20,20,107,107,20,20,107,107,20,20,107,107]
        body_data.append(addData)
        
        #首
        para = edata["首"]
        addData = [i+5,"首",0,0,0,rx*para,ry*para,rz*para,20,20,107,107,20,20,107,107,20,20,107,107,20,20,107,107]
        body_data.append(addData)
        
        #上半身
        para = edata["上半身"]
        addData = [i+9,"上半身",0,0,0,rx*para,ry*para,rz*para,20,20,107,107,20,20,107,107,20,20,107,107,20,20,107,107]
        body_data.append(addData)
        
        #上半身2
        para = edata["上半身2"]
        addData = [i+11,"上半身2",0,0,0,rx*para,ry*para,rz*para,20,20,107,107,20,20,107,107,20,20,107,107,20,20,107,107]
        body_data.append(addData)
        
        #センター
        para = edata["センター"]
        addData = [i+14,"センター",0,0,0,rx*para,ry*para,rz*para,20,20,107,107,20,20,107,107,20,20,107,107,20,20,107,107]
        body_data.append(addData)
        
        #左腕
        para = edata["左腕"]
        addData = [i+14,"左腕",0,0,0,-ry*para,-rx*para,-edata["腕のZ回転"]-rz*para,20,20,107,107,20,20,107,107,20,20,107,107,20,20,107,107]
        body_data.append(addData)
        
        #右腕
        para = edata["右腕"]
        addData = [i+14,"右腕",0,0,0,ry*para,rx*para,edata["腕のZ回転"]+rz*para,20,20,107,107,20,20,107,107,20,20,107,107,20,20,107,107]
        body_data.append(addData)
        
        #左肩
        para = edata["左肩"]
        addData = [i+15,"左肩",0,0,0,-ry*para,-rx*para,-rz*para,20,20,107,107,20,20,107,107,20,20,107,107,20,20,107,107]
        body_data.append(addData)
        
        #右肩
        para = edata["右肩"]
        addData = [i+15,"右肩",0,0,0,ry*para,rx*para,rz*para,20,20,107,107,20,20,107,107,20,20,107,107,20,20,107,107]
        body_data.append(addData)
        
        
        i += 1
    
    if edata["トリミング"] == "ON":
        for d in body_data:
            if d[0] >= 19:
                d[0] -= 19
                csv_data.append(d)
    else:
        csv_data.extend(body_data)
    csv_data.extend(foot_data)
    # CSVファイルを出力
    out_file_path = split_filepath(file_path)[0]+"/outputdata.csv"
    output_sjis_csv(csv_data, out_file_path)