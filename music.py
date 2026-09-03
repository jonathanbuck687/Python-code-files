artist = input("Enter a musician: ")
votes = {artist.lower(): 1}
bean = False
while(not artist == "done"):
    artist = input("Enter a musician: ")
    if artist == "done":
        break
    for i in votes:
        if i == artist.lower():
            bean = True
    if (bean):
        votes[artist.lower()] = votes[artist.lower()] + 1
    else:
        votes.update({artist.lower(): 1})
    bean = False
print("\nVotes\n-------------")
for j in votes:
    print(j.lower().title(),":", votes[j])