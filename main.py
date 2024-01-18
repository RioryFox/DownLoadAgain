import vk_api

search_chat = ['Хохочущий Гроб Транзакции']


session_api = vk_session19.get_api()



lol = session_api.messages.getConversations()
lol = lol['items']
for ing in lol:
    ing = ing['conversation']
    if ing['peer']['type'] == 'chat':
        if ing['chat_settings']['title']in search_chat:
            print(ing['peer'], ing['chat_settings']['title'])
