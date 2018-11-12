import keras
from keras import models,layers
import numpy
from skimage.transform import resize
from skimage import util
class Cnn:
    def __init__(self, model):
        self.model = models.load_model("model.dat")
    def getPredict(self,img):
        img = numpy.asarray(img)
        img = img.astype('float32')/255.
        img = resize(img, (28, 28, 1))
        img = img.reshape((1, 28, 28, 1))
        return self.model.predict(img).argmax()