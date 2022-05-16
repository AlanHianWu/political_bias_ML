#import tensorflow as tf
import tensorflow.compat.v1 as tf


def load_pb(path_to_pb):
    with tf.gfile.GFile(path_to_pb, "rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
    with tf.Graph().as_default() as graph:
        tf.import_graph_def(graph_def, name='')
        return graph

graph = load_pb('saved_model.pb')

_input = graph.get_tensor_by_name('input:0')
_output = graph.get_tensor_by_name('output:0')
