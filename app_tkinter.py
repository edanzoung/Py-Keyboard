#=====================================================#
#=========== PY KEYBOARD APP  V1.0  by Edanzoung =====#
#============== edanzoung@outlook.fr =================#
#=====================================================#


#=====================================================#
#==================== LICENSE ========================#

#************** THIS PROJECT IS FREE *****************#
#******* It means that the users have the freedom ****#
#***** *** to run, copy, distribute, study, change ***#
#*********** and improve the software  ***************#
#=====================================================#


from tkinter import Tk, Canvas, Entry, Label, Button,Frame
from PIL import Image, ImageTk


class Tkinter_app():

    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x500")
        self.window.configure(bg = "#000")
        self.window.resizable(False, False)
        
        #==== Background Image - Left Section
        self.image_file = Image.open("assets/3.jpg")
        self.image_file = self.image_file.resize((800,1000), Image.ANTIALIAS)
        self.image=ImageTk.PhotoImage(self.image_file)      
        #=== Logo Image
        self.logo_file = Image.open("assets/logo.png")
        self.logo_file = self.logo_file.resize((300,300), Image.ANTIALIAS)
        self.logo=ImageTk.PhotoImage(self.logo_file)     
        #=== Start Button Image
        self.start_file = Image.open("assets/start.png")
        self.start_file = self.start_file.resize((150,50), Image.ANTIALIAS)
        self.start=ImageTk.PhotoImage(self.start_file)
        #=== Home Button Image
        self.home_file = Image.open("assets/home.png")
        self.home_file = self.home_file.resize((150,50), Image.ANTIALIAS)
        self.home=ImageTk.PhotoImage(self.home_file)

        self.App()

    def App(self):
        
        
        def rgb(rgb):
            """translate an rgb tuple of int to a tkinter friendly color code"""
            return "#%02x%02x%02x" % rgb

        #=====================================================#
        #================= kEYBOARD PAGE    ==================#
        #=====================================================#
        self.frame2=Frame(self.window,bg = rgb((100,100,100)), height = 500, width = 800)
        self.frame2.place(x=0,y=0)
        self.canvas2 = Canvas(self.frame2,bg = rgb((150,150,150)),
            height = 500,
            width = 800,
            bd = 0,
            highlightthickness = 0,cursor='hand2')
        self.canvas2.place(x = 0, y = 0)

        gap=50
        x1=50
        y1=20
        x2=x1+gap
        y2=250
        _gap=25
        _x1=88
        _y1=20
        _x2=_x1+_gap
        _y2=150
        white_key_color=rgb((255,255,255))
        white_key_motion_color=rgb((50,250,50))
        black_key_color=rgb((0,0,0))
        black_key_motion_color=rgb((255,100,50))

        
        self.canvas2.create_rectangle(0,400,800,500,fill="#fff",outline="#fff")
        

        #==== White Keys Creation
        self.white1=self.canvas2.create_rectangle(x1,y1,x2,y2,fill=white_key_color,outline="#000")
        self.white2=self.canvas2.create_rectangle(x1+gap,y1,x2+gap,y2,fill=white_key_color,outline="#000")
        self.white3=self.canvas2.create_rectangle(x1+gap*2,y1,x2+gap*2,y2,fill=white_key_color,outline="#000")
        self.white4=self.canvas2.create_rectangle(x1+gap*3,y1,x2+gap*3,y2,fill=white_key_color,outline="#000")
        self.white5=self.canvas2.create_rectangle(x1+gap*4,y1,x2+gap*4,y2,fill=white_key_color,outline="#000")
        self.white6=self.canvas2.create_rectangle(x1+gap*5,y1,x2+gap*5,y2,fill=white_key_color,outline="#000")
        self.white7=self.canvas2.create_rectangle(x1+gap*6,y1,x2+gap*6,y2,fill=white_key_color,outline="#000")
        self.white8=self.canvas2.create_rectangle(x1+gap*7,y1,x2+gap*7,y2,fill=white_key_color,outline="#000")
        self.white9=self.canvas2.create_rectangle(x1+gap*8,y1,x2+gap*8,y2,fill=white_key_color,outline="#000")
        self.white10=self.canvas2.create_rectangle(x1+gap*9,y1,x2+gap*9,y2,fill=white_key_color,outline="#000")
        self.white11=self.canvas2.create_rectangle(x1+gap*10,y1,x2+gap*10,y2,fill=white_key_color,outline="#000")
        self.white12=self.canvas2.create_rectangle(x1+gap*11,y1,x2+gap*11,y2,fill=white_key_color,outline="#000")
        self.white13=self.canvas2.create_rectangle(x1+gap*12,y1,x2+gap*12,y2,fill=white_key_color,outline="#000")
        self.white14=self.canvas2.create_rectangle(x1+gap*13,y1,x2+gap*13,y2,fill=white_key_color,outline="#000")

        #==== Black Keys Creation
        self.black1=self.canvas2.create_rectangle(_x1,_y1,_x2,_y2,fill=black_key_color,outline="#000")
        self.black2=self.canvas2.create_rectangle(_x1+_gap*2,_y1,_x2+_gap*2,_y2,fill=black_key_color,outline="#000")
        self.black3=self.canvas2.create_rectangle(_x1+_gap*6,_y1,_x2+_gap*6,_y2,fill=black_key_color,outline="#000")
        self.black4=self.canvas2.create_rectangle(_x1+_gap*8,_y1,_x2+_gap*8,_y2,fill=black_key_color,outline="#000")
        self.black5=self.canvas2.create_rectangle(_x1+_gap*10,_y1,_x2+_gap*10,_y2,fill=black_key_color,outline="#000")
        self.black6=self.canvas2.create_rectangle(_x1+_gap*14,_y1,_x2+_gap*14,_y2,fill=black_key_color,outline="#000")
        self.black7=self.canvas2.create_rectangle(_x1+_gap*16,_y1,_x2+_gap*16,_y2,fill=black_key_color,outline="#000")
        self.black8=self.canvas2.create_rectangle(_x1+_gap*20,_y1,_x2+_gap*20,_y2,fill=black_key_color,outline="#000")
        self.black9=self.canvas2.create_rectangle(_x1+_gap*22,_y1,_x2+_gap*22,_y2,fill=black_key_color,outline="#000")
        self.black10=self.canvas2.create_rectangle(_x1+_gap*24,_y1,_x2+_gap*24,_y2,fill=black_key_color,outline="#000")

        self.log=self.canvas2.create_text(430,320,text="",fill=black_key_color,font=("Time",50,"bold"))
        
        #=====================================================#
        #================= KEYBOARD PAGE   END ===============#
        #=====================================================#

        #=====================================================#
        #================= HOME PAGE    ======================#
        #=====================================================#
        self.frame1=Frame(self.window,bg = rgb((255,0,0)), height = 500, width = 800)
        self.frame1.place(x=0,y=0)
        self.canvas = Canvas(self.frame1,bg = "#fff",
            height = 500,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")

        self.canvas.place(x = 0, y = 0)

        #==== Background Image - Left Section
        self.canvas.create_image(0,0, image=self.image)

        #==== Logo Image
        self.canvas.create_image(600,180, image=self.logo)
        #==== App Nane
        self.canvas.create_text(220,250, text="PY KEYBOARD",font=("Arial",25,"bold"),fill=rgb((255,255,255)))

        #=====================================================#
        #================= HOME PAGE  END  ===================#
        #=====================================================#
        

        #=====================================================#
        #================= PAGINATION FUNCTIONS ==============#
        #=====================================================#

        def welcome():
            self.frame2.lift()
            self.frame1.lower()
        def decon():
            self.frame1.lift()
            self.frame2.lower()
            

        #==== Button Start in Home Page        
        self.con_button = Button(self.canvas,image=self.start,compound = 'center',relief="flat",
                            highlightthickness = 0,text="",
                            bg=rgb((255,255,255)),borderwidth = 0,cursor="hand2",command=welcome)
        self.con_button.place(x=550, y=380)
        
        #==== Button Home in Keyboard Page
        self.decon_button = Button(self.canvas2,image=self.home,compound = 'center',relief="flat",
                            highlightthickness = 0,text="",
                            bg=rgb((255,255,255)),borderwidth = 0,cursor="hand2",command=decon)
        self.decon_button.place(x=350, y=420)

        #=====================================================#
        #================= PAGINATION FUNCTIONS  END =========#
        #=====================================================#

        #=====================================================#
        #================= MOUSE EVENTS FUNCTIONS  ===========#
        #=====================================================#

        #==== When Mouse Enter and move over the key
        #####== WHITES
        def white1_motion(event):
            self.canvas2.itemconfig(self.white1,fill=white_key_motion_color)
            self.canvas2.itemconfig(self.log,fill=white_key_motion_color,text="Note de DO")
        def white2_motion(event):
            self.canvas2.itemconfig(self.white2,fill=white_key_motion_color)
            self.canvas2.itemconfig(self.log,fill=white_key_motion_color,text="Note de RE")
        def white3_motion(event):
            self.canvas2.itemconfig(self.white3,fill=white_key_motion_color)
            self.canvas2.itemconfig(self.log,fill=white_key_motion_color,text="Note de MI")
        def white4_motion(event):
            self.canvas2.itemconfig(self.white4,fill=white_key_motion_color)
            self.canvas2.itemconfig(self.log,fill=white_key_motion_color,text="Note de FA")
        def white5_motion(event):
            self.canvas2.itemconfig(self.white5,fill=white_key_motion_color)
            self.canvas2.itemconfig(self.log,fill=white_key_motion_color,text="Note de SOL")
        def white6_motion(event):
            self.canvas2.itemconfig(self.white6,fill=white_key_motion_color)
            self.canvas2.itemconfig(self.log,fill=white_key_motion_color,text="Note de LA")
        def white7_motion(event):
            self.canvas2.itemconfig(self.white7,fill=white_key_motion_color)
            self.canvas2.itemconfig(self.log,fill=white_key_motion_color,text="Note de SI")
        def white8_motion(event):
            self.canvas2.itemconfig(self.white8,fill=white_key_motion_color)
            self.canvas2.itemconfig(self.log,fill=white_key_motion_color,text="Note de DO")
        def white9_motion(event):
            self.canvas2.itemconfig(self.white9,fill=white_key_motion_color)
            self.canvas2.itemconfig(self.log,fill=white_key_motion_color,text="Note de RE")
        def white10_motion(event):
            self.canvas2.itemconfig(self.white10,fill=white_key_motion_color)
            self.canvas2.itemconfig(self.log,fill=white_key_motion_color,text="Note de MI")
        def white11_motion(event):
            self.canvas2.itemconfig(self.white11,fill=white_key_motion_color)
            self.canvas2.itemconfig(self.log,fill=white_key_motion_color,text="Note de FA")
        def white12_motion(event):
            self.canvas2.itemconfig(self.white12,fill=white_key_motion_color)
            self.canvas2.itemconfig(self.log,fill=white_key_motion_color,text="Note de SOL")
        def white13_motion(event):
            self.canvas2.itemconfig(self.white13,fill=white_key_motion_color)
            self.canvas2.itemconfig(self.log,fill=white_key_motion_color,text="Note de LA")
        def white14_motion(event):
            self.canvas2.itemconfig(self.white14,fill=white_key_motion_color)
            self.canvas2.itemconfig(self.log,fill=white_key_motion_color,text="Note de SI")
        #####== BLACKS
        def black1_motion(event):
            self.canvas2.itemconfig(self.black1,fill=black_key_motion_color)
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="Note de DO#/REb")
        def black2_motion(event):
            self.canvas2.itemconfig(self.black2,fill=black_key_motion_color)
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="Note de RE#/MIb")
        def black3_motion(event):
            self.canvas2.itemconfig(self.black3,fill=black_key_motion_color)
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="Note de FA#/SOLb")
        def black4_motion(event):
            self.canvas2.itemconfig(self.black4,fill=black_key_motion_color)
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="Note de SOL#/LAb")
        def black5_motion(event):
            self.canvas2.itemconfig(self.black5,fill=black_key_motion_color)
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="Note de LA#/SIb")
        def black6_motion(event):
            self.canvas2.itemconfig(self.black6,fill=black_key_motion_color)
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="Note de DO#/REb")
        def black7_motion(event):
            self.canvas2.itemconfig(self.black7,fill=black_key_motion_color)
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="Note de RE#/MIb")
        def black8_motion(event):
            self.canvas2.itemconfig(self.black8,fill=black_key_motion_color)
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="Note de FA#/SOLb")
        def black9_motion(event):
            self.canvas2.itemconfig(self.black9,fill=black_key_motion_color)
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="Note de SOL#/LAb")
        def black10_motion(event):
            self.canvas2.itemconfig(self.black10,fill=black_key_motion_color)
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="Note de LA#/SIb")
            
        #==== When Mouse Leave the key
        #####== WHITES
        def white1_leave(event):
            self.canvas2.itemconfig(self.white1,fill=rgb((255,255,255)))
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="")
        def white2_leave(event):
            self.canvas2.itemconfig(self.white2,fill=rgb((255,255,255)))
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="")
        def white3_leave(event):
            self.canvas2.itemconfig(self.white3,fill=rgb((255,255,255)))
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="")
        def white4_leave(event):
            self.canvas2.itemconfig(self.white4,fill=rgb((255,255,255)))
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="")
        def white5_leave(event):
            self.canvas2.itemconfig(self.white5,fill=rgb((255,255,255)))
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="")
        def white6_leave(event):
            self.canvas2.itemconfig(self.white6,fill=rgb((255,255,255)))
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="")
        def white7_leave(event):
            self.canvas2.itemconfig(self.white7,fill=rgb((255,255,255)))
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="")
        def white8_leave(event):
            self.canvas2.itemconfig(self.white8,fill=rgb((255,255,255)))
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="")
        def white9_leave(event):
            self.canvas2.itemconfig(self.white9,fill=rgb((255,255,255)))
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="")
        def white10_leave(event):
            self.canvas2.itemconfig(self.white10,fill=rgb((255,255,255)))
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="")
        def white11_leave(event):
            self.canvas2.itemconfig(self.white11,fill=rgb((255,255,255)))
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="")
        def white12_leave(event):
            self.canvas2.itemconfig(self.white12,fill=rgb((255,255,255)))
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="")
        def white13_leave(event):
            self.canvas2.itemconfig(self.white13,fill=rgb((255,255,255)))
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="")
        def white14_leave(event):
            self.canvas2.itemconfig(self.white14,fill=rgb((255,255,255)))
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="")

        #####== BLACKS
        def black1_leave(event):
            self.canvas2.itemconfig(self.black1,fill=rgb((0,0,0)))
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="")
        def black2_leave(event):
            self.canvas2.itemconfig(self.black2,fill=rgb((0,0,0)))
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="")
        def black3_leave(event):
            self.canvas2.itemconfig(self.black3,fill=rgb((0,0,0)))
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="")
        def black4_leave(event):
            self.canvas2.itemconfig(self.black4,fill=rgb((0,0,0)))
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="")
        def black5_leave(event):
            self.canvas2.itemconfig(self.black5,fill=rgb((0,0,0)))
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="")
        def black6_leave(event):
            self.canvas2.itemconfig(self.black6,fill=rgb((0,0,0)))
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="")
        def black7_leave(event):
            self.canvas2.itemconfig(self.black7,fill=rgb((0,0,0)))
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="")
        def black8_leave(event):
            self.canvas2.itemconfig(self.black8,fill=rgb((0,0,0)))
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="")
        def black9_leave(event):
            self.canvas2.itemconfig(self.black9,fill=rgb((0,0,0)))
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="")
        def black10_leave(event):
            self.canvas2.itemconfig(self.black10,fill=rgb((0,0,0)))
            self.canvas2.itemconfig(self.log,fill=black_key_motion_color,text="")

        #=====================================================#
        #================= MOUSE EVENTS FUNCTIONS  END =======#
        #=====================================================#


        #=====================================================#
        #============= KEYS BINDING  WHITES AND BLACKS =======#
        #=====================================================#

        #####== WHITES
        self.canvas2.tag_bind(self.white1,"<Motion>",white1_motion)
        self.canvas2.tag_bind(self.white1,"<Enter>",white1_motion)
        self.canvas2.tag_bind(self.white1,"<Leave>",white1_leave)
        self.canvas2.tag_bind(self.white2,"<Motion>",white2_motion)
        self.canvas2.tag_bind(self.white2,"<Enter>",white2_motion)
        self.canvas2.tag_bind(self.white2,"<Leave>",white2_leave)
        self.canvas2.tag_bind(self.white3,"<Motion>",white3_motion)
        self.canvas2.tag_bind(self.white3,"<Enter>",white3_motion)
        self.canvas2.tag_bind(self.white3,"<Leave>",white3_leave)
        self.canvas2.tag_bind(self.white4,"<Motion>",white4_motion)
        self.canvas2.tag_bind(self.white4,"<Enter>",white4_motion)
        self.canvas2.tag_bind(self.white4,"<Leave>",white4_leave)
        self.canvas2.tag_bind(self.white5,"<Motion>",white5_motion)
        self.canvas2.tag_bind(self.white5,"<Enter>",white5_motion)
        self.canvas2.tag_bind(self.white5,"<Leave>",white5_leave)
        self.canvas2.tag_bind(self.white6,"<Motion>",white6_motion)
        self.canvas2.tag_bind(self.white6,"<Enter>",white6_motion)
        self.canvas2.tag_bind(self.white6,"<Leave>",white6_leave)
        self.canvas2.tag_bind(self.white7,"<Motion>",white7_motion)
        self.canvas2.tag_bind(self.white7,"<Enter>",white7_motion)
        self.canvas2.tag_bind(self.white7,"<Leave>",white7_leave)
        self.canvas2.tag_bind(self.white8,"<Motion>",white8_motion)
        self.canvas2.tag_bind(self.white8,"<Enter>",white8_motion)
        self.canvas2.tag_bind(self.white8,"<Leave>",white8_leave)
        self.canvas2.tag_bind(self.white9,"<Motion>",white9_motion)
        self.canvas2.tag_bind(self.white9,"<Enter>",white9_motion)
        self.canvas2.tag_bind(self.white9,"<Leave>",white9_leave)
        self.canvas2.tag_bind(self.white10,"<Motion>",white10_motion)
        self.canvas2.tag_bind(self.white10,"<Enter>",white10_motion)
        self.canvas2.tag_bind(self.white10,"<Leave>",white10_leave)
        self.canvas2.tag_bind(self.white11,"<Motion>",white11_motion)
        self.canvas2.tag_bind(self.white11,"<Enter>",white11_motion)
        self.canvas2.tag_bind(self.white11,"<Leave>",white11_leave)
        self.canvas2.tag_bind(self.white12,"<Motion>",white12_motion)
        self.canvas2.tag_bind(self.white12,"<Enter>",white12_motion)
        self.canvas2.tag_bind(self.white12,"<Leave>",white12_leave)
        self.canvas2.tag_bind(self.white13,"<Motion>",white13_motion)
        self.canvas2.tag_bind(self.white13,"<Enter>",white13_motion)
        self.canvas2.tag_bind(self.white13,"<Leave>",white13_leave)
        self.canvas2.tag_bind(self.white14,"<Motion>",white14_motion)
        self.canvas2.tag_bind(self.white14,"<Enter>",white14_motion)
        self.canvas2.tag_bind(self.white14,"<Leave>",white14_leave)
        #####== BLACKS
        self.canvas2.tag_bind(self.black1,"<Motion>",black1_motion)
        self.canvas2.tag_bind(self.black1,"<Enter>",black1_motion)
        self.canvas2.tag_bind(self.black1,"<Leave>",black1_leave)
        self.canvas2.tag_bind(self.black2,"<Motion>",black2_motion)
        self.canvas2.tag_bind(self.black2,"<Enter>",black2_motion)
        self.canvas2.tag_bind(self.black2,"<Leave>",black2_leave)
        self.canvas2.tag_bind(self.black3,"<Motion>",black3_motion)
        self.canvas2.tag_bind(self.black3,"<Enter>",black3_motion)
        self.canvas2.tag_bind(self.black3,"<Leave>",black3_leave)
        self.canvas2.tag_bind(self.black4,"<Motion>",black4_motion)
        self.canvas2.tag_bind(self.black4,"<Enter>",black4_motion)
        self.canvas2.tag_bind(self.black4,"<Leave>",black4_leave)
        self.canvas2.tag_bind(self.black5,"<Motion>",black5_motion)
        self.canvas2.tag_bind(self.black5,"<Enter>",black5_motion)
        self.canvas2.tag_bind(self.black5,"<Leave>",black5_leave)
        self.canvas2.tag_bind(self.black6,"<Motion>",black6_motion)
        self.canvas2.tag_bind(self.black6,"<Enter>",black6_motion)
        self.canvas2.tag_bind(self.black6,"<Leave>",black6_leave)
        self.canvas2.tag_bind(self.black7,"<Motion>",black7_motion)
        self.canvas2.tag_bind(self.black7,"<Enter>",black7_motion)
        self.canvas2.tag_bind(self.black7,"<Leave>",black7_leave)
        self.canvas2.tag_bind(self.black8,"<Motion>",black8_motion)
        self.canvas2.tag_bind(self.black8,"<Enter>",black8_motion)
        self.canvas2.tag_bind(self.black8,"<Leave>",black8_leave)
        self.canvas2.tag_bind(self.black9,"<Motion>",black9_motion)
        self.canvas2.tag_bind(self.black9,"<Enter>",black9_motion)
        self.canvas2.tag_bind(self.black9,"<Leave>",black9_leave)
        self.canvas2.tag_bind(self.black10,"<Motion>",black10_motion)
        self.canvas2.tag_bind(self.black10,"<Enter>",black10_motion)
        self.canvas2.tag_bind(self.black10,"<Leave>",black10_leave)

        #=====================================================#
        #============= KEYS BINDING  WHITES AND BLACKS =======#
        #=====================================================#


if __name__=='__main__':
    app=Tkinter_app()
    app.window.mainloop()
