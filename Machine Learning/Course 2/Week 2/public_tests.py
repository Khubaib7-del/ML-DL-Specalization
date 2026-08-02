import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.activations import linear, sigmoid, relu

def test_my_softmax(target):
    z = np.array([1., 2., 3., 4.])
    a = target(z)
    atf = tf.nn.softmax(z)
    
    assert np.allclose(a, atf, atol=1e-10), f"Wrong values. Expected {atf}, got {a}"
    
    z = np.array([np.log(0.1)] * 10)
    a = target(z)
    atf = tf.nn.softmax(z)
    
    assert np.allclose(a, atf, atol=1e-10), f"Wrong values. Expected {atf}, got {a}"
    
    print("\033[92m All tests passed.")
    
def test_model(target, classes, input_size):
    target.build(input_shape=(None,input_size))
    
    assert len(target.layers) == 3, \
        f"Wrong number of layers. Expected 3 but got {len(target.layers)}"
    target_input_shape = list(target.input_shape) if hasattr(target, 'input_shape') and target.input_shape is not None else list(target.input.shape)
    assert target_input_shape == [None, input_size], \
        f"Wrong input shape. Expected [None,  {input_size}] but got {target_input_shape}"
    i = 0
    expected = [[Dense, [None, 25], relu],
                [Dense, [None, 15], relu],
                [Dense, [None, classes], linear]]

    for layer in target.layers:
        assert type(layer) == expected[i][0], \
            f"Wrong type in layer {i}. Expected {expected[i][0]} but got {type(layer)}"
        layer_output_shape = list(layer.output_shape) if hasattr(layer, 'output_shape') else list(layer.output.shape)
        assert layer_output_shape == expected[i][1], \
            f"Wrong number of units in layer {i}. Expected {expected[i][1]} but got {layer_output_shape}"
        assert layer.activation == expected[i][2], \
            f"Wrong activation in layer {i}. Expected {expected[i][2]} but got {layer.activation}"
        i = i + 1

    print("\033[92mAll tests passed!")
    