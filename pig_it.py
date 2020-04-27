def pig_it(string):
    result=''
    words=string.split()
    for word in words:
       if word.isalpha():
            result+=word[1:]+word[0]+'zy'+' '
        else:
            result+=word
    return result.strip()

pig_it('Hello world !')
'elloHzy orldwzy !'

'''
Задача: Simple Pig latin
Переместите первую букву каждого слова в конец, затем добавьте 'zy' в конец этого слова.
Оставьте знаки препинания нетронутыми.
>>>pig_it('Hello world !')
'elloHzy orldwzy !'
>>> pig_it('Pig latin is cool')
'igPzy atinlzy sizy oolczy'
'''