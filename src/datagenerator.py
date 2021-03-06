import numpy as np

from tensorflow import keras
from tensorflow.keras.utils import Sequence


class DataGenerator(Sequence):
    """Generates data for Keras"""

    def __init__(self, list_IDs, labels, batch_size, dim, n_channels,
                 n_classes, gen_dir, shuffle=True, dict_label=None):
        """Initialization"""
        self.dim = dim
        self.batch_size = batch_size
        self.labels = labels
        self.list_IDs = list_IDs
        self.n_channels = n_channels
        self.n_classes = n_classes
        self.shuffle = shuffle
        self.on_epoch_end()
        self.gen_dir = gen_dir
        self.dict_label = dict_label


    def __len__(self):
        'Denotes the number of batches per epoch'
        return int(np.floor(len(self.list_IDs) / self.batch_size))

    def __getitem__(self, index):
        'Generate one batch of data'
        # Generate indexes of the batch
        indexes = self.indexes[index * self.batch_size:(index + 1) * self.batch_size]

        # Find list of IDs
        list_IDs_temp = [self.list_IDs[k] for k in indexes]

        # Generate data
        X, y = self.__data_generation(list_IDs_temp)

        return X, y

    def on_epoch_end(self):
        'Updates indexes after each epoch'
        self.indexes = np.arange(len(self.list_IDs))
        if self.shuffle:
            np.random.shuffle(self.indexes)

    def __data_generation(self, list_IDs_temp):

        'Generates data containing batch_size samples'  # X : (n_samples, *dim, n_channels)
        # Initialization
        X = np.empty((self.batch_size, *self.dim, self.n_channels))
        y = np.empty((self.batch_size), dtype=int)

        # Generate data
        for i, ID in enumerate(list_IDs_temp):

            # Store sample
            this_feat = np.load(self.gen_dir + str(ID) + '.npy')

            X[i,] = this_feat.reshape((*self.dim,
                                       self.n_channels))
            # Store class
            y[i] = self.dict_label[ID.split("/")[0]]

        self.labels = y# store true labels
        return X, keras.utils.to_categorical(y, num_classes=self.n_classes)
