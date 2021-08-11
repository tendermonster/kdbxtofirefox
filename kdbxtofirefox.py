from absl import app
from absl import flags
import os
import kdbxtofirefox.parse_helper as parser
import kdbxtofirefox.csv_types as types
import numpy as np
import pandas as pd
import csv

FLAGS = flags.FLAGS

# Flag names are globally defined!  So in general, we need to be
# careful to pick names that are unlikely to be used by other libraries.
# If there is a conflict, we'll get an error at import time.
flags.DEFINE_string('input', None, 'kdbx or firefox password csv file location')
flags.DEFINE_string('output', None, 'output file location')
flags.DEFINE_boolean('debug', False, 'Produces debugging output.')

def main(argv):
  """
  This app should have be able to convert kdbx csv format to firefox csv format both ways
  """
  type = None
  if FLAGS.debug:
    print('non-flag arguments:', argv)
  #read in the file and check for type
  if FLAGS.input is not None:
    print('input file name {}'.format(FLAGS.input))
    if os.path.exists(FLAGS.input):
      if os.path.isfile(FLAGS.input):
        print("file exists and is a file {}".format(FLAGS.input))
        type = parser.checkIfKdbx(FLAGS.input)
      else:
        raise Exception("not a file")
    else:
      raise Exception("file not found")
  else:
    print("no input file spacified")
    return 1
  if FLAGS.output is not None:
    #does not check true when path contains dir depth > 1 might need some trick
    if os.access(os.path.dirname(FLAGS.output), os.W_OK):
      print("file is writable")
      print('output file name {}'.format(FLAGS.output))
  else:
    print("no output file specified")
    return 1
  #convert databases
  if type is not None:
    if type is types.Types.FIREFOX:
      res = parser.convertToKdbx(FLAGS.input)
    if type is types.Types.KDBX:
      res = parser.convertToFirefox(FLAGS.input)
      #check if url is presend. if not than do not include the columns to the csv
    print(type)
  #write to output 
  pd.DataFrame(res).to_csv(FLAGS.output,header=False,index=False,quoting=csv.QUOTE_ALL)
if __name__ == '__main__':
  app.run(main)
