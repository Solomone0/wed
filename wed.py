from pywebio import start_server
from pywebio.input import *# استرجاع القيم
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *
def App():
    name=input("Enter your name",type="text")
    if name==name:
        #password=input("Enter your password" ,type="text")
        a=open("dat","w")
        a.write(name)
start_server(App,port=885 ,debug=True)
App()
