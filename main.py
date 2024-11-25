users:list=[
    {'name':'Patrycja','posts':1,'city':'Warszawa'},
    {'name':'Dominik','posts':3,'city':'Poznań'},
    {'name':'Szymon z wąsem','posts':5,'city':'Toruń'},
    {'name':'Szymon','posts':7,'city':'Łódź'},
    {'name':'Patryk','posts':9,'city':'Kielce'},
    {'name':'Kinga','posts':3,'city':'Gdynia'},
    {'name':'Dominik','posts':8,'city':'Sosnowiec'},
    {'name':'Michał','posts':94,'city':'Białystok'},
    {'name':'Żerom','posts':92,'city':'Wrocław'},
    {'name':'Amelia','posts':999,'city':'Kraków'},


]
print(f'Witaj {users[0]['name']}!!')
for user in users[1:]:
    print(f'twój znajomy {user['name']}, {user['city']}, opublikował {user['posts']} postów')
# for idx,_ in enumerate(users[1:]):
#     print(f'twój znajomy {users[idx]}, opublikował {postow[idx]} postów')
