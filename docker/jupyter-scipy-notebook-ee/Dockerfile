FROM jupyter/scipy-notebook:c7fb6660d096

LABEL maintainer="Tyler Erickson <tylere@google.com>"

USER root

# Upgrade JupyterLab
RUN conda install jupyterlab==0.30.5

# Install ipywidgets.
#   https://github.com/jupyter-widgets/ipywidgets
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
             libjpeg-dev \
             libgif-dev \
             libcairo2-dev \
             pkg-config \
  && pip install ipywidgets==7.0.5 \
  && jupyter nbextension enable --py --sys-prefix widgetsnbextension \
  && jupyter labextension install @jupyter-widgets/jupyterlab-manager@0.31.3 \
  && apt-get purge -y build-essential \
             dpkg-dev \
             pkg-config \
             fakeroot \
             libfakeroot:amd64 \
  && apt-get autoremove -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Install bqplot.
#   https://github.com/bloomberg/bqplot
RUN pip install bqplot==0.10.1 \
  && jupyter nbextension install bqplot --py --symlink --sys-prefix \
  && jupyter nbextension enable --py --sys-prefix bqplot \
  && jupyter labextension install bqplot

# Install ipyleaflet.
#   https://github.com/ellisonbg/ipyleaflet
RUN pip install ipyleaflet==0.5.1 \
  && jupyter nbextension enable --py --sys-prefix ipyleaflet \
  && jupyter labextension install jupyter-leaflet@0.5.0

# Install the Earth Engine Python API.
#   https://github.com/google/earthengine-api
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
             build-essential \
             libssl-dev \
             libffi-dev \
  && pip install cryptography \
  && pip install earthengine-api \
  && apt-get purge -y build-essential \
             libssl-dev \
             libffi-dev \
             dpkg-dev \
             fakeroot \
             libfakeroot:amd64 \
  && apt-get autoremove -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

USER $NB_USER

# Make sure contents are in HOME and owned by the non-root user, which is required by Binder.
# http://mybinder.readthedocs.io/en/latest/dockerfile.html#preparing-your-dockerfile
COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}
