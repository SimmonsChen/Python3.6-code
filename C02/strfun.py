intab = "最"
outtab = "*"
trantab = str.maketrans(intab, outtab)
str1="这是最好的一次体验。"
print (str1.translate(trantab))
