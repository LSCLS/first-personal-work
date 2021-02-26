import urllib.request
import re
import urllib.error
headers=('user-agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0')
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
lastid = "6534646827828360320"
newtext=[]
for i in range(1,12711//10):
    url = "https://video.coral.qq.com/varticle/5963120294/comment/v2?callback=_varticle3889738104commentv2&orinum=10&oriorder=o&pageflag=1&cursor="+lastid+"&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=155840371506"+str(i)
    print(url)
    data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    patlast='"last":"(.*?)"'
    lastid=re.compile(patlast).findall(data)[0]
    patcontent='"content":"(.*?)"'
    content=re.compile(patcontent).findall(data)
    print('-----第%s页评论-----' % str(i))
    for j in range(1,len(content)):
        newtext.append(content[j])
        print('第%d条评论: ' %j + content[j])
with open("comment.txt", "w", encoding="utf-8") as f:
    for i in newtext:
        f.write(i)
