def hungman(word):
    wrong = 0 #プレーヤーが何回間違えたかカウント
    stages = ["",
              "_______      ",
              "|            ",
              "|     |      ",
              "|     0      ",
              "|    /||     ",
              "|    / |     ",
              "|            "]
    rletters = list(word)#受け取った文字"cat"を分解して1文字ずつのリストにする
    board = ["_"] * len(word)#"cat"の文字数分だけ アンダースコアのリストを作る
    win = False #プレーヤの勝ち負けの状態
    print("ハングマンへようこそ！")

    while wrong < len(stages) -1:#プレーヤがハングマン完成させるまでの間
        print("\n")#見やすくするため改行 → \n
        msg = "１文字を予想してね"
        char = input(msg)#プレーヤに予想文字を入力させる
        if char in rletters:#プレーヤが入力した文字が正解の中にあれば
            cind = rletters.index(char)#入力（正解）された文字が正解の何番目にあるか
            board[cind] = char#入力された正解文字を当てはめる 例：["c", "_", "_"]
            rletters[cind] = '$' #indexメソッドは最初に見つけたインデックス値しか返さないため
                                 # 正解した文字を$に置き換える。こうすると複数同じ文字があっても正常に動く
        else:#プレーヤの入力も字が間違っていた場合
            wrong += 1 #失敗回数のカウントアップ
        print(" ".join(board))#boardの中身を空白" "で結合して表示 例：_ _ t
        e = wrong + 1 #間違った回数 + 1
        print("\n".join(stages[0:e]))#ハングマンの表示 stageリストの0～eまでを改行（\n）しながら表示

        if "_" not in board:#boardのなかに_が無ければ
            print("あなたの勝ち！")
            print(" ".join(board))#boardの中身を空白" "区切りで表示
            win = True #プレーヤの勝ち負け状態：勝ち
            break #ループを終了

    if not win:#ループが終了したときにwinがtrueになっていなかった場合
        print("\n".join(stages[0:wrong+1]))#すべてのハングマンを改行\n区切りで表示
        print("あなたの負け！正解は {}".format(word))#正解を表示

hungman("favorite")#関数hungmanに正解文字を渡す（プログラムスタート）