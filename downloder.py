from pytube import YouTube



class Get_res:
    def __init__(self, vlink):
        self.vlink = vlink
     
    def r_720p(self):
        yt = YouTube(self.vlink)
        return yt.streams.filter(progressive=True, res="720p").last()
    def r_360p(self):
        yt = YouTube(self.vlink)
        return yt.streams.filter(progressive=True, res="360p").last()
    def r_144p(self):
        yt = YouTube(self.vlink)
        return yt.streams.filter(progressive=True, res="144p").last()
    def thumb_nail(self):
        yt = YouTube(self.vlink)
        return yt.thumbnail_url
    


