import subprocess
import os

# フォルダとNode.jsスクリプトのパス
folder_path = r"D:\Temp\kif\fujii_1te"
node_script = r"D:\program\tsshogi_wrapper\convert_kifu_to_sfen.js"

# 出力ファイル
output_txt = os.path.join(folder_path, "sfen_list.txt")

# .ki2 または .kif ファイル一覧を取得（昇順ソート）
kifu_files = [f for f in os.listdir(folder_path) if f.endswith((".ki2", ".kif"))]
kifu_files.sort()

# 一括変換してテキスト出力
with open(output_txt, "w", encoding="utf-8") as out:
    for kifu_file in kifu_files:
        file_path = os.path.join(folder_path, kifu_file)
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
            print(f"{kifu_file} → OK")
        except subprocess.CalledProcessError as e:
            print(f"{kifu_file} → エラー: {e.stderr.strip()}")
