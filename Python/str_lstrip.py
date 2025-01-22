#it remove any leading/first cahracters (space is the default leading charecter to remove.)
# syntex=string.lstrip(character)
url =['https://www.facebook.com','https://www.facebook.com','https://www.google.com']
for ur in url:
    urls=ur.lstrip('htps:/.com')
    print(urls)
for ur in url:
    urlm=ur.lstrip('htps/.com')
    print(urlm) # it can not encriment where it missmass and this loop is stop