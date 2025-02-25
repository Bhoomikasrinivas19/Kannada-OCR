from main import prediction_call
import os

def results(augdir):

    output = prediction_call(augdir)

    print(output)

results('images/Processed/Segmented/Augmented_Segmented/')

