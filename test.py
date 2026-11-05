import os
import py_vncorenlp

BASE_DIR = os.path.abspath(".")
VNCORENLP_DIR = os.path.join(BASE_DIR, "vncorenlp")   # phải là đường dẫn tuyệt đối
os.makedirs(VNCORENLP_DIR, exist_ok=True)

# Chỉ tải lần đầu (nếu đã có model thì bỏ qua)
if not os.path.exists(os.path.join(VNCORENLP_DIR, "VnCoreNLP-1.2.jar")):
    py_vncorenlp.download_model(save_dir=VNCORENLP_DIR)

# Chỉ cần tách từ nên dùng annotators=["wseg"] cho nhanh
segmenter = py_vncorenlp.VnCoreNLP(annotators=["wseg"], save_dir=VNCORENLP_DIR)

text = "Hà Nội là thủ đô của Việt Nam. Hôm nay trời rất đẹp."
result = segmenter.word_segment(text)

print(type(result), len(result))
for i, sent in enumerate(result):
    print(i, "->", sent)