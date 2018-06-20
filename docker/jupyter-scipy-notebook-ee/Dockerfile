FROM jupyter/scipy-notebook:59904dd7776a
LABEL base-image="jupyter/scipy-notebook:59904dd7776a 6/6/2018"

LABEL maintainer="Tyler Erickson <tylere@google.com>"

USER root

RUN conda install -c conda-forge \
  ipywidgets \
  altair \
  vega_datasets

# Install nbgitpuller (Notebook Git Puller).
# https://github.com/data-8/nbgitpuller
RUN pip install git+https://github.com/data-8/nbgitpuller \
  && jupyter serverextension enable --py nbgitpuller --sys-prefix

# Install the JupyterLab Sidecar.
# https://github.com/jupyter-widgets/jupyterlab-sidecar
RUN pip install sidecar

# Install ipyleaflet (Leaflet-based interactiving mapping widget).
# https://github.com/jupyter-widgets/ipyleaflet
ARG IPYLEAFLET_VERSION=0.8.1
RUN pip install ipyleaflet==$IPYLEAFLET_VERSION \
  && jupyter nbextension enable --py --sys-prefix ipyleaflet \
  && jupyter labextension install --no-build jupyter-leaflet@0.8.1

# Install bqplot.
# https://github.com/bloomberg/bqplot
ARG BQPLOT_VERSION=0.10.1
RUN pip install bqplot==$BQPLOT_VERSION \
  && jupyter nbextension install bqplot --py --symlink --sys-prefix \
  && jupyter nbextension enable --py --sys-prefix bqplot \
  && jupyter labextension install --no-build bqplot

# Install nbdime (Notebook Diff & Merge tool).
# https://github.com/jupyter/nbdime
RUN pip install nbdime 

# Install the Table of Contents extension.
RUN jupyter labextension install  --no-build jupyterlab-toc

# Build all the JupyterLab extensions.
RUN jupyter lab build

# Install ipythonblocks (colored grids) and Palettable (color maps)
RUN pip install ipythonblocks \
  && pip install palettable

# Install Tensorflow. (https://www.tensorflow.org/)
RUN pip install tensorflow

# Install the Earth Engine Python API. (https://github.com/google/earthengine-api)
RUN conda install -c conda-forge earthengine-api

# Install libraries for working with Google tools.
RUN pip install PyDrive \
  && pip install --upgrade google-cloud

USER $NB_USER