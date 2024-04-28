with open('file1.txt','r+')as file:
    contents=file.read()
    print('contents before writing:',contents)
    file.seek(0)
    file.write('New content added!\n')
    file.seek(0,2)
    file.write('Additional content appended!')
    file.seek(0)
    updated_contents=file.read()
    print('contents after writing:',updated_contents)
     