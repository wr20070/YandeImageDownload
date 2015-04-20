import urllib.request
import time
import re
import os

url = 'https://yande.re/post?page='

def saveImg (imgUrl,saveDir):
	startTime = time.time()
	fileRe = re.compile(r'/yande.re (.*)')
	fileName = fileRe.findall(urllib.request.unquote(imgUrl))[0]
	outPutRe = re.compile(r'\d+')
	imgNum = outPutRe.findall(fileName)[0]
	print ('Image ID: [' + imgNum + '] Saving Please wait...')
	urllib.request.urlretrieve(imgUrl,  saveDir + '/' + fileName)
	print ('Image ID: [' + imgNum + '] has been saved,Processed in' , int(time.time() - startTime) , 'seconds.')


def getImgList(url):
	print ('Loading...Please wait..')
	page = urllib.request.urlopen(url).read()
	page = page.decode('UTF-8')
	img = re.compile ( r'<a class="directlink largeimg" href="(.+?)">')
	imgList = img.findall (page) 
	return imgList

saveDir=input('Please input saved dir:')

try:
	os.mkdir(saveDir)
except Exception:
	pass

startPage = int(input('Please input start page num:'))
endPage = int(input('Please input end page num:'))


for i in range(startPage, endPage + 1):
	print('########################### Processing page' , i ,'###########################')
	for imgurl in getImgList(url + str(i) ):
		try:
			saveImg(imgurl, saveDir)
			print()
		except Exception:
			pass
	
print ('###########################Download is complete###########################')
