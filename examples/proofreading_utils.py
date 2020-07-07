import os
from glob import glob

import imageio
import h5py
import numpy as np
import skimage.color as skc

from batchlib.util import read_image, read_table
from scipy.ndimage import convolve
from scipy.ndimage.morphology import binary_erosion


def normalize(im):
    im = im.astype('float32')
    im -= im.min()
    im /= im.max()
    return im


def quantile_normalize(im, low=.01, high=.99):
    tlow, thigh = np.quantile(im, low), np.quantile(im, high)
    im -= tlow
    im /= thigh
    return np.clip(im, 0., 1.)


def make_2d_edges(segmentation):
    gy = convolve(segmentation + 1, np.array([-1., 0., 1.]).reshape(1, 3))
    gx = convolve(segmentation + 1, np.array([-1., 0., 1.]).reshape(3, 1))
    return ((gx ** 2 + gy ** 2) > 0)


def get_edge_segmentation(seg, iters):
    seg_ids = np.unique(seg)[1:]
    new_seg = np.zeros_like(seg)
    for seg_id in seg_ids:
        seg_mask = seg == seg_id
        eroded_mask = binary_erosion(seg_mask, iterations=iters)
        edge_mask = np.logical_xor(seg_mask, eroded_mask)
        new_seg[edge_mask] = seg_id
    return new_seg


# TODO enable quantile normalization for other channels to be robust to artifacts
def get_image_edges_and_labels(path, saturation_factor=1.5, edge_width=2, return_seg=False):
    with h5py.File(path, 'r') as f:
        serum = normalize(read_image(f, 'serum_IgG'))
        marker = quantile_normalize(read_image(f, 'marker'))
        nuclei = normalize(read_image(f, 'nuclei'))

        seg = read_image(f, 'cell_segmentation')
        _, infected_labels = read_table(f, 'infected_cell_labels')
        assert len(infected_labels) == seg.max() + 1
        assert infected_labels.shape[1] == 2

    bg_mask = seg == 0

    def subtract_bg(raw):
        bg = np.median(raw[bg_mask])
        raw -= bg
        return raw

    serum = subtract_bg(serum)
    marker = subtract_bg(marker)
    nuclei = subtract_bg(nuclei)

    infected_labels = infected_labels[:, 1]
    edges = get_edge_segmentation(seg, edge_width)

    raw = np.concatenate([marker[..., None], serum[..., None], nuclei[..., None]], axis=-1)
    if saturation_factor > 1:
        raw = skc.rgb2hsv(raw)
        raw[..., 1] *= saturation_factor
        raw = skc.hsv2rgb(raw).clip(0, 1)

    if return_seg:
        return raw, edges, infected_labels, seg
    else:
        return raw, edges, infected_labels


def export_proofreading_image(path, saturation_factor=1.5):
    raw, edges, infected_labels = get_image_edges_and_labels(path, saturation_factor)
    seg_ids = np.unique(edges)

    pos_edges = np.isin(edges, seg_ids[infected_labels == 1])
    neg_edges = np.isin(edges, seg_ids[infected_labels == 2])

    imageio.imwrite(path.replace('.h5', '_raw.png'), raw)

    raw[pos_edges, :] = [1, 0.6, 0]  # orange
    raw[neg_edges, :] = [0, 1, 1]  # cyan
    imageio.imwrite(path.replace('.h5', '.png'), raw)

    imageio.imwrite(path.replace('.h5', '_pos_edges.png'), pos_edges.astype('float32'))
    imageio.imwrite(path.replace('.h5', '_neg_edges.png'), neg_edges.astype('float32'))


def plot_all(root):
    for path in glob(os.path.join(root, '*.h5')):
        export_proofreading_image(path)


if __name__ == '__main__':
    plot_all()
