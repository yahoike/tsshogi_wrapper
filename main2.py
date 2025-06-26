import subprocess
import os

# 親ディレクトリを指定（ここが「詰将棋」フォルダ）
parent_folder = r"D:\Temp\kif\詰将棋3"

# Node.js スクリプトのパス
node_script = r"D:\program\tsshogi_wrapper\convert_kifu_to_sfen.js"

# 親ディレクトリ内のサブフォルダを走査
for subfolder in sorted(os.listdir(parent_folder)):
    subfolder_path = os.path.join(parent_folder, subfolder)
    if not os.path.isdir(subfolder_path):
        continue  # フォルダでないものは無視

    # 出力ファイル名を決定（例: 本1.sfen）
    output_txt = os.path.join(parent_folder, f"{subfolder}.sfen")

    # .ki2 / .kif ファイルを取得
    kifu_files = [f for f in os.listdir(subfolder_path) if f.endswith((".ki2", ".kif"))]
    kifu_files.sort()

    if not kifu_files:
        print(f"{subfolder} → 棋譜ファイルなし")
        continue

    with open(output_txt, "w", encoding="utf-8") as out:
        for kifu_file in kifu_files:
            file_path = os.path.join(subfolder_path, kifu_file)
            try:
                result = subprocess.run(
                    ["node", node_script, file_path],
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    encoding="utf-8"
                )
                sfen = result.stdout.strip()
                out.write(sfen + "\n")
                print(f"{subfolder}/{kifu_file} → OK")
            except subprocess.CalledProcessError as e:
                print(f"{subfolder}/{kifu_file} → エラー: {e.stderr.strip()}")
