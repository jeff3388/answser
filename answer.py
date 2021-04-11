
# (A)請寫一個程式把裡面的字串反過來。
# (B)請寫一個程式把裡面的字串,每個單字本身做反轉,但是單字的順序不變。

words = "ymedacaiynuj"
word_list = [word for word in words]
word_list.reverse()

result = "".join(word_list)
print(result)

ls = "flipped class room is important"

result_ls = []
if ' ' in ls:
    word_ls = ls.split(' ')

    for words in word_ls:
        word_list = [word for word in words]
        word_list.reverse()
        results = "".join(word_list)
        result_ls += [results]
        
result = " ".join(result_ls)
print(result)


# 請寫一個程式,Input 是一個數字,Output 是從 1 到這個數字,扣除掉所有 3 的
# 倍數以及 5 的倍數,但是需要保留同時是 3 和 5 的倍數的總數字數。


def caculaction_func(val: int):
    result_ls = []
    num_ls = [i for i in range(1, val + 1)]
    for num in num_ls:
        if all([num % 3, num % 5]):
            result_ls += [num]
        elif num == val:
            result_ls += [num]
    
    result = len(result_ls)
    return result

val = 15
result = caculaction_func(val)
print(result)

# 3. 房間裡有三個袋子,一個只裝鉛筆,一個只裝原子筆,第三個有鉛筆也有原子筆。
# 袋子是不透明的,單從袋子的外表上看不出任何差異,你不知道哪個袋子裝什麼。
# 除了袋子上各貼了一個標示("鉛筆"、"原子筆"、"混和"),且標示都是錯的
# (e.g. 標示鉛筆的袋子可能是混和的或是只裝原子筆)。
# 你只能選一個袋子,拿出裡面一支筆,看是鉛筆還是原子筆,然後你要推論出這三
# 個袋子分別的情況。請列出你的作法,以及解釋為什麼這樣可以找到答案。

'''
假設為 A、B、C 袋子
如果我從 A 袋子拿出來為 1 支鉛筆
B、C 袋子其中只有 1 個袋子有 1 原子筆
B、C 袋子可能有個是混合的袋子或者是全都沒有混合的狀況
B、C 袋子可能有一個有裝1支鉛筆情況或者可能全部都沒有

'''


# 4. 有三個人一起到迪士尼遊玩,中午肚子餓了,去餐廳點了一份現在最夯的冰雪奇緣
# 雙人組,要價 900 元,付錢後,服務生發現今天套餐大特價,只要 750 元,因此
# 服務生應該退還 150 元給這三個人,但是這位服務生一時鬼迷心竅,決定暗槓 60
# 元,只退了 90 元給這三個遊客。
# 那麼:三人各出 300 元 - 服務生還給他們一人 30 元 = 三人各出 270 元。270
# 元 × 3 人+ 服務生私吞的 60 元 = 810 + 60 = 870 !? 怎麼不是 900 元呢?還
# 有 30 元去哪了呢?請用敘述的方式,儘量清楚解釋問題出在哪裡。
'''
正常的計算應該是 900 - 90 - 60 = 750

(300 - 30) * 3 - 60 = 750
900 - 90 = 810
題目的計算角度有問題，不應該以總金額 900 塊錢來做計算的基準點

'''

