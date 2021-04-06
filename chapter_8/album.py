def make_album(name, album, number=''):
    albums = {'singer': name.title(), 'album': album.title()}
    if number:
        albums['songs'] = number
    return albums

while True:
    print("\n(Enter q for quiting)")
    name = input("Please input the name of singer: ")
    if name == 'q':
        break
    album = input("The name of album: ")
    if album == 'q':
        break
    result = make_album(name, album)
    print(result)
    
