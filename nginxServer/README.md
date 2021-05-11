## General

This is a docker image which uses the nginx/hello base image. It spins up an nginx server to serve the index.html associated with it.
For convienience, an alternative index.html is provided as index.html2 for the 'Change the Image Content' section. The additional questions 
are addressed throughout this README but are gathered here for convienience.

1. [Remove the container](#rm) by running `docker rm <container-name>` where `<container-name>` is the tag associated with the container.
2. [Modify](#change)  the index.html to the desired content and save. Rebuild a new image with a new version tag.
3. [Run](#run) the container on port 8081 by changing the port flag from `-p 8080:80` to `-p 8081:80`.

## Getting the Image
To build the image, `cd` into the 'nginx' directory where the Dockerfile is located and 
issue `docker image build -t <image-name:<version> .` For example: 

`docker image build -t myhellonginx:1.0 .`

Alternatively, you can pull this docker image from the docker hub:

`docker pull minhly/helloprotenus:1.0`

The image should be listed by inspecting `docker image ls`.

## <a name="run"></a>Running the Container
To run the container, enter `docker container run --name <container-name> -p 8080:80 <imagename:1.0>`. For example,

`docker container run --name nginxdemo -p 8080:80 minhly/helloprotenus:1.0`

would be possible if you chose to pull the image from docker hub from the above step. The name flag is optional but recommended for easy reference later on if you want to remove or stop the container.

If port 8080 is not available, you can enter another port number such as 8081 in the command above instead.

## <a name="rm"></a> Removing/Stopping the Container
You can remove the container by executing one of:

1. `docker rm <container-name>`
2. ``docker rm <container-id>``

where `<container-name>` is the tag name and `<container-id>` is the docker assigned container id. To get the container id, run
`docker container ls -a`. Note that you cannot remove a still running container. Stop the container first. To stop the container, replace the `rm` command with `stop`.

## <a name="change"></a>Changing the Image Content
You can modify what the nginx container serves by changing index.html:
1. Modify and save the contents of index.html. 
2. Create a new image with a new version tag `docker image build -t <imagename>s:2.0 .` For example

        docker image build -t minhly/helloprotenus:2.0 .
        
3. Test and run the new version 

        docker container run --name newhello -p 8080:80 minhly/helloprotenus:2.0 

