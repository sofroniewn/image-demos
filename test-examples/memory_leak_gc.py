import gc
import weakref
import sys
import napari

viewer = napari.Viewer()
r = weakref.ref(viewer.add_points())

viewer.layers.pop()
print(gc.collect(), "unreachable objects after collection")

print("referenced layer is:", repr(r()))

print(f"\n{sys.getrefcount(r()) - 1} remaining references:")
for q in enumerate(gc.get_referrers(r())):
    print(q[0], q[1])