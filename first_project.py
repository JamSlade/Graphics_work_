
from tkinter import *
import tkinter

class my_graphic():
    def __init__(self):
        self.init_window_name = tkinter.Tk()
        self.bottom_list = []
        self.operator_list = [self.PEN ,self.ERASER, 
                            self.LINE, self.ELLIPSE,
                            self.CIRCLE, self.SQUARE,
                            self.RECTANGLE, self.TRIANGLE,
                            self.CLEAR,self.CHANGE_PEN_COLOR,
                            self.CHANGE_PEN_WIDTH]
        self.condition = ""
        self.point = []
        self.PEN_COLOR = "red"
        self.BG_COLOR = "white"
        self.PEN_WIDTH = 2
        
    def set_init_window(self):
        #the init of canvas
        self.init_window_name.geometry('{0}x{1}'.
                                        format(
                                        #self.init_window_name.winfo_screenwidth() - 
                                        1200,
                                        #self.init_window_name.winfo_screenheight() - 
                                        700))
        
        self.cv = Canvas(self.init_window_name,
                    width = #self.init_window_name.winfo_screenwidth() - 
                    800,
                    height = #self.init_window_name.winfo_screenheight() - 
                    600,
                    bg = self.BG_COLOR,)
    
        self.cv.pack(side='top')
        # the init of curve or bottom
        operate_list = ['pen',"eraser",'line','ellipse','circle','square',
                        'rectangle','triangle','clear','change color','change width']

        for i in range(len(operate_list)):
            self.bottom_list.append((tkinter.Button
                                    (# pady = 10 ,
                                     width = 10,height = 2,
                                     text = operate_list[i],
                                     command = self.operator_list[i])        
                                    ))
        for i in self.bottom_list:
            i.pack(side = 'left',padx = 7, pady = 10)
        
    
    def motion_paint(self, event):
        if(self.condition == "PEN"):
            x1, y1 = ( event.x ), ( event.y )
            x2, y2 = ( event.x + 1 ), ( event.y + 1 )
            self.cv.create_line( x1, y1, x2, y2,fill=self.PEN_COLOR, width = self.PEN_WIDTH)
        elif(self.condition == "ERASER"):
            x1, y1 = ( event.x ), ( event.y )
            x2, y2 = ( event.x + 1 ), ( event.y + 1 )
            self.cv.create_line( x1, y1, x2, y2,fill=self.BG_COLOR, width = self.PEN_WIDTH)
                
    def line_paint(self):
        if(len(self.point) == 4):
            x1 = self.point[0]
            y1 = self.point[1]
            x2 = self.point[2]
            y2 = self.point[3]

            dx = abs(x1 - x2)
            dy = abs(y1 - y2)
            signx = 1 if(x2 - x1 > 0) else -1
            signy = 1 if(y2 - y1 > 0) else -1
            if(dx == 0):
                for i in range(dy):
                    self.cv.create_line(
                        x1, y1 + i * signy,
                        x1 , y1 + (i+1) * signy,
                        fill = self.PEN_COLOR,
                        width = self.PEN_WIDTH
                    )
            elif(dy == 0):
                for i in range(dx):
                    self.cv.create_line(
                        x1 + i * signx, y1,
                        x1 + (i - 1) * signx, y1 ,
                        fill = self.PEN_COLOR,
                        width = self.PEN_WIDTH
                    )
            elif(dx >= dy):
                k = dy / dx
                for i in range(dx):
                    self.cv.create_line(
                        x1 + i * signx, round(y1 + k * i * signy),
                        x1 + (i + 1) * signx, round(y1 + k * i * signy) + 1,
                        fill = self.PEN_COLOR,
                        width = self.PEN_WIDTH
                    )
            else:
                k = dx / dy
                for i in range(dy):
                    self.cv.create_line(
                        round(x1 + i * k * signx), y1 + i * signy,
                        round(x1 + i * k * signx)+1, y1 + (i+1) * signy,
                        fill = self.PEN_COLOR,
                        width = self.PEN_WIDTH
                    )
            while(len(self.point)):
                self.point.pop()
        else:
            self.point.clear()

    def cir_paint(self):
        x1 = self.point[0]
        y1 = self.point[1]
        x2 = self.point[2]
        y2 = self.point[3]
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2

        dx = abs(x1 - x2)
        a = dx / 2
        dy = abs(y1 - y2)
        b = dy / 2
        
        #print(self.point)
        if(a != 0 and b != 0):
            for i in range(int(a)):
                c = a*a*b*b - b*b*i*i
                self.cv.create_line(cx + i * -1,     cy + int(pow(c,0.5) / a + 0.5),
                                        cx + i * -1 + 1, cy + int(pow(c,0.5) / a + 0.5),
                                        fill = self.PEN_COLOR, width = self.PEN_WIDTH
                                        )
                self.cv.create_line(cx + i * -1,     cy + -1 * int(pow(c,0.5) / a + 0.5),
                                        cx + i * -1 + 1, cy + -1 * int(pow(c,0.5) / a + 0.5),
                                        fill = self.PEN_COLOR, width = self.PEN_WIDTH
                                        )
                
                self.cv.create_line(cx + i  ,     cy + int(pow(c,0.5) / a + 0.5),
                                        cx + i + 1, cy + int(pow(c,0.5) / a + 0.5),
                                        fill = self.PEN_COLOR, width = self.PEN_WIDTH
                                        )
                self.cv.create_line(cx + i ,     cy + -1 * int(pow(c,0.5) / a + 0.5),
                                        cx + i + 1, cy + -1 * int(pow(c,0.5) / a + 0.5),
                                        fill = self.PEN_COLOR, width = self.PEN_WIDTH
                                        )
                                        
            for i in range(int(b)):
                c = a*a*b*b - a*a*i*i
                self.cv.create_line(cx + int( pow (c, 0.5)/b  + 0.5), cy + i ,
                                        cx + int( pow (c, 0.5)/b + 0.5), cy + i + 1,
                                        fill = self.PEN_COLOR, width = self.PEN_WIDTH
                                        )
                self.cv.create_line(cx + -1 * int( pow (c, 0.5)/b + 0.5), cy + i ,
                                        cx + -1 * int( pow (c, 0.5)/b + 0.5), cy + i + 1,
                                        fill = self.PEN_COLOR, width = self.PEN_WIDTH
                                        )
                self.cv.create_line(cx + int( pow (c, 0.5)/b  + 0.5), cy + i * -1,
                                        cx + int( pow (c, 0.5)/b + 0.5), cy + i * -1 + 1,
                                        fill = self.PEN_COLOR, width = self.PEN_WIDTH
                                        )
                self.cv.create_line(cx + -1 * int( pow (c, 0.5)/b + 0.5), cy + i * -1,
                                        cx + -1 * int( pow (c, 0.5)/b + 0.5), cy + i * -1 + 1,
                                        fill = self.PEN_COLOR, width = self.PEN_WIDTH
                                        )
        else:
            self.line_paint()
        self.point.clear()
        #print(self.point)

    def click_paint(self,event):
        self.point.append(event.x)
        self.point.append(event.y)
        print(self.condition)
        #print(self.point)

        if(len(self.point) == 4):
            
            if(self.condition == "LINE"):
                self.line_paint()
            elif(self.condition == "CIRCLE"):
                x1 = self.point[0]
                y1 = self.point[1]
                x2 = self.point[2]
                y2 = self.point[3]
                dx = abs(x1 - x2)
                dy = abs(y1 - y2)
                if(dx < dy):
                    d = dy
                else:
                    d = dx
                signx = 1 if(x2 - x1 > 0) else -1
                signy = 1 if(y2 - y1 > 0) else -1
                self.point[2] = x1 + d * signx
                self.point[3] = y1 + d * signy
                self.cir_paint()
                
            elif(self.condition == "ELLIPSE"):
                self.cir_paint()

            elif(self.condition == "SQUARE"):
                L1 = []
                L2 = []
                L3 = []
                L4 = []
                x1 = self.point[0]
                y1 = self.point[1]
                x2 = self.point[2]
                y2 = self.point[3]
                dx = abs(x1 - x2)
                dy = abs(y1 - y2)
                signx = 1 if(x2 - x1 > 0) else -1
                signy = 1 if(y2 - y1 > 0) else -1
                d = 0
                if(dx < dy):
                    d = dy
                else:
                    d = dx
                self.point[2] = x1 + d * signx
                self.point[3] = y1 + d * signy
                for i in range(4):
                    L1.append(self.point[i])
                    L2.append(self.point[i])
                    L3.append(self.point[i])
                    L4.append(self.point[i])
                L1[0] = L1[2]
                L2[1] = L2[3]
                L3[2] = L3[0]
                L4[3] = L4[1]
                while(len(self.point)):
                    self.point.pop()
                for i in range(4):
                    self.point.append(L1[i])
                self.line_paint()
                for i in range(4):
                    self.point.append(L2[i])
                self.line_paint()
                for i in range(4):
                    self.point.append(L3[i])
                self.line_paint()
                for i in range(4):
                    self.point.append(L4[i])
                self.line_paint()


            elif(self.condition == "RECTANGLE"):
                L1 = []
                L2 = []
                L3 = []
                L4 = []
                for i in range(4):
                    L1.append(self.point[i])
                    L2.append(self.point[i])
                    L3.append(self.point[i])
                    L4.append(self.point[i])
                L1[0] = L1[2]
                L2[1] = L2[3]
                L3[2] = L3[0]
                L4[3] = L4[1]
                while(len(self.point)):
                    self.point.pop()
                for i in range(4):
                    self.point.append(L1[i])
                self.line_paint()
                for i in range(4):
                    self.point.append(L2[i])
                self.line_paint()
                for i in range(4):
                    self.point.append(L3[i])
                self.line_paint()
                for i in range(4):
                    self.point.append(L4[i])
                self.line_paint()

            elif(self.condition == "TRIANGLE"):
                L1 = []
                L2 = []
                for i in self.point:
                    L1.append(i)
                L2.append(L1[2])
                L2.append(L1[3])                
                L1[2] = L1[2] - 2*(self.point[2]  - self.point[0])
                L1[3] = L1[3]
                L2.append(L1[2])
                L2.append(L1[3])

                self.line_paint() 
                for i in L1:
                    self.point.append(i)
                self.line_paint()
                for i in L2:
                    self.point.append(i)
                self.line_paint()
                


    def PEN(self):
        self.condition = "PEN"
        if(self.condition == "PEN"):
            self.cv.bind("<B1-Motion>", self.motion_paint)
    def ERASER(self):
        self.condition = "ERASER"
        if(self.condition == "ERASER"):
            self.cv.bind("<B1-Motion>", self.motion_paint)

    def LINE(self):
        self.condition = "LINE"
        self.point.clear()
        if(self.condition == "LINE"):
            self.cv.bind("<Button-1>", self.click_paint)


    def CIRCLE(self):
        self.condition = "CIRCLE"
        self.point.clear()
        if(self.condition == "CIRCLE"):
            self.cv.bind("<Button-1>", self.click_paint)

    def ELLIPSE(self):
        self.condition = "ELLIPSE"
        self.point.clear()
        if(self.condition == "ELLIPSE"):
            self.cv.bind("<Button-1>", self.click_paint)
            

    def SQUARE(self):
        self.condition = "SQUARE"
        self.point.clear()
        if(self.condition == "SQUARE"):
            self.cv.bind("<Button-1>", self.click_paint)

    def RECTANGLE(self):
        self.condition = "RECTANGLE"
        self.point.clear()
        if(self.condition == "RECTANGLE"):
            self.cv.bind("<Button-1>", self.click_paint)

    def TRIANGLE(self):
        self.condition = "TRIANGLE"
        self.point.clear()
        if(self.condition == "TRIANGLE"):
            self.cv.bind("<Button-1>", self.click_paint)

    def CLEAR(self):
        self.cv.delete('all')

    def CHANGE_PEN_COLOR(self):
        #改�?�色的弹�?
        self.popup = tkinter.Entry(self.init_window_name)
        self.popup.pack()
        self.popup.insert(0," please input the color")
        tkinter.Button(self.init_window_name, text = "change",command = self.CHANGE_pen_c).pack()
        
        #变化

    def CHANGE_pen_c(self):
        self.PEN_COLOR = self.popup.get()
        self.popup.delete(0,"end")
        self.popup.insert(0," please input the color")
        
    def CHANGE_PEN_WIDTH(self):
        self.popup = tkinter.Entry(self.init_window_name)
        self.popup.pack()
        self.popup.insert(0," please input the width(int)")
        tkinter.Button(self.init_window_name, text = "change",command = self.CHANGE_pen_w).pack()

    def CHANGE_pen_w(self):
        self.PEN_WIDTH = self.popup.get()
        self.popup.delete(0,"end")
        self.popup.insert(0," please input the width(int)")

def start():
    JAM = my_graphic()
    JAM.set_init_window()
    JAM.init_window_name.mainloop()

start()
