#%%
import re
from posixpath import split, splitext
from janome.tokenizer import Tokenizer
from janome import tokenfilter, charfilter
from janome.analyzer import Analyzer
import markovify



origin_text = ''  #origin_textを宣言

#ーーーーーファイルを開くーーーーーーー
with open('text/manga.txt' , mode="r" , encoding="utf-8") as f:
  manga_word = f.read()  

# print(manga_word)

#ーーーー基本的な前処理ーーーーーーーー
manga = re.sub("[！ 、]" , "" , manga_word)

#ーーーー特定ワードの除去ーーーーーーー
manga = manga.replace("である", "")
manga = manga.replace("これ", "")
manga = manga.replace("クセ", "")
manga = manga.replace("んで", "")

# print(manga)

# 解析
# #固有名詞の結合
# token_filters =[tokenfilter.CompoundNounFilter()]
# t = Tokenizer()

# analyzer = Analyzer(tokenizer= t , token_filters=token_filters)

# for mangaword in analyzer.analyze(manga):
#   print(mangaword)


#解析
#単語の出現頻度
# token_filters = [tokenfilter.TokenCountFilter()]
# t = Tokenizer()

# analyzer = Analyzer(tokenizer= t , token_filters=token_filters)

# for mangaword, count in analyzer.analyze(manga):
#   print(mangaword,count)


#ーーーー分かち書きーーーーー
def split_text(text):
  t = Tokenizer()
  token = t.tokenize(text, wakati=True)

  split_text_list = []

  for i in token:
    if i =='。':
        i = '\n'
    elif i != '。':
        i +=' ' #ここ大事,半角スペ-スを単語毎に無いとnoneになってしまう。

    split_text_list.append(i)
    split_text_str = "".join(split_text_list)

  return split_text_str

##確認
# print(split_text(manga))

##ーーーーーーマルコフ連鎖model定義ーーーーーー
##戻り値を格納
split_text_str = split_text(manga)

##markomodel  state_size=繋ぐ数
marko_model = markovify.NewlineText(split_text_str, state_size=2)

#ーーー(tries= 連鎖回数(何回施行するか))ーーーーー
for i in range(1):
  origin_text = marko_model.make_sentence(tries=200)

print("-------------------------")  
print(origin_text)
print("-------------------------")


# %%
