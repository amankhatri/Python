__author__ = 'Aman'
#create a file
fw = open('File1.txt','w')
fw.write('This is Line 1 \n')
fw.write('Line 2')
fw.close()

fr = open('File1.txt','r')
text = fr.read()
print(text)
fr.close()