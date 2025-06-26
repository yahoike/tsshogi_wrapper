import subprocess
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
import pyperclip
import os

# Node.jsスクリプトのパス
NODE_SCRIPT = r"D:\program\tsshogi_wrapper\convert_kifu_to_sfen.js"

def convert_and_copy():
    file_path = filedialog.askopenfilename(
        title="棋譜ファイルを選択してください",
        filetypes=[
            ("すべてのファイル", "*.*"),
            ("KIFファイル", "*.kif"),
            ("KI2ファイル", "*.ki2"),
        ]
    )
    if not file_path:
        return

    try:
        result = subprocess.run(
            ["node", NODE_SCRIPT, file_path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
            creationflags=subprocess.CREATE_NO_WINDOW  # ← これがポイント
        )
        sfen = result.stdout.strip()
        pyperclip.copy(sfen)
        messagebox.showinfo("成功", f"SFENをクリップボードにコピーしました:\n{sfen}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("エラー", f"変換に失敗しました:\n{e.stderr.strip()}")

# GUIは非表示のままファイル選択
root = tk.Tk()
root.withdraw()

convert_and_copy()
