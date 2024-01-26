from pytube import YouTube



class Get_res:
    def __init__(self, vlink):
        self.vlink = vlink
        self.ytt = YouTube(self.vlink)
        self.yt = self.ytt.streams
    def r_720p(self):
        #yt = YouTube(self.vlink)
        #return self.yt.streams.filter(progressive=True, res="720p").last()
        return self.yt.filter(progressive=True, res="720p").last()
    def r_360p(self):
        #yt = YouTube(self.vlink)
        #return self.yt.streams.filter(progressive=True, res="360p").last()
        return self.yt.filter(progressive=True, res="360p").last()
    def r_144p(self):
        #yt = YouTube(self.vlink)
        #return self.yt.streams.filter(progressive=True, res="144p").last()
        return self.yt.filter(progressive=True, res="144p").last()
    def thumb_nail(self):
        #yt = YouTube(self.vlink)
        return self.ytt.thumbnail_url
    def title(self):
        return self.ytt.title
    def a_128(self):
        return self.yt.filter(progressive=False, type="audio", abr="128kbps").last()
    def a_50(self):
        return self.yt.filter(progressive=False, type="audio", abr="50kbps").last()
    def a_70(self):
        return self.yt.filter(progressive=False, type="audio", abr="70kbps").last()


