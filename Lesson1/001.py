# coding: cp1251

# ?????? 1. ???????? ?????????, ??????? ????????? ?? ???? ?????, ???????????? ???? ??????, ? ??????? ???????? ????? ??? ??????.
# 1 ?> ???????????
# 10 ?> ??? ?????? ???
# 7 ?> ???????????

day = int(input("??????? ????? ??? ??????: "))
days = ["???????????", "???????", "?????",
        "???????", "???????", "???????", "???????????"]

if 0 < day < 8:
    print(days[day - 1])
else:
    print("?????? ??? ?? ??????????")
