import os
import glob
import sys
import re

import io_handler as io

def main():
  arguments = sys.argv

  notes_dir = '/Users/motephyr/Dropbox/Boostnote/notes'
  setting_file = '/Users/motephyr/Dropbox/Boostnote/boostnote.json'
  output_dir = '/Users/motephyr/Dropbox/Joplin'

  current_dir = os.getcwd()

  files = glob.glob('%s/*.cson' % notes_dir)
  setting_data = io.open_file(setting_file)

  for i, file in enumerate(files):
    file_data = io.open_file(file)

    io.write_to_file(output_dir, file, file_data, setting_data)
  
  print('All found files were processed.')

if __name__ == '__main__':
  main()
