from qtconsole.inprocess import QtInProcessKernelManager
from IPython import get_ipython

# Check if there is an ipython shell
shell = get_ipython()
assert shell == None

# Start in process kernel manager and client
kernel_manager = QtInProcessKernelManager()
kernel_manager.start_kernel(show_banner=False)
kernel_manager.kernel.gui = 'qt'
kernel_client = kernel_manager.client()
kernel_client.start_channels()

# Shutdown kernel manager and client
kernel_client.stop_channels()
kernel_manager.shutdown_kernel()

# Check there is no longer an ipython shell
shell = get_ipython()
assert shell == None
