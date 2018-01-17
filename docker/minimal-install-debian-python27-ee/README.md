# Minimal Earth Engine Python API Image

This directory contains a Docker image configuration for a minimal container containing the Earth Engine Python API.
(No Jupyter libraries are included.)

# Building the Image

The Docker image can be built by opening up a terminal, navigating to this directory, and running
the `docker build` command:

```
docker build . -t debian-python27-ee
```

The `-t` parameter assigns the tag/name `debian-python27-ee` to the image.

# Running the Image

To create a Docker container and run it, execute the following command:

```
docker run -it debian-python27-ee
```

This will provide a bash shell prompt for the container (because the [Dockerfile](Dockerfile) specifies an entry point of /bin/bash).

Using the bash shell you can use the Earth Engine [Command Line Tool](https://developers.google.com/earth-engine/command_line)
to authenticate the container's access to the Earth Engine servers.

```
$ docker run -it debian-python27-ee
root@1f439fe712a0:/# earthengine authenticate
Opening the following address in a web browser:

    https://accounts.google.com/o/oauth2/auth? ...

Please authorize access to your Earth Engine account, and paste the generated code below. If the web browser does not start, please manually browse the URL above.

Please enter authorization code: XXXXXXXXXXXXXXXXXXXXXXXX

Successfully saved authorization token.
```

From within the bash shell you can also open a Python shell to import and initialize the Earth Engine Python API.

```
root@1f439fe712a0:/# python
Python 2.7.13 (default, Nov 24 2017, 17:33:09) 
[GCC 6.3.0 20170516] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import ee
>>> ee.Initialize()
>>> 
```