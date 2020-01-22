# -*- Coding: UTF-8 -*-
from wordcloud import WordCloud
import MeCab

STOP_WORDS = [
    "いい", "感じ", "あっ", "使っ", "あり", "やっ", "する", "いる", "なっ",
    "でき", "よう", "てる", "思っ", "さん", "こと", "ところ", "ため", "みよ",
    "なる", "ある", "あがら", "みる", "いえ", "つけ", "せい"
]


def new_wordcloud_client(text):
    return WordCloud(
        background_color="white",
        font_path="/ipaexg.ttf",
        stopwords=set(STOP_WORDS),
        width=900,
        height=500
    ).generate(text)


def text_parser(sentence):
    m = MeCab.Tagger('-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd')
    node = m.parseToNode(sentence)

    words = []
    while node:
        if node.feature.split(',')[0] in ["動詞", "形容詞", "名詞"]:
            words.append(node.surface)
        node = node.next
    return " ".join(words)
