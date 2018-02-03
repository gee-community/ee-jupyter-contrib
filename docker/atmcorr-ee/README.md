# Docker Image: Atmospheric Correction in Earth Engine

This directory contains a Docker image configuration for atmospheric correction with [Py6S](http://py6s.readthedocs.io/en/latest/) and Earth Engine.

# Building the Image

The Docker image can be built by opening up a terminal, navigating to this
directory, and running the `docker build` command:

```
docker build . -t atmcorr-ee
```

The `-t` parameter assigns the tag/name `atmcorr-ee` to the image.

# Running the Image

To create a Docker container with access to a web browser

```
docker run -i -t -p 8888:8888 atmcorr-ee
```

Once inside the container, authenticate Earth Engine

`earthengine authenticate`

get the source code from [this repo](https://github.com/samsammurphy/gee-atmcorr-S2) for an example application with Sentinel 2 using the following command:

`git clone https://github.com/samsammurphy/gee-atmcorr-S2`

then run the example jupyter notebook

```
cd gee-atmcorr-S2/jupyer_notebooks/
jupyter-notebook sentinel2_atmospheric_correction.ipynb --ip='*' --port=8888 --allow-root
```

this will print out a URL that you can use in your web browser to run the code.

perfect.

# Result

If all went well then you should be able to see a before and after set of images similar to this one

![](https://media.githubusercontent.com/media/gee-community/ee-jupyter-contrib/atmcorr-ee/docker/atmcorr-ee/images/before_and_after.png)
