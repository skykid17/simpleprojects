import webbrowser
url = input("Enter video url: ")
url = url[:12] + "ss" +url[12:]
webbrowser.open(url)