import tkinter,os

#Hello there
#THIS WILL STORE OUT FRACTAL NAMES - TO BE CHANGED ACCORDING TO NAME OF FILES
dict_Of_Fractals={ 1 : 'Bransley_Fern',
                   2 : 'SIERPINSKI',
                   3 : 'TREE1',
                   4 : 'TREE2',
                   }



class GUI:
    '''MAIN FILE OF OUR CODE'''
    def __init__(self,master):
        master.geometry('400x650+400+10')  # Setting window geometry for page
        master.resizable(0, 0)              #NON RESIZABLE WINDOW
        master.title('Choose Fractal:')

        self.master = master
        self.fractal =None
        self.paddingx = 110
        self.paddingy = 15


        self.Frac1Button = tkinter.Button(master,width=20,height=2,text = "BRANSLEY'S FERN",command = self.Frac1)
        self.Frac1Button.grid(padx=self.paddingx,pady=self.paddingy,row=0,column =10)

        self.Frac2Button = tkinter.Button(master,width=20,height=2,text = 'SIERPINSKI TRIANGLE',command = self.Frac2)
        self.Frac2Button.grid(padx=self.paddingx,pady=self.paddingy,row=1,column =10)

        self.Frac3Button = tkinter.Button(master,width=20,height=2,text = 'TREE1',command = self.Frac3)
        self.Frac3Button.grid(padx=self.paddingx,pady=self.paddingy,row=2,column =10)

        self.Frac4Button = tkinter.Button(master,width=20,height=2,text = 'TREE2',command = self.Frac4)
        self.Frac4Button.grid(padx=self.paddingx,pady=self.paddingy,row=3,column =10)


    def Frac1(self):
        self.playFile(1)
        self.master.quit()

    def Frac2(self):
        self.playFile(2)
        self.master.quit()

    def Frac3(self):
        self.playFile(3)
        self.master.quit()

    def Frac4(self):
        self.playFile(4)
        self.master.quit()

    def playFile(self,fractalNumber):
        '''PLAY THE FRACTAL ANIMATION'''
        self.master.destroy()
        commandToRunFile = 'python '+dict_Of_Fractals[fractalNumber] + '.py'
        os.system(commandToRunFile) #This will run the fractal file.Uncomment this when ur file is ready
        print(commandToRunFile)  # JUST FOR CHECKING



root = tkinter.Tk()
b =GUI(root)
root.mainloop()



#Uncomment this to prank urself!!!!
#os.system('python Mainpage.py')