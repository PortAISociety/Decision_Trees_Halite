import threading
import time
import parse
from parse import *
import os
exitFlag = 0

class ThreadCreator(threading.Thread):
   def __init__(self, replay_buffer,folder_name,file_name):
      threading.Thread.__init__(self)
      self.replay_buffer = replay_buffer
      self.folder_name = folder_name
      self.file_name = file_name

   def run(self):
      print("Starting " + self.name)
      self.replay_buffer.append(parse_replay_file(os.path.join(self.folder_name, self.file_name)))
      print("Exiting " + self.name)
