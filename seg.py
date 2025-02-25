import os
import ntpath
import cv2

from preprocessing.segment_sentence import segment_sentence
from preprocessing.segment_word import segment_word
from preprocessing.segment_character import segment_character

dir = "Segmented"
location = "E:/Kannada/images/Processed/Segmented"


import shutil
shutil.rmtree('E:/Kannada/images/Processed/Segmented')

def segment(file):
    rootdir = 'images/Processed'
    directory = rootdir + '/Segmented'

    if not os.path.exists(directory):
        os.makedirs(directory)

    image = cv2.imread(file)

    sentences = segment_sentence(image, directory)

    for i in range(0, len(sentences)):
        words = segment_word(sentences[i], directory, i)

        for j in range(0, len(words)):
            characters, ottaksharas = segment_character(words[j], directory)

            for key in characters:

                imageName = str(i+1).zfill(2) + '-' + str(j+1).zfill(2) + \
                    '-' + str(key+1).zfill(2) + '-0' + '.png'

                cv2.imwrite(os.path.join(
                    directory, imageName), characters[key])

            for key in ottaksharas:

                imageName = str(i+1).zfill(2) + '-' + str(j+1).zfill(2) + \
                    '-' + str(key+1).zfill(2) + '-1' + '.png'

                # save image
                cv2.imwrite(os.path.join(directory, imageName),
                            ottaksharas[key])

segment('test1.jpg')