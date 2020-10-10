# Docker Image: AI Platform Notebook Deep Learning + Earth Engine

This directory contains a Docker image configuration for adding
the Earth Engine Python API to an
[AI Platform Deep Learning VM Image](https://cloud.google.com/deep-learning-vm).
The configuration file also installs the [geemap](https://github.com/giswqs/geemap) and several other
[Jupyter Widgets](http://jupyter.org/widgets) packages that are useful for working with
geospatial data.

## Local development

### Setup

* Install Docker:
https://docs.docker.com/get-docker/
* Install mamba:
https://github.com/TheSnakePit/mamba
`conda install mamba -c conda-forge`
* Install node.js:
`conda install -c conda-forge nodejs`

### Build a container image

Navigate to the directory containing the Dockerfile.
Update the Dockerfile as needed.

Build a Docker image, assiging a name/tag to the image.

```docker build . --tag gcp_ai_deep_learning_platform_ee```

Run the Docker image to create a container, using port 8080 and mapping your local home directory to the container's home directory for the default "jupyter" user:

```docker run -p 8080:8080 -v $HOME:/home/jupyter gcp_ai_deep_learning_platform_ee```
