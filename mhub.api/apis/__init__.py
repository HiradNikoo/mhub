from apis.google import Google

def searchVideo(q):
    return Google().search_youtube(q)
