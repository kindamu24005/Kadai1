#再帰関数の例題　nまでの整数の和
def total(n):
    if n < 1: #終了条件
        return 0

    return n + total(n - 1) #n-1回目の解を使ってn回目の解を求める(漸化式の考え方)