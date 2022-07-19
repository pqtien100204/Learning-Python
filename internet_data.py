import urllib.request

def main():
    weburl = urllib.request.urlopen("http://www.google.com") # urlopen() take the string of thee web => open the web. a web-response object
    print("Result code:", weburl.getcode()) # retrieve the result code(i.e: 200-accessable; 404-notfound)
    data = weburl.read() # help reading all the content of the speccified url into the variable named data
    print(data)

main()