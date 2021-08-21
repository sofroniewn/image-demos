import fiftyone.zoo as foz
import napari
from qtpy.QtWidgets import QListWidget
from imageio import imread
import numpy as np


def detections_to_shapes(detections, frame_size, metadata=None):
    """Convert a list of detections into a shapes tuple.
    
    Parameters
    ----------
    detections : fiftyone.core.labels.Detection

    Returns
    -------
    tuple
        Shape layer data tuple, consisting of list of shapes
        layer data, shapes layer metadata, and `Shapes`.
    """
    polylines = detections.to_polylines().polylines
    shapes_data = []
    properties = {}
    for polyline in polylines:
        polyline_dict = polyline.to_dict()
        points = np.array(polyline_dict.pop('points')[0])[:, ::-1]
        points = np.multiply(points, frame_size)
        shapes_data.append(points)
        for key, value in polyline_dict.items():
            if not isinstance(value, dict) and not isinstance(value, list):
                existing_values = properties.get(key, [])
                existing_values.append(value)
                properties[key] = existing_values
    layer_metadata = {'properties': properties, 'shape_type': 'polygon'}
    if metadata is not None:
        layer_metadata.update(metadata)

    return shapes_data, layer_metadata, 'Shapes'


def sample_to_image(sample):
    image = imread(sample.filepath)
    metadata = {}
    metadata['name'] = sample.id
    return (image, metadata, 'Image')


def sample_to_layers(sample):
    layer_data = []
    image_data = sample_to_image(sample)
    frame_size = image_data[0].shape[:-1]
    layer_data.append(image_data)
    metadata = {'name': 'ground_truth',
                'edge_width':2,
                'edge_color': 'green',
                'face_color':'transparent',
                'text': {
                    'text': 'label',
                    'size': 12,
                    'color': 'green',
                    'anchor': 'upper_left',
                    'translation': [-1, 0],
                    }
                }
    layer_data.append(detections_to_shapes(sample.ground_truth, frame_size, metadata))
    metadata = {'name': 'predictions',
                'edge_width':2,
                'edge_color': 'red',
                'face_color':'transparent',
                'text': {
                    'text': 'label',
                    'size': 12,
                    'color': 'red',
                    'anchor': 'upper_left',
                    'translation': [-1, 0],
                    }
                }
    layer_data.append(detections_to_shapes(sample.predictions, frame_size, metadata))
    return layer_data


def load_sample(idx):
    idx = int(idx.text())
    print('Loading', idx, '...')
    sample = samples[idx]
    viewer.layers.select_all()
    viewer.layers.remove_selected()
    layer_data = sample_to_layers(sample)    
    for ld in layer_data:
        viewer._add_layer_from_data(*ld)
    print('... done.')


dataset = foz.load_zoo_dataset("quickstart")
samples = list(dataset.iter_samples())

viewer = napari.Viewer()

list_widget = QListWidget()
for n in range(len(samples)):
    list_widget.addItem(str(n))
list_widget.currentItemChanged.connect(load_sample)

viewer.window.add_dock_widget(list_widget, area='right')

napari.run()