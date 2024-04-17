def solution(sizes):
    short = []
    long = []
    for size in sizes:
        short.append(min(size))
        long.append(max(size))
    return max(short) * max(long)