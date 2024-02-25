import pyshorteners
url= input("Enter URL to shorten:")

shorteners=pyshorteners.Shortener()
shortened_url=shorteners.tinyurl.short(url)

print("shortened URL: ",shortened_url)
