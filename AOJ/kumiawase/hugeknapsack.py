"""
巨大ナップザック問題

価値が vi 重さが wi であるような N 個の品物と、容量が W のナップザックがあります。次の条件を満たすように、品物を選んでナップザックに入れます：

選んだ品物の価値の合計をできるだけ高くする。
選んだ品物の重さの総和は W を超えない。
価値の合計の最大値を求めてください。

入力
N W
v1 w1
v2 w2
:
vN wN
１行目に２つの整数　N、W が空白区切りで1行に与えられます。 続く N 行に i 番目の品物の価値 vi と重さ wi が空白区切りで与えられます。

出力
価値の合計の最大値を１行に出力してください。

制約
1 ≤ N ≤ 40
1 ≤ vi ≤ 10^15 ←やばい
1 ≤ wi ≤ 10^15 ←やばい
1 ≤ W ≤ 10^15 ←やばい
"""

# 例を取って一つ一つ書いていった方がよくわかる

N,W=map(int,input().split())

# 半分全列挙を使って計算量を減らす
n1 = N // 2
n2 = N - n1

# 半分全列挙で分けた品物を入れるリストを作る
vw1 = [[0, 0]]
vw2 = [[0, 0]]

for _ in range(n1):
  v,w=map(int, input().split())
  for i in range(len(vw1)):
    p=vw1[i][:]
    p[0]+=v
    p[1]+=w
    vw1.append(p)

for _ in range(n2):
  v,w=map(int,input().split())
  for i in range(len(vw2)):
    p=vw2[i][:]
    p[0]+=v
    p[1]+=w
    vw2.append(p)

# 両方のリストをw(重さ)の値でソートする
vw1.sort(key=lambda vw1: vw1[1])
vw2.sort(key=lambda vw2: vw2[1])

# v(価値)については価値の大きさを塗り替えていく
for i in range(len(vw1)-1):
    if vw1[i][0] > vw1[i+1][0]:
        vw1[i+1][0] = vw1[i][0]

for i in range(len(vw2)-1):
    if vw2[i][0] > vw2[i+1][0]:
        vw2[i+1][0] = vw2[i][0]

ans=0
i=0
# 半分に分けた方の一方を逆から回す
for j in range(len(vw1)-1,-1,-1):
    # 品物の重さwが容量Wより大きいときは無視して回す
    if vw1[j][1]>W:
        continue

    # もう一方をリストも要素の分だけ回す
    while i<len(vw2):
        # 両方のリストから取ってきた品物の重さの合計が容量Wを超えたら終わり  
        if vw1[j][1]+vw2[i][1]>W:
            break
        i+=1
    # リストから取った価値の合計が大きい方を答えとして塗り替えていく
    ans=max(ans,vw1[j][0]+vw2[i-1][0])
print(ans)

