def add_songs(*args):
    my_dict = {}
    result = ''
    for i in args:
        song_title = i[0]
        song_lyrics = i[1]
        if song_title not in my_dict:
            my_dict[song_title] = song_lyrics
        else:
            my_dict[song_title].extend(song_lyrics)
    for song, lyrics in my_dict.items():
        result += f"- {song}" + '\n'
        if len(lyrics) > 0:
            for i in range(len(lyrics)):
                result += f"{lyrics[i]}" + '\n'

    return result


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))

print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))

print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
