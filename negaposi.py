import csv
# 形態素解析
from janome.tokenizer import Tokenizer
tok = Tokenizer()

cols = {4:"夏目"}

# ネガポジ判定関数
def evaluation(tok,text):
  res = {"p":0, "n":0, "e":0}
  words = {"p":"", "n":"", "e":""}
  for t in tok.tokenize(text):
    bf = t.base_form 
    if bf in np_dic:
      r = np_dic[bf]
      if r in res:
        res[r] += 1
        words[r] += bf + " "
  cnt = res["p"] + res["n"] + res["e"]  
  return res,words

# ネガポジ判定辞書を読み込み
np_dic = {}
fp = open("pn.csv", "rt", encoding="utf-8")
reader = csv.reader(fp, delimiter='\t')
for i, row in enumerate(reader):
  name = row[0]
  result = row[1]
  np_dic[name] = result
fp.close

output = []
# コメントファイルを読み込む
fp = open("comment.csv", "rt", encoding="utf-8")
reader = csv.reader(fp, delimiter=',')
for row in enumerate(reader):
  for key in cols:
    comment = row[1][key]
    res,words = evaluation(tok,comment)
    tmp_output = [cols[key],comment,words["p"],words["n"],words["e"],res["p"],res["n"],res["e"]]
    output.append(tmp_output)
fp.close

# CSVファイルに書き込む
with open("output.csv", "w", encoding="utf-8", newline="") as fp:
  writer = csv.writer(fp,delimiter=',')
  writer.writerow(["segment", "comment","positive_words","negative_words","neutral_words","positive_cnt","negative_cnt","neutral_cnt"])
  writer.writerows(output)
