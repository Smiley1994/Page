from bs4 import BeautifulSoup
import requests, sys

class downloadBood(object):
    def __init__(self):
        self.bookname = "凡人修仙传.txt"
        self.sever = "http://www.biqukan.com/"
        self.target = "https://www.biqukan.com/1_1680/"
        self.names = []
        self.urls = []
        self.nums = 0

    def get_download_url(self):
        req = requests.get(url=self.target)
        html = req.text
        div_bf = BeautifulSoup(html, features="html.parser")
        div = div_bf.find_all("div", class_="listmain")
        a_bf= BeautifulSoup(str(div[0]), features="html.parser")
        a = a_bf.find_all("a")
        self.nums = len(a[12:])
        for each in a[12:]:
            self.names.append(each.string)
            self.urls.append(self.sever + each.get("href"))

    def get_contents(self, target):
        req = requests.get(url=target)
        html = req.text
        bf = BeautifulSoup(html, features="html.parser")
        texts = bf.find_all("div",class_="showtxt")
        if len(texts):
            texts = texts[0].text.replace("\xa0"*8, "\n\n")
        return texts

    def writer(self, name, path, text):
        write_flag = True
        with open(path, "a", encoding="utf-8") as f:
            f.write(name + "\n")
            f.writelines(text)
            f.write("\n\n")



class downloadImages(object):

    def __init__(self):
        


if __name__ == "__main__":

    # dl = downloadBood()
    # dl.get_download_url()
    # print("star download", dl.bookname)
    # for i in range(dl.nums):
    #     print("\n\n", dl.bookname + ": ", dl.names[i], dl.urls[i], "\n star download....")
    #     dl.writer(dl.names[i], dl.bookname, dl.get_contents(dl.urls[i]))
    #     print("\n", dl.bookname + " -- ", dl.names[i], "\n end download!!!!")
    #     # sys.stdout.write(" 已下载：%.3f%%" % float(i/dl.nums) + "\r")
    #     # sys.stdout.flush()
    # print("\n\n", dl.bookname,"download end")

