# -*- coding: utf-8 -*-
"""
Created on Tue May 29 21:36:39 2018

@author: rodel
"""
import os
path = 'C:/Users/rodel/Documents/Machine_Learning/'
os.chdir(path)

# Utility imports
import numpy as np

# Data Managing imports
import pandas as pd

# Machine Learning imports
import tensorflow as tf
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn_pandas import DataFrameMapper
from sklearn.preprocessing import StandardScaler, OneHotEncoder


def _weight_variable(shape, name):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial, name=name)

def _bias_variable(shape, name):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial, name=name)
    
def _activation(z_val, act_name ='ReLU'):
    if act_name == "ReLU":
        return tf.nn.relu(z_val, name='act_fun_'+act_name)
    elif act_name == "Tanh":
        return tf.nn.tanh(z_val, name='act_fun_'+act_name)
    else:
        return tf.nn.sigmoid(z_val, name='act_fun_'+act_name)
 
def _variable_summaries(var):
    """Attach a lot of summaries to a Tensor (for TensorBoard visualization)."""
    with tf.name_scope('summaries'):
        mean = tf.reduce_mean(var)
        tf.summary.scalar('mean', mean)
        with tf.name_scope('stddev'):
            stddev = tf.sqrt(tf.reduce_mean(tf.square(var - mean)))
        tf.summary.scalar('stddev', stddev)
        tf.summary.scalar('max', tf.reduce_max(var))
        tf.summary.scalar('min', tf.reduce_min(var))
        tf.summary.histogram('histogram', var)

class Custom_Nnet(object): 
    def __init__(self, layer_sizes, activations, learning_rate=1e-4, dropout=1, epochs=500):
        self.layer_sizes = layer_sizes
        self.activations = activations
        self.num_hidden = len(layer_sizes)
        self.learning_rate = learning_rate
        self.dropout = dropout
        self.epochs = epochs
    
    def _nn_layer(self, in_vals, out_size, layer_name, activation):
        with tf.name_scope('Layer_'+layer_name) as scope:
            in_size = in_vals.shape.as_list()[1]
            w_fc = _weight_variable([in_size, out_size], 'weight_input')   # weights
            _variable_summaries(w_fc)
            b_fc = _bias_variable([out_size], 'bias_input')  # biases
            if layer_name == 'Output':
                self.Y_hat = tf.matmul(in_vals, w_fc)+b_fc
                return self.Y_hat
            elif layer_name == 'Hidden_1':
                z = tf.matmul(in_vals, w_fc) + b_fc
                h_fc1 = _activation(z, act_name = activation) # activation
                tf.summary.histogram('activations_input', h_fc1)
                return h_fc1
            else:
                z = tf.matmul(in_vals, w_fc) + b_fc
                h_fc1 = _activation(z, act_name = activation) # activation
                h_fc1_drop = tf.nn.dropout(h_fc1, self.keep_prob, name='Dropout_'+ layer_name)
                return h_fc1_drop

    def _build_network(self,x_width):
        ### Placeholders ###
        with tf.name_scope('placeholder') as scope:
            self.y = tf.placeholder(tf.float32, [None, 1], name='y')
            self.X = tf.placeholder(tf.float32, [None, x_width], name='X') # Placeholder values
            self.keep_prob = tf.placeholder("float", name='keep_prob') # Placeholder values

        output = self.X
        output_size = 1
        for i, size in enumerate(self.layer_sizes + [output_size]):
            if i == self.num_hidden:
                layer_name = 'Output'
            else:
                layer_name = 'Hidden_'+str(i+1) 
                activation = self.activations[i]
            output = self._nn_layer(output , size, layer_name, activation)
            
    def _loss(self):
        with tf.name_scope("cost_function") as scope:
            loss = tf.reduce_sum(tf.square(self.y-self.Y_hat, name='loss'))
            tf.summary.scalar('cost_function_summary', loss)
            return loss
    
    def _optimizer(self):
        with tf.name_scope("train") as scope:
            self.optimizer = tf.train.GradientDescentOptimizer(learning_rate=self.learning_rate).minimize(self._loss())
    
    def build_graph(self,x_with):
        with tf.Graph().as_default() as g:  
            self._build_network(x_width)
            self._optimizer()
            ### Write Summary Out ###
            self.merged = tf.summary.merge_all()
            self.g = g
            self.saver = tf.train.Saver()

#   TODO: Get display working
    def train(self,X,y):
        with tf.Session(graph=self.g) as sess:            
            sess.run(tf.global_variables_initializer())
            summary_writer = tf.summary.FileWriter('./graphs/n_net', graph=sess.graph)
            for epoch in range(self.epochs): # Train for 3000 epochs
                sess.run(self.optimizer, feed_dict={self.X: X, self.y: y,
                                                    self.keep_prob: self.dropout}) # run GD
                if epoch % 10 == 0:
                    print("Epoch:", '%04d' % (epoch+1))
                # Write logs for each iteration
                summary_str = sess.run(self.merged, feed_dict={self.X: X, self.y:y, self.keep_prob: 1})
                summary_writer.add_summary(summary_str, epoch)
                # Run the code below in the console
                #tensorboard --logdir=C:/Users/rodel/Documents/Machine_Learning/graphs/n_net --host=127.0.0.1
                #tensorboard --inspect --logdir C:/Users/rodel/Documents/Machine_Learning/graphs/n_net
            print("Optimization Finished!")
            self.saver.save(sess, "/tmp/model.ckpt")

    
    def predict(self,X):
        y_fake = np.ones((X.shape[0],1))
        with tf.Session(graph=self.g) as sess:
            self.saver.restore(sess, "/tmp/model.ckpt")            
            # Evaluate the predicted values
            yP = sess.run(self.Y_hat, feed_dict={self.X: X, self.y: y_fake, self.keep_prob:1})
            return yP
    
##############################################################
########               Model Start                 ###########
##############################################################
# Read the raw data file into arrays
dataPath ='C:/Users/rodel/Dropbox/Pmena EAcuna Rdelafu/Latex/Base.csv'
save_dir = 'C:/Users/rodel/Documents/Machine_Learning/imagenes/'

data = pd.read_csv(dataPath)
data=data[['Season','M3','TH','Este','Norte','TS']]
###############################################
####  Neural Network with Tensor Flow    ######
###############################################
# 1) Create a mapper to take care of all transformations
numeric = ['M3','TH','Este','Norte']
categories = ['Season']
data_cat_encoded, data_categories = data["Season"].factorize()
data.Season = data_cat_encoded
# Define a dummy encoder

class DummyEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, n_values='auto'):
        self.n_values = n_values
        self.ohe = OneHotEncoder(sparse=False, n_values=self.n_values)
    def transform(self, X, train=True):
            return self.ohe.transform(X)[:,:-1]
    def fit(self, X, y=None, **fit_params):
        return self.ohe.fit(X)
  
mapper = DataFrameMapper([(numeric, StandardScaler()),
                          (categories, DummyEncoder())])
# 2) Define the parameters to pass into the neural network
# 3) build the dataset
mapper.fit(data.copy())
data_ = np.round(mapper.transform(data.copy()), 2)
rows, cols = data_.shape
hidden = [10,10]
act = ['ReLU' for _ in range(len(hidden))]
nn=Custom_Nnet(hidden,act)
x_width = data_.shape[1]
nn.build_graph(x_width)
y = data.TS.values.reshape([len(data.TS),1])
nn.train(data_,y)
Y_hat=nn.predict(data_)

np.hstack([y,Y_hat])