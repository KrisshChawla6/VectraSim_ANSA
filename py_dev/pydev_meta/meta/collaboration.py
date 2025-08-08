from __future__ import annotations
from typing import *

def ConnectToCollaborationServer(server_address: str, server_port: int) -> int:

	"""

	Sends a connection request to a META collaboration server. If META is already 
	connected to another server, then the user will be asked for closing current
	connection.

	Parameters
	----------
	server_address : str
		Address of the server; can be either IPv4 or IPv6.

	server_port : int
		Listening port of the server.

	Returns
	-------
	int
		Returns 1 if the request has been sent successfully, and 0 if not.

	See Also
	--------
	IsConnectedToCollaborationServer

	Examples
	--------
	::

		# PYTHON script
		from meta import guitk
		from meta import collaboration
		
		labelTest = None
		
		
		def main():
		    global labelTest
		    server_address = "192.9.122.55"
		    server_port = 12345
		    if collaboration.ConnectToCollaborationServer(server_address, server_port):
		        name = "New Connection"
		        a = guitk.constants.BCOnExitDestroy
		        winTest = guitk.BCWindowCreate(name, a)
		        text = "Trying to connect..."
		        labelTest = guitk.BCLabelCreate(winTest, text)
		        time_wait = 5000.0
		        checkConnect(time_wait)
		        guitk.BCShow(winTest)
		    else:
		        text = "Error: Could not send request!"
		        guitk.BCLabelSetText(labelTest, text)
		
		
		def checkConnect(time_wait):
		    global labelTest
		    if collaboration.IsConnectedToCollaborationServer():
		        text = "Connected!"
		        guitk.BCLabelSetText(labelTest, text)
		    else:
		        if time_wait < 0:
		            text = "Time-out: not able to connect!"
		            guitk.BCLabelSetText(labelTest, text)
		        else:
		            text = "Trying to connect... (" + str(time_wait / 1000.0) + " secs)"
		            guitk.BCLabelSetText(labelTest, text)
		            ms = 500
		            funct = checkConnect
		            data = time_wait - 500
		            guitk.BCTimerSingleShot(ms, funct, data)  # start check-timer:
		    return 0
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsConnectedToCollaborationServer() -> int:

	"""

	This function checks if META is connected to a Collaboration Server.

	Returns
	-------
	int
		Returns 1 if META is connected; otherwise it returns 0.

	See Also
	--------
	ConnectToCollaborationServer

	Examples
	--------
	::

		# PYTHON script
		from meta import collaboration
		
		
		def main():
		    if collaboration.IsConnectedToCollaborationServer():
		        print("Connected")
		    else:
		        print("Not Connected")
		
		
		if __name__ == "__main__":
		    main()


	"""

