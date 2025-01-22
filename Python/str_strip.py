#it remove any leading/first and trailing/last cahracters (space is the default leading charecter to remove.)
# syntex=string.strip(character)
url =['https://www.facebook.com','https://www.facebook.com','https://www.google.com']
for ur in url:
    url=ur.strip('htps:/.com')
    print(url)# it can not encriment where it missmass and this loop is stop