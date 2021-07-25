import pandas as pd
from absl import app
from absl import flags

FLAGS = flags.FLAGS

# Flag names are globally defined!  So in general, we need to be
# careful to pick names that are unlikely to be used by other libraries.
# If there is a conflict, we'll get an error at import time.
flags.DEFINE_string('in', None, 'kdbx of firefox password csv file location')
flags.DEFINE_string('out', None, 'output file location')
flags.DEFINE_boolean('debug', False, 'Produces debugging output.')

def main(argv):
  """
  This app should have be able to convert kdbx csv format to firefox csv format both ways
  """
  if FLAGS.debug:
    print('non-flag arguments:', argv)
  print('Happy Birthday', FLAGS.name)
  if FLAGS.age is not None:
    print('You are %d years old, and your job is %s' % (FLAGS.age, FLAGS.job))


if __name__ == '__main__':
  app.run(main)
