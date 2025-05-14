import platform

if platform.system() == "Windows":
        pathToHosts=r"C:\Windows\System32\drivers\etc\hosts"
elif platform.system() == "Linux":
        pathToHosts=r"/etc/hosts"

redirect="127.0.0.1"
websites=["www.google.com","www.youtube.com","www.facebook.com","www.instagram.com","www.twitter.com","www.linkedin.com","www.github.com","www.stackoverflow.com","www.quora.com","www.reddit.com","www.medium.com","www.wikipedia.org","www.amazon.com","www.apple.com","www.microsoft.com","www.adobe.com","www.spotify.com","www.netflix.com","www.hulu.com","www.disneyplus.com","www.hbo.com","www.showtime.com","www.starz.com","www.peacock.com","www.apple.com","www.microsoft.com","www.adobe.com","www.spotify.com","www.netflix.com","www.hulu.com","www.disneyplus.com","www.hbo.com","www.showtime.com","www.starz.com","www.peacock.com"]

with open(pathToHosts,'r+') as file:
    content=file.read()
    for site in websites:
        if site in content:
            pass
        else:
            file.write(redirect+" "+site+"\n")
            