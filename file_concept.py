
fo = open("lok.txt", 'w+')
fo.write("this is first line in lok.txt")
fo.read()
fo.seek(0)
fa = open('lok.txt', 'a+')
fa.write("\nthis is appended line in lok.txt file")
fa.read()
fa.seek(0)
fa.close()

