import urllib, io, os
import matplotlib
import matplotlib.pyplot as plt

# Utility functions used to retrieve and cache images locally, ensures 
# that thumbnails are shown in notebooks

def get_path(image, region, dimensions):
    return image.getThumbURL({
        'region' : region.getInfo(), 
        'format': 'png', 
        'dimensions': dimensions
    })

def retrieve(image, path_out, region, dimensions):
    path = get_path(image, region, dimensions)
    
    if os.path.exists(path_out):
            os.remove(path_out)
    
    urllib.request.urlretrieve(path, path_out)

def show(image, path_out, region, dimensions=256):
    plt.grid(False)
    
    if path_out:
        retrieve(image, path_out, region, dimensions)
        plt.imshow(plt.imread(path_out))
    else:
        display(Image(url=get_path(image, region, dimensions)))
        