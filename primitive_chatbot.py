import random


def chatbot_response(res):
    print(f'Chatbot: {res}')


def chatbot_byebye(arg):
    response="Ты ложися на бочок, сожми руку в кулачок."
    chatbot_response(response)
    return -1


def chatbot_advisor(arg):
    response="Не советуй ничего в этом чате."
    chatbot_response(response)
    return 0


def chatbot_usya(arg):
    usya=random.randint(1,100)
    response="Твои усы длиной "+str(usya)+" см."
    if usya<5:
        response+=" Не расстраивайся, размер не главное!"
    elif usya>90:
        response+=" Да куда тебе столько усов?"
    chatbot_response(response)
    return 0


def chatbot_love_chance(arg):
    lover=arg if arg else "самим собой"
    chance=usya=random.randint(1,100)
    response="Шанс познакомиться с "+lover+" равен "+str(chance)+"%"
    chatbot_response(response)
    return 0
	
def chatbot_print_commands(dict):
    s=''
    #for k in dict.keys:
    s=', '.join(dict.keys())
    response="Команды: "+s
    chatbot_response(response)
    return 0

chatbot_commands={
    "!бб":chatbot_byebye,
    "!советчик":chatbot_advisor,
    "!усы":chatbot_usya,
    "!люблю":chatbot_love_chance,
    "!команды":chatbot_print_commands
}


while True:
    user_input=input()
    print(f'User: {user_input}')
    if user_input.split(' ')[0].startswith('!') and user_input.split(' ')[0] in chatbot_commands:
        arg1=user_input.split(' ')[1] if len(user_input.split(' '))>1 else ''
        #---
        if user_input.split(' ')[0]=='!команды':
            arg1=chatbot_commands
        #---
        if chatbot_commands[user_input.split(' ')[0]](arg1)==-1:
            break
