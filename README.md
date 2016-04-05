grid-docker-bootstrap
=============
The Docker VM bootstrap loader.

This script is the first step of a Docker environment builder in a grid cluster. 

0. The grid-docker-bootstrap script directly executes "docker run" command with some proper VM image parameters and configurations in a cluster.
0. This script looks for /etc/grid-docker-bootstrap.conf, $HOME/.grid-docker-bootstrap.conf and read one of them according to this order.
0. $TMPDIR in the host is mounted on $DOCKER_TMPDIR in the VM. /root (=$DOCKER_HOME) is used for a working directory in the VM. 

Some other issues will be added later.


Usages
-----

 * Clone

 ```
git clone https://github.com/GenKawamura/grid-docker-bootstrap
cd grid-docker-bootstrap
```

 
 * Show usage

 ```
./grid-docker-bootstrap
```


 * Run

 ```
export DOCKER_IMG=b.gcr.io/tensorflow/tensorflow:latest-devel
./grid-docker-bootstrap python /tensorflow/tensorflow/models/image/mnist/convolutional.py
```


 * Run by interactive mode

 ```
export DOCKER_INTERACTIVE=ON
export DOCKER_IMG=b.gcr.io/tensorflow/tensorflow:latest-devel
./grid-docker-bootstrap
```
