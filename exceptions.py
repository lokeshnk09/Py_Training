try:
    # to run exception choose file which is not created
    # to run else(no exceptions) block choose file which is already present.
    open_file = open('lok.txt', 'r')
    open_file.read()
    open_file.seek(0)
    print(open_file.read())


except SyntaxError as e:
    print(SyntaxError, e)

else:
    print("no more exceptons")

finally:
    open_file.close()








