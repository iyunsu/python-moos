#!/usr/bin/python3
import sys
sys.path.append('/usr/local/lib/python3/dist-packages')
from pymoos import pymoos
import time
import lsm9ds1_compass_function as ls

class lsm9ds1MOOS(pymoos.comms):
    """pongMOOS is an example python MOOS app.
    It registers for 'PING' and responds with 'PONG' and the number of received
    'PING's

    Attributes:
        moos_community: a string representing the address of the Community
        moos_port:      an interger defining the port
    """
    def __init__(self, moos_community, moos_port):
        """Initiates MOOSComms, sets the callbacks and runs the loop"""
        super(pongMOOS, self).__init__()
        self.server = moos_community
        self.port = moos_port
        self.name = 'lsm9ds1MOOS'
        self.iter = 0

        self.set_on_connect_callback(self.__on_connect)
        self.set_on_mail_callback(self.__on_new_mail)
        self.run(self.server, self.port, self.name)

    def __on_connect(self):
        """OnConnect callback"""
        print("Connected to", self.server, self.port,
              "under the name ", self.name)
        return self.register('PING', 0)

    def __on_new_mail(self):
        """OnNewMail callback"""
        #for msg in self.fetch():
        #    if msg.key() == 'PING':
        #        self.iter += 1
        self.notify('MY_HEADING', float(heading), -1)
        return True



def main():
    #ponger = pongMOOS('localhost', 9001)

    #while True:
    #    time.sleep(1)
    
    while(1):
        heading = ls.get_heading()
        time.sleep(0.01)

if __name__ == "__main__":
    main()
