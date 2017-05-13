def viterbi(str):
    T = len(str)
    Vtable = []
    backtrace = []

    for i in range(T+1):
        scores = []
        states = []
        for j in range(3):
            if i == 0  and j == s_0:
                