import os
from nsml.constants import DATASET_PATH

def feed_infer(output_file, infer_func):

    filepath = os.path.join(DATASET_PATH, 'test', 'test_data', 'test_list.csv')

    with open(output_file, 'w') as of:

        with open(filepath, 'r') as f:

            for no, line in enumerate(f):

                # line : "abc.wav"

                wav_path = line.strip()
                wav_path = os.path.join(DATASET_PATH, 'test', 'test_data', wav_path)
                pred = infer_func(wav_path)

                of.write('%s,%s\n' % (wav_path, pred))
                print(wav_path, pred)

