# import keras building blocks - models, layers, optimizers
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras import optimizers, regularizers
from keras.optimizers import Adam

# to do deep learning on spark, we import elephas
from elephas.ml_model import ElephasEstimator
