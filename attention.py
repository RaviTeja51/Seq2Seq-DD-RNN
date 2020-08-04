import tensorflow as tf
from tensorflow.keras import layers

## implementation reference https://blog.floydhub.com/attention-mechanism/
## https://github.com/uzaymacar/attention-mechanisms/blob/master/layers.py
class LuongAttention(layers.Layer):
    def __init__(self, hidden_size, method="dot"):
        super(LuongAttention, self).__init__()
        self.method = method
        self.hidden_size = hidden_size

        if method == "general":
            self.fc = layers.Dense(hidden_size,use_bias=False)

        elif method == "concat":
            self.fc = layers.Dense(hidden_size, use_bias=False)
            self.v_a = Dense(units=1, use_bias=False)

    def __call__(self, decoder_hidden, encoder_output):
        # encoder_output shape (BATCH_SIZE, TIME STEP, UNITS)
        # decoder_hidden shape (BATCH_SIZE, UNITS)

        # add time axis to decoder_hidden h_t
        decoder_hidden = tf.expand_dims(decoder_hidden,axis=1)

        if self.method == "dot":
            score = layers.Dot([2,2])([encoder_output, decoder_hidden]) #SHAPE (BATCH_SIZE, TIME STEP, 1)

        elif self.method == "general":
            weighted_encoder_output =  self.fc(encoder_output)
            score =  layers.Dot([2,2])([weighted_encoder_output, decoder_hidden])  #SHAPE (BATCH_SIZE, TIME STEP, 1)

        elif self.method == "concat":
            weighted_sum = weighted_encoder_output  + weighted_decoder_hidden  #SHAPE(BATCH_SIZE, TIME STEP, UNITS)
            weighted_sum = self.fc(weighted_sum) #SHAPE(BATCH_SIZE, TIME STEP, UNITS)
            weighted_sum =  layers.Activation("tanh")(weighted_sum) #SHAPE (BATCH_SIZE, TIME STEP, UNITS)
            score = self.v_a(weighted_sum)   #SHAPE (BATCH_SIZE, TIME STEP, 1)

        attention_weights = tf.nn.softmax(score, axis = 2) #SHAPE (BATCH_SIZE, TIME STEP, 1)

        context_vector = tf.matmul(attention_weights, encoder_output) #SHAPE (BATCH_SIZE, TIME STEP, UNITS)
        return attention_weights, context_vector
