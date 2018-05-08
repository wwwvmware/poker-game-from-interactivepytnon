import random
class card(object):
    def __init__(self, n, c):
        self.num = n
        self.color = c
    def __str__(self):
        return str(self.num) + ',' + str(self.color)
class player(object):
    def __init__(self):
        self.holdpoke = []
class poke(object):
    def __init__(self):
        self.c = card(0, None)
        self.allcard = []
        self.card_color = [1, 2, 2, 4]
    def Creat(self):
        for cardnum in range(1, 14):
            for cardcolor in self.card_color:
                self.c = card(cardnum, cardcolor)
                self.allcard.append(self.c)
class game(object):
    def __init__(self):
        self.num = 0
        self.disnum = []
        self.onecard = 0
        self.deskpoke = poke()
        self.deskpoke.Creat()
        self.playerA = player()
        self.playerB = player()
    def shuffle(self):
        while 1:
            self.onecard = random.randint(0, 51)
            if len(self.disnum) == 52:
                break
            elif self.onecard in self.disnum:
                continue
            else:
                self.disnum.append(self.onecard)
                if self.num % 2 == 0:
                    self.playerA.holdpoke.append(self.deskpoke.allcard[self.onecard])
                if self.num % 2 == 1:
                    self.playerB.holdpoke.append(self.deskpoke.allcard[self.onecard])
                self.num = self.num + 1
        return self.playerB, self.playerA
    def paycard(self, playerpoke):
        n = int(input())
        return n,playerpoke[n]
    def comparepoke(self,bpoke,spoke):
        if bpoke.num>spoke.num:
            return 1
        elif bpoke.num==spoke.num and bpoke.color>spoke.color:
            return 1
        else:
            return 0
    def delcard(self,n,playerspoke):
        del playerspoke[n]
        return playerspoke
g = game()
(a, b) = g.shuffle()
print("一号玩家手牌")
for row in range(len(a.holdpoke)):
    print("第"+str(row)+"张"+str(a.holdpoke[row]),end=" ")
print()
print("二号玩家手牌")
for row in range(len(b.holdpoke)):
    print("第"+str(row)+"张"+str(b.holdpoke[row]),end=" ")
print()
print("请一号玩家出牌")
(an,adeskcard)=g.paycard(a.holdpoke)
a.holdpoke=g.delcard(an,a.holdpoke)
print(adeskcard)
while 1:
    print("请二号玩家出牌")
    for row in range(len(b.holdpoke)):
        print("第" + str(row) + "张" + str(b.holdpoke[row]), end=" ")
    (bn,bdeskcard)=g.paycard(b.holdpoke)
    print(bdeskcard)
    if g.comparepoke(bdeskcard,adeskcard):
     while 1:
        print("请一号玩家出牌")
        for row in range(len(a.holdpoke)):
            print("第" + str(row) + "张" + str(a.holdpoke[row]), end=" ")
        (an, adeskcard) = g.paycard(a.holdpoke)
        print(adeskcard)
        if g.comparepoke(adeskcard,bdeskcard):
            print("请二号玩家出牌")
            for row in range(len(b.holdpoke)):
                print("第" + str(row) + "张" + str(b.holdpoke[row]), end=" ")
            (bn, bdeskcard) = g.paycard(b.holdpoke)
            print(bdeskcard)
            if g.comparepoke(bdeskcard,adeskcard):
                continue
            else:
                print("所出手牌不能小于桌面的牌")
        else:
            print("所出手牌不能小于桌面上的牌")
    else:
        print("所出手牌不能小于桌面上的牌")
