# -*- coding: utf-8 -*-
"""Tải VnCoreNLP (jar + models) bằng Python, thay cho wget (Windows không có sẵn).
Chạy: python download_vncorenlp.py   -> tạo thư mục vncorenlp/ cạnh file này.
"""
import os
import urllib.request

BASE = "https://raw.githubusercontent.com/vncorenlp/VnCoreNLP/master/"
FILES = [
    "VnCoreNLP-1.2.jar",
    "models/wordsegmenter/vi-vocab",
    "models/wordsegmenter/wordsegmenter.rdr",
    "models/postagger/vi-tagger",
    "models/ner/vi-500brownclusters.xz",   # chỉ cần nếu dùng ner
    "models/ner/vi-ner.xz",                # chỉ cần nếu dùng ner
    "models/dep/vi-dep.xz",                # chỉ cần nếu dùng parse
]
SAVE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vncorenlp")

for rel in FILES:
    dst = os.path.join(SAVE_DIR, *rel.split("/"))
    if os.path.exists(dst) and os.path.getsize(dst) > 0:
        print("Đã có, bỏ qua:", rel)
        continue
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    print("Đang tải:", rel, "...", flush=True)
    urllib.request.urlretrieve(BASE + rel, dst)
    print("  xong, %.1f MB" % (os.path.getsize(dst) / 1e6))

print("\nHoàn tất. Thư mục:", SAVE_DIR)