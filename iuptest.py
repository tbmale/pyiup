from iup import Iup
import thread

def apasa(this):
 thread.start_new_thread(bcbk,())
 return Iup.IUP_DEFAULT

def bcbk():
 if not mut.acquire(0):return
 Iup.Message("auci","auci")
 mut.release()

mut=thread.allocate_lock()
Iup.Open(Iup.NULL,Iup.NULL)
# Iup.ControlsOpen()
b=Iup.Button("apasa",Iup.NULL)
d=Iup.Dialog(Iup.Hbox(b,Iup.NULL))
Iup.SetAttributes(d,"SIZE=200x100")
cb=Iup.CB("int(Ihandle *)",apasa)
Iup.SetCallback(b,"ACTION",cb)

Iup.Show(d)
# Iup.FreeConsole() 

# shouldstop=False
# while not shouldstop:
 # Iup.LoopStep()
Iup.MainLoop()
# Iup.Close()
