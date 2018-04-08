FROM jupyter/scipy-notebook:92fe05d1e7e5

LABEL maintainer="Tyler Erickson <tylere@google.com>"

USER root

# Upgrade JupyterLab
RUN conda install jupyterlab==0.31.12

# Install bqplot.
#   https://github.com/bloomberg/bqplot
RUN pip install bqplot==0.10.5 \
  && jupyter nbextension install bqplot --py --symlink --sys-prefix \
  && jupyter nbextension enable --py --sys-prefix bqplot \
  && jupyter labextension install bqplot

# Install ipyleaflet.
#   https://github.com/ellisonbg/ipyleaflet
RUN pip install ipyleaflet==0.7.3 \
  && jupyter nbextension enable --py --sys-prefix ipyleaflet \
  && jupyter labextension install jupyter-leaflet

# Install Altair.
#   https://github.com/altair-viz/jupyter_vega
RUN pip install altair==2.0.0rc1 \
  && pip install --upgrade notebook \
  && jupyter labextension install @jupyterlab/vega3-extension

# Install sample Vega datasets.
RUN pip install vega_datasets

# Install Palettable (color maps)
RUN pip install palettable

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
