from module_7_3 import WordsFinder

wf = WordsFinder('file1.txt, file2.txt', ['file3.txt', ('file4.txt', 'file5.txt, file6.txt')])
print(wf.file_names)
for i in wf.file_names:
    print(i)