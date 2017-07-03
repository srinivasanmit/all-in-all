'''
song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
  # =>  WE ARE THE CHAMPIONS MY FRIEND
'''
def song_decoder(song):
    orig_song = ''
    for word in song.split('WUB') :
        if word != '' :
            orig_song += word + ' '
    return orig_song[:-1]

print song_decoder("AWUBBWUBC")
print song_decoder("AWUBWUBWUBBWUBWUBWUBC")
print song_decoder("WUBAWUBBWUBCWUB")

def song_decoder1(song):
    return " ".join(song.replace('WUB', ' ').split())

print song_decoder("AWUBBWUBC")
print song_decoder("AWUBWUBWUBBWUBWUBWUBC")
print song_decoder("WUBAWUBBWUBCWUB")

