# Docker Image: Jupyter Notebook Scientific Python Stack + Earth Engine

This directory contains a Docker image configuration for adding
the Earth Engine Python API to the
[Jupyter Notebook Scientific Python Stack](https://github.com/jupyter/docker-stacks/tree/master/scipy-notebook).
The configuration file also installs several other
[Jupyter Widgets](http://jupyter.org/widgets) that are useful for working with
geospatial data.

# Building the Image

The Docker image can be built by opening up a terminal, navigating to this
directory, and running the `docker build` command:

```
docker build . -t jupyter-scipy-notebook-ee
```

The `-t` parameter assigns the tag/name `jupyter-scipy-notebook-ee` to the image.

# Running the Image

To create a Docker container and start up JupyterLab, execute the following
command:

```
docker run -it --rm -p 8888:8888 --hostname localhost -e JUPYTER_LAB_ENABLE=yes -v "$PWD:/home/jovyan/mount" jupyter-scipy-notebook-ee start.sh jupyter lab
```

This command will launch the JupyterLab UI.

The `-v` flag specifies a volume mount, which exposes the host's current
directory as the path `/home/jovyan/mount` within the container.
You may want to add additional volume mounts for commonly used directories
(like where you clone git repositories).

From within the JupyterLab UI, you can open up a terminal tab, and use the
Earth Engine
[Command Line Tool](https://developers.google.com/earth-engine/command_line)
to authenticate the container's access to the Earth Engine servers.

```
jovyan@1234567890ab:~$ earthengine authenticate
Opening the following address in a web browser:

    https://accounts.google.com/o/oauth2/auth? ...

Please authorize access to your Earth Engine account, and paste the generated
code below. If the web browser does not start, please manually browse the URL
above.

Please enter authorization code: XXXXXXXXXXXXXXXXXXXXXXXX

Successfully saved authorization token.
```

Now that you have authencated the server, from within a Notebook you can import
and initialize the Earth Engine Python API.
