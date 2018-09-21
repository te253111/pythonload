import urllib.request as ur
import re
s = ur.urlopen("https://mobilegamerhub.com/arena-of-valor/heroes/")
sl = str(s.read())
start = sl.find("<main")
end = sl.find("</main>")
content = sl[start:end]
arr = re.split('data-src="',content)
i=0
while i<len(arr) :
    if i>0 :
        url = arr[i][0:arr[i].find("></div")-1]
        name = arr[i][arr[i].find('class="text-center">')+20:arr[i].find('/h2></article>')-1]
        name = name.replace("&#8217;","'")
        ur.urlretrieve(url, name+".jpg")
        print(name+' '+url)
    i+=1