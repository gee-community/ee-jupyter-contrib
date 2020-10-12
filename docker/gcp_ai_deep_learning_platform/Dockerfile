# If updating, look for new versions of the base image:
#   gcloud container images list --repository="gcr.io/deeplearning-platform-release"
FROM gcr.io/deeplearning-platform-release/tf2-cpu.2-3
LABEL base-image="gcr.io/deeplearning-platform-release/tf2-cpu.2-3"
LABEL maintainer="Tyler Erickson <tylere@google.com>"

# Altair - Declarative visualization in Python
#     docs: https://altair-viz.github.io
#   source: https://github.com/altair-viz/altair
#     pkgs: mamba repoquery search altair
ARG ALTAIR_VERSION=4.1.0

# Earth Engine Python API 
#     home: https://earthengine.google.com
#     docs: https://developers.google.com/earth-engine
#   source: https://github.com/google/earthengine-api
#     pkgs: mamba repoquery search earthengine-api
ARG EARTHENGINE_API_VERSION=0.1.238

# geemap - Interactive mapping of Earth Engine data in Jupyter notebooks
#     docs: https://geemap.readthedocs.io
#   source: https://github.com/giswqs/geemap
#     pkgs: mamba repoquery search geemap
ARG GEEMAP_VERSION=0.7.13

# ipyvolume - 3d plotting in the Jupyter notebook
#     docs: https://ipyvolume.readthedocs.io/
#   source: https://github.com/maartenbreddels/ipyvolume
#     pkgs: mamba repoquery search ipyvolume
#           npm search jupyter-threejs
ARG IPYVOLUME_VERSION=0.5.2
ARG THREEJS_VERSION=2.2.0

# Palettable - color maps
#     docs: https://jiffyclub.github.io/palettable
#   source: https://github.com/jiffyclub/palettable
#     pkgs: mamba repoquery search palettable
ARG PALETTABLE_VERSION=3.3.0

# Vega Datasets - Collection of datasets used in Vega and Vega-Lite examples
#     docs: http://vega.github.io/vega-datasets
#   source: https://github.com/vega/vega-datasets
#     pkgs: mamba repoquery search vega_datasets
ARG VEGA_DATASETS_VERSION=0.8.0

RUN conda update -n base -c defaults --yes conda
RUN conda install -c conda-forge --verbose mamba

RUN mamba install -c conda-forge --yes \
        altair=${ALTAIR_VERSION} \
        earthengine-api=${EARTHENGINE_API_VERSION} \
        geemap=${GEEMAP_VERSION} \
        palettable=${PALETTABLE_VERSION} \
        vega_datasets=${VEGA_DATASETS_VERSION} \
   && mamba clean --all -f -y

# Install and enable JupyterLab extensions
RUN jupyter labextension update --no-build nbdime-jupyterlab \
    && jupyter labextension install --no-build @jupyter-widgets/jupyterlab-manager \
                                               jupyter-leaflet \
                                               bqplot \
    && jupyter lab build --dev-build=False --minimize=False \
    # Clean up
    && npm cache clean --force
