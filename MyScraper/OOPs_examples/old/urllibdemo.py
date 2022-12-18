
import urllib.request

try:
    url = urllib.request.urlopen("https://docs.python.org/3/library/threading.html")

    content = url.read()
    url.close()
    print(content)
except urllib.error.HTTPError:
    print("Page not loaded")
    exit()
