try:
    # to run exception choose file which is not created
    # to run else(no exceptions) block choose file which is already present.
    file_open = open('lok.txt', 'r')
    file_open.read()
    file_open.seek(0)
    print(file_open.read())


except SyntaxError as e:
    print(SyntaxError, e)

else:
    print("no more exceptons")

finally:
    file_open.close()








