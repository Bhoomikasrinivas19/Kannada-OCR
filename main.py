import os
import ntpath
from preprocessing.segmentation import segment
from preprocessing.augment import augment

from CNN.recognize_character import recognize

from Unicode.seqgen import sequenceGen
from Unicode.printdoc import unicode_to_kn


def segmentation_call(image):
    rootdir = '/images/Processed_' + \
        os.path.splitext(ntpath.basename(image))[0]
    if not os.path.exists(rootdir):
        os.makedirs(rootdir)

    dir = rootdir + '/Segmented_' + os.path.splitext(ntpath.basename(image))[0]
    segment(image)
    return rootdir, dir


def augmentation_call(image, rootdir):
    augdir = rootdir + '/Augmented_' + \
        os.path.splitext(ntpath.basename(image))[0]
    augment(rootdir, augdir)
    return augdir


def prediction_call(augdir):
    predictions = recognize(os.path.join(os.getcwd(), augdir))
    sequence = sequenceGen(predictions)
    kannada_text = unicode_to_kn(sequence)
    return(kannada_text)
