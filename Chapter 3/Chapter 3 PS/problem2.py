# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

letter = '''Dear <|Name|>, #it means triple ' can be used in code too. It's not only the multiline comments.
You are selected in FC Barcalona!
<|Date|>'''

print(letter.replace("<|Name","Halland").replace("<|Date|>","27 September, 2026")) #we can do chaining of replace() like here