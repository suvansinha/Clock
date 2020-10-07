import tkinter as Tkinter 
from datetime import datetime 
counter = 66600
running = False
def counter_label(label): 
     def count(): 
          if running: 
               global counter 

               
               if counter==66600:			 
                       display="Starting..."
               else: 
                       tt = datetime.fromtimestamp(counter) 
                       string = tt.strftime("%H:%M:%S") 
                       display=string 

               label['text']=display  

    
               label.after(1000, count) 
               counter += 1

      
     count()	 
     
 
def Start(label): 
	global running 
	running=True
	counter_label(label) 
	start['state']='disabled'
	stop['state']='normal'
	reset['state']='normal'
	

def Stop(): 
	global running 
	start['state']='normal'
	stop['state']='disabled'
	reset['state']='normal'
	running = False
	

def Reset(label): 
	global counter 
	counter=66600
	

	if running==False:
		reset['state']='disabled'
		label['text']='Welcome!'
	
	
	else:				 
		label['text']='Starting...'
	
root = Tkinter.Tk() 
root.title("Stopwatch") 
	
 
root.minsize(width=650, height=200) 
label = Tkinter.Label(root, text="Welcome!",bg="black", fg="cyan", font="Ds-Digital 60") 
label.pack() 
f = Tkinter.Frame(root) 
start = Tkinter.Button(f, text='Start', width=13, height=2,
                       font="Ds-Digital 15 ", command=lambda:Start(label)) 
stop = Tkinter.Button(f, text='Stop',width=13, height=2,
                      font="Ds-Digital 15 ",state='disabled', command=Stop) 
reset = Tkinter.Button(f, text='Reset',width=13, height=2,
                       font="Ds-Digital 15 ", state='disabled',
                       command=lambda:Reset(label)) 
f.pack(anchor = 'center',pady=5) 
start.pack(side="left") 
stop.pack(side ="left") 
reset.pack(side="left") 
root.mainloop()