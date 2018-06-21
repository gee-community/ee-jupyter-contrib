FROM jupyter/scipy-notebook:03b897d05f16
LABEL base-image="jupyter/scipy-notebook:03b897d05f16 6/13/2018"

LABEL maintainer="Tyler Erickson <tylere@google.com>"

USER root

# ipyleaflet - Leaflet-based interactiving mapping widget
#     docs: https://ipyleaflet.readthedocs.io
#   source: https://github.com/jupyter-widgets/ipyleaflet
#     pkgs: conda search -c conda-forge ipyleaflet
ARG IPYLEAFLET_VERSION=0.8.4

# ipywidgets - Interactive Widgets for the Jupyter Notebook
#     docs: https://ipywidgets.readthedocs.io
#   source: https://github.com/jupyter-widgets/ipywidgets
#     pkgs: conda search -c conda-forge ipywidgets
ARG IPYWIDGETS_VERSION=7.2.1

# Altair - Declarative visualization in Python
#     docs: https://altair-viz.github.io
#   source: https://github.com/altair-viz/altair
#     pkgs: conda search -c conda-forge altair
ARG ALTAIR_VERSION=2.1.0

# Vega Datasets - Collection of datasets used in Vega and Vega-Lite examples
#     docs: http://vega.github.io/vega-datasets
#   source: https://github.com/vega/vega-datasets
#     pkgs: source: https://github.com/vega/vega-datasets
ARG VEGA_DATASETS_VERSION=0.5.0

# bqplot - Grammar of Graphics-based interactive plotting framework for the Jupyter notebook
#     docs: https://bqplot.readthedocs.io
#   source: https://github.com/bloomberg/bqplot
#     pkgs: conda search -c conda-forge bqplot
ARG BQPLOT_VERSION=0.10.5

# nbdime - Notebook Diff & Merge tool
#     docs: https://nbdime.readthedocs.io
#   source: https://github.com/jupyter/nbdime
#     pkgs: conda search -c conda-forge nbdime
ARG NBDIME_VERSION=1.0.1

# Palettable - color maps
#     docs: https://jiffyclub.github.io/palettable
#   source: https://github.com/jiffyclub/palettable
#     pkgs: conda search -c conda-forge palettable
ARG PALETTABLE_VERSION=3.1.1

# TensorFlow - Computation using data flow graphs for scalable machine learning
#     home: https://www.tensorflow.org
#     docs: https://www.tensorflow.org/api_docs
#   source: https://github.com/tensorflow/tensorflow
#     pkgs: conda search -c conda-forge tensorflow
ARG TENSORFLOW_VERSION=1.8.0

# Earth Engine Python API 
#     home: https://earthengine.google.com
#     docs: https://developers.google.com/earth-engine
#   source: https://github.com/google/earthengine-api
#     pkgs: conda search -c conda-forge earthengine-api
ARG EARTHENGINE_API_VERSION=0.1.141

RUN conda install -c conda-forge \
  ipywidgets=$IPYWIDGETS_VERSION \
  ipyleaflet=$IPYLEAFLET_VERSION \
  altair=$ALTAIR_VERSION \
  vega_datasets=$VEGA_DATASETS_VERSION \
  bqplot=$BQPLOT_VERSION \
  nbdime=$NBDIME_VERSION \
  palettable=$PALETTABLE_VERSION \
  tensorflow=$TENSORFLOW_VERSION \
  earthengine-api=$EARTHENGINE_API_VERSION

# Enable JupyterLab extensions.
RUN jupyter labextension install --no-build \
  jupyter-leaflet \
  bqplot \
  jupyterlab-toc

# Install nbgitpuller (Notebook Git Puller).
# https://github.com/data-8/nbgitpuller
RUN pip install git+https://github.com/data-8/nbgitpuller \
  && jupyter serverextension enable --py nbgitpuller --sys-prefix

# Install the JupyterLab Sidecar.
# https://github.com/jupyter-widgets/jupyterlab-sidecar
RUN pip install sidecar

# Build all the JupyterLab extensions.
RUN jupyter lab build

# Install ipythonblocks (colored grids)
RUN pip install ipythonblocks 

# Install libraries for working with Google tools.
RUN pip install PyDrive \
  && pip install --upgrade google-cloud

USER $NB_USER