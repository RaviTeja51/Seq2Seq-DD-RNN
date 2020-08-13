import tensorflow as tf
from tensorflow.keras import layers, Model

## implementation reference https://blog.floydhub.com/attention-mechanism/
## https://machinetalk.org/2019/03/29/neural-machine-translation-with-attention-mechanism/

class LuongAttention(Model):

    def __init__(self, hidden_size, method="dot"):
        super(LuongAttention, self).__init__()
        self.method = method
        self.hidden_size = hidden_size

        self.wa = layers.Dense(hidden_size)

    def __call__(self, decoder_hidden, encoder_output):
        #decoder_hidden shape (batch_size,units)
        # encoder_outputs shape(batch_size, time_steps, units)

        decoder_hidden = tf.expand_dims(decoder_hidden,1) #decoder_hidden shape (batch_size, 1,units)

        score = tf.matmul(decoder_hidden, self.wa(encoder_output), transpose_b=True)
        # score will have shape: (batch_size, 1, max_len)

        # alignment vector a_t
        alignment = tf.nn.softmax(score, axis=2)

        # context vector c_t is the average sum of encoder output
        context = tf.matmul(alignment, encoder_output)
        #  vector's shape: (batch_size, 1, rnn_size)

        return context, alignment
