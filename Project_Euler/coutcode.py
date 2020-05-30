
# Return the number of times that the string "code" appears anywhere in the given string,
# except we'll accept any letter for the 'd', so "cope" and "cooe" count.

# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcope') → 2


def count_code(str):
    count = 0

    for i in range(0, int(len(str))):
        if (str[i] == 'c') and (str[i+1] == 'o'):
            if str[i+3] == 'e':
                print(str[i] + str[i+1] + str[i+2] + str[i+3])
                count = count +1

    print(count)


count_code('cozexxcope')




