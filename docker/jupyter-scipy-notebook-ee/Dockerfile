FROM jupyter/scipy-notebook:75d7f5e4f76d
LABEL base-image="jupyter/scipy-notebook:75d7f5e4f76d 2020-07-20"
LABEL maintainer="Tyler Erickson <tylere@google.com>"

# Altair - Declarative visualization in Python
#     docs: https://altair-viz.github.io
#   source: https://github.com/altair-viz/altair
#     pkgs: conda search -c conda-forge altair
ARG ALTAIR_VERSION=4.1.0

# bqplot - Grammar of Graphics-based interactive plotting framework for the Jupyter notebook
#     docs: https://bqplot.readthedocs.io
#   source: https://github.com/bloomberg/bqplot
#     pkgs: conda search -c conda-forge bqplot
#           npm search bqplot
ARG BQPLOT_VERSION=0.12.14
ARG BQPLOT_NPM_VERSION=0.5.14

# Earth Engine Python API 
#     home: https://earthengine.google.com
#     docs: https://developers.google.com/earth-engine
#   source: https://github.com/google/earthengine-api
#     pkgs: conda search -c conda-forge earthengine-api
ARG EARTHENGINE_API_VERSION=0.1.227

# ipyleaflet - Leaflet-based interactiving mapping widget
#     docs: https://ipyleaflet.readthedocs.io
#   source: https://github.com/jupyter-widgets/ipyleaflet
#     pkgs: conda search -c conda-forge ipyleaflet
ARG IPYLEAFLET_VERSION=0.13.1

# ipyvolume - 3d plotting in the Jupyter notebook
#     docs: https://ipyvolume.readthedocs.io/
#   source: https://github.com/maartenbreddels/ipyvolume
#     pkgs: conda search -c conda-forge ipyvolume
#           npm search jupyter-threejs
ARG IPYVOLUME_VERSION=0.5.2
ARG THREEJS_VERSION=2.1.1

# jupyterlab-manager
#   source: https://github.com/jupyter-widgets/ipywidgets/tree/master/packages/jupyterlab-manager
#     pkgs: npm search @jupyter-widgets/jupyterlab-manager
ARG WIDGETS_JUPYTERLAB_MANAGER_VERSION=2.0.0

# nbdime - Notebook Diff & Merge tool
#     docs: https://nbdime.readthedocs.io
#   source: https://github.com/jupyter/nbdime
#     pkgs: conda search -c conda-forge nbdime
ARG NBDIME_VERSION=2.0.0

# Palettable - color maps
#     docs: https://jiffyclub.github.io/palettable
#   source: https://github.com/jiffyclub/palettable
#     pkgs: conda search -c conda-forge palettable
ARG PALETTABLE_VERSION=3.2.0

# PyDrive - Simplifies many Google Drive API tasks
#     home: https://pypi.org/project/PyDrive
#     docs: https://pythonhosted.org/PyDrive
#   source: https://github.com/gsuitedevs/PyDrive
#     pkgs: conda search -c conda-forge pydrive
ARG PYDRIVE_VERSION=3.3.0

# TensorFlow - Computation using data flow graphs for scalable machine learning
#     home: https://www.tensorflow.org
#     docs: https://www.tensorflow.org/api_docs
#   source: https://github.com/tensorflow/tensorflow
#     pkgs: conda search -c conda-forge tensorflow
ARG TENSORFLOW_VERSION=2.0.0

# Vega Datasets - Collection of datasets used in Vega and Vega-Lite examples
#     docs: http://vega.github.io/vega-datasets
#   source: https://github.com/vega/vega-datasets
#     pkgs: conda search -c conda-forge vega_datasets
ARG VEGA_DATASETS_VERSION=0.8.0

#### Other packages
#
# nbgitpuller - Notebook Git Puller
#   source: https://github.com/data-8/nbgitpuller
#
# Sidecar - A sidecar output widget for JupyterLab
#   source: https://github.com/jupyter-widgets/jupyterlab-sidecar
#
# ipythonblocks - colored grids
#   home: http://www.ipythonblocks.org/

RUN conda update -n base conda &&\ 
    conda install --quiet --yes \
        conda-build \
        altair=${ALTAIR_VERSION} \
        bqplot=${BQPLOT_VERSION} \
        earthengine-api=${EARTHENGINE_API_VERSION} \
        ipyleaflet=${IPYLEAFLET_VERSION} \
        ipyvolume=${IPYVOLUME_VERSION} \
        nbdime=${NBDIME_VERSION} \
        palettable=${PALETTABLE_VERSION} \
        pydrive=${PYDRIVE_VERSION} \
        tensorflow=${TENSORFLOW_VERSION} \
        vega_datasets=${VEGA_DATASETS_VERSION} \
      && \
    conda upgrade --all && \
    conda build purge-all && \
    jupyter nbextension enable --py widgetsnbextension --sys-prefix && \
    # JupyterLab Extensions
    pip install sidecar && \
    jupyter labextension install --no-build jupyter-leaflet@${IPYLEAFLET_VERSION} && \
    jupyter labextension install --no-build ipyvolume@${IPYVOLUME_VERSION} && \
    jupyter labextension install --no-build jupyter-threejs@${THREEJS_VERSION} && \
    jupyter labextension install --no-build bqplot@${BQPLOT_NPM_VERSION} && \
    jupyter labextension install --no-build @jupyter-widgets/jupyterlab-manager && \
    jupyter labextension install --no-build @jupyter-widgets/jupyterlab-sidecar && \
    pip install ipythonblocks && \
    export NODE_OPTIONS=--max-old-space-size=16000 && \
    jupyter lab build && \
    # Clean up
    npm cache clean --force && \
    rm -rf $CONDA_DIR/share/jupyter/lab/staging && \
    rm -rf /home/$NB_USER/.cache/yarn && \
    rm -rf /home/$NB_USER/.node-gyp && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER
