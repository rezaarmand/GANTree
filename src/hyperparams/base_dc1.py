import tensorflow as tf
from . import base


class Hyperparams(base.Hyperparams):  # change
    dtype = tf.float32
    batch_size_train = 128
    batch_size_test = 64
    logit_batch_size = 32 # factor of batch_size

    input_size = 2

    input_height = 32
    input_width = 32
    input_channel = 1

    z_size = 32

    lr_autoencoder = 0.0001
    lr_decoder = 0.0001
    lr_disc = 0.0001
    beta1 = 0.6
    beta2 = 0.99

    z_dist_type = 'normal'  # ['uniform', 'normal', 'sphere']
    show_visual_while_training = False

    train_generator_adv = True

    model = 'dcgan'
    exp_name = 'dcgan_mnist_0'
    dataloader = 'mnist'
