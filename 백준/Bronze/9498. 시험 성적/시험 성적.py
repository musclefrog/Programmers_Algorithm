try:
    score = int(input())

    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")
except ValueError:
    print("숫자를 입력해주세요.")