import argparse

FLAGS_BATCH_SIZE = 'batch_size'

ap = argparse.ArgumentParser()
ap.add_argument(FLAGS_BATCH_SIZE, help="batch size")
args = vars(ap.parse_args())

print('batch size is {}'.format(args[FLAGS_BATCH_SIZE]))
