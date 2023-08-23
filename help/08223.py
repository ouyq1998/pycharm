searchMap = {
    "a":"a",
    "e":"e",
    "i":"i",
    "o":"o",
    "u":"u",
    "b":"bac",
    "c":"cad",
    "d":"def",
    "f":"feg",
    "g":"geh",
    "h":"hij",
    "j":"jik",
    "k":"kil",
    "l":"lim",
    "m":"mon",
    "n":"nop",
    "p":"poq",
    "q":"qor",
    "r":"ros",
    "s":"sut",
    "t":"tuv",
    "w":"wux",
    "x":"xuy",
    "y":"yuz",
    "z":"zuz"
}

letterList = []
yy = []
for i in range(ord("a"),ord("a")+26):
    letterList.append(i)
for j in "aeiou":
    yy.append(ord(j))
def replaceLetter(letter):
    if letter in "aeiou":
        return letter
    res = letter
    letterIndex = letterList.index(ord(letter))
    diff = 9999
    nextLetter = -1
    for i in yy:
        if diff > abs(ord(letter)-i) :
            nextLetter = i
            diff =min(diff,ord(letter)-i)
    res = res+ chr(nextLetter)
    for j in range(letterIndex+1,26):
        if letterList[j] not in yy:
            res = res+chr(letterList[j])
            break
    if letter=="z":
        res = res+"z"
    return res


if __name__ == '__main__':
    str = "nowcoder"
    res =""
    for i in str:
        res = res+replaceLetter(i)
    print(res)
