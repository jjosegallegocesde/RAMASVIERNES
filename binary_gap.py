print('Soy emanuel, Hi!')

def binaryGap(N):
    max_gap = 0
    current_max = 0
    seen_one = False

    while N > 0:
        if N % 2 == 1:        
            seen_one = True
            if current_max > max_gap:
                max_gap = current_max
            current_max = 0
        else:
            if seen_one:
                current_max += 1

        N //= 2

    return max_gap