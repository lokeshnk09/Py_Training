# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


def compute():
    n = int(input("Enter the number: "))
    i = 0
    f_v = 0
    s_v = 1
    while i < n:
        if i <= 1:
            Next = i
        else:
            Next = f_v + s_v
            f_v = s_v
            s_v = Next
        print(Next)
        i = i + 1


if __name__ == '__main__':
    compute()