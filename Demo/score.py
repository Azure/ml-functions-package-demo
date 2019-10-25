import tensorflow as tf
from azureml.core.model import Model
import json

def init():
    global session
    global input_map
    global output_tensor_names
    global output_output_names

    session = tf.Session()

    model_path = Model.get_model_path('abs')
    model = tf.saved_model.loader.load(session, ['serve'], model_path)
    input_map = {name:tensor.name for (name,tensor) in model.signature_def['serving_default'].inputs.items()}
    output_map = {name:tensor.name for (name,tensor) in model.signature_def['serving_default'].outputs.items()}
    output_output_names, output_tensor_names = zip(*output_map.items())

input_sample = {"input":[-1,-2,-3,-4]}
output_sample = {"abs":[1,2,3,4]}


def run(raw):
    data = json.loads(raw)
    data = {tensorName:data[name] for (name, tensorName) in input_map.items()}
    result = session.run(output_tensor_names, data)
    return dict(zip(output_output_names, [res.tolist() for res in result]))


if __name__ == "__main__":
    init()
    out = run(json.dumps(input_sample))
    print("output {}".format(out))
    print("expected output {}".format(out))
