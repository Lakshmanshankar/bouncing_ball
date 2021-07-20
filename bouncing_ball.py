from tkinter import *
#from tkinter import all
import time

window=Tk()

window.configure(bg='black')
#bg=background color

canvas=Canvas(window,width=800,height=1700,bg='black')

canvas.pack()

class ball:
    
    def __init__(self,canvas,x,y,diameter,xvelocity,yvelocity,color):
        
        self.canvas=canvas
        
        self.img=canvas.create_oval(x,y,diameter,diameter,fill=color)
        
        self.xvelocity=xvelocity
        
        self.yvelocity=yvelocity
    def move(self):
        
        
        cordinates=self.canvas.coords(self.img)
        
        
        print(cordinates)
        
        
        
        if(cordinates[2]>=(self.canvas.winfo_width()) or cordinates[0]<0):
            self.xvelocity=-self.xvelocity
            
            
            
        if(cordinates[3]>=(self.canvas.winfo_height()) or cordinates[0]<0):
            self.yvelocity=-self.yvelocity
            
            
            
            
        self.canvas.move(self.img,self.xvelocity,self.yvelocity)
# class end objects;



s=ball(canvas,4,5,78,6,8,'red')

s1=ball(canvas,7,3,140,16,8,'lavender')

s2=ball(canvas,5,10,330,24,4,'orange')

s3=ball(canvas,15,5,200,22,16,'green')

s4=ball(canvas,34,5,150,36,8,'brown')

s5=ball(canvas,54,5,156,8,64,'blue')

s6=ball(canvas,6,5,156,18,64,'yellow')

s7=ball(canvas,5,5,76,8,4,'lightblue')

s8=ball(canvas,4,5,200,8,34,'lightgreen')
s9=ball(canvas,74,75,15,8,4,'yellow')

while True:
    s.move()
    
    s1.move()
    
    s2.move()
    
    s3.move()
    
    s4.move()
    
    s5.move()
    
    s6.move()
    
    s7.move()
    
    s8.move()
    
    s9.move()
    
    
    
    #_____end______
    window.update()
    time.sleep(0.01)
        
window.mainloop()

