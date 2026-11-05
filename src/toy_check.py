from collections import Counter

corpus = [
    "tôi thích học xử_lý ngôn_ngữ",
    "tôi thích học toán",
    "tôi học xử_lý ngôn_ngữ",
]

uni, bi, tri = Counter(), Counter(), Counter()
hist_bi, hist_tri = Counter(), Counter()

for line in corpus:
    words = line.split()
    # Bigram: thêm 1 <s> đầu câu và </s> cuối câu
    t2 = ["<s>"] + words + ["</s>"]
    for i in range(1, len(t2)):
        uni[t2[i]] += 1                      # chỉ đếm từ được dự đoán (không đếm <s>)
    for i in range(len(t2) - 1):
        bi[(t2[i], t2[i + 1])] += 1
        hist_bi[t2[i]] += 1
    # Trigram: thêm 2 <s> đầu câu
    t3 = ["<s>", "<s>"] + words + ["</s>"]
    for i in range(len(t3) - 2):
        tri[(t3[i], t3[i + 1], t3[i + 2])] += 1
        hist_tri[(t3[i], t3[i + 1])] += 1

V = len(uni)          # kích thước từ điển (đã gồm </s>, không gồm <s>)
N = sum(uni.values()) # tổng số từ được dự đoán

def p_uni(w):
    return uni[w] / N

def p_bi(w1, w2, k=0.0):
    denom = hist_bi[w1] + k * V
    return (bi[(w1, w2)] + k) / denom if denom > 0 else 0.0

def p_tri(w1, w2, w3, k=0.0):
    denom = hist_tri[(w1, w2)] + k * V
    return (tri[(w1, w2, w3)] + k) / denom if denom > 0 else 0.0

def sentence_prob_bi(sentence, k=0.0):
    toks = ["<s>"] + sentence.split() + ["</s>"]
    p = 1.0
    for i in range(1, len(toks)):
        p *= p_bi(toks[i - 1], toks[i], k)
    return p, len(toks) - 1               # (xác suất, số từ được dự đoán)

def perplexity_bi(sentence, k=0.0):
    p, n = sentence_prob_bi(sentence, k)
    return float("inf") if p == 0 else p ** (-1 / n)

print("V =", V, "| N =", N)
print("P_uni(học)              =", round(p_uni("học"), 4))
print("MLE  P(xử_lý|học)       =", round(p_bi("học", "xử_lý"), 4))
print("Lap  P(xử_lý|học)       =", round(p_bi("học", "xử_lý", k=1), 4))
print("Lap  P(toán|học)        =", round(p_bi("học", "toán", k=1), 4))
print("Lap  P(ngôn_ngữ|học)    =", round(p_bi("học", "ngôn_ngữ", k=1), 4))
print("MLE  P(xử_lý|thích học) =", round(p_tri("thích", "học", "xử_lý"), 4))

s = "tôi thích học toán"
print("MLE  P(câu)             =", round(sentence_prob_bi(s)[0], 4))
print("MLE  Perplexity         =", round(perplexity_bi(s), 4))
print("Lap  P(câu)             =", round(sentence_prob_bi(s, k=1)[0], 4))
print("Lap  Perplexity         =", round(perplexity_bi(s, k=1), 4))