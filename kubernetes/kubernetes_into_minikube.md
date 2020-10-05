> Kubernetes is the most widely used container scheduler that has a massive community behind it.

Alternatives could be **Mesos and Marathon, Docker Swarm**. It’s not enough to run containers. We need to be able to scale them, to make them fault tolerant, to provide transparent communication across a cluster, and many other things. Containers are only a low-level piece of the puzzle. The real benefits are obtained with tools that sit on top of containers. 
Those tools are today known as container schedulers. They are our interface. We do not manage containers, they do.



Modern infrastructure:
> We’re living in an era without the need to SSH into servers.

Today, modern infrastructure is created from immutable images. Any upgrade is performed by building new images and performing rolling updates that will replace VMs one by one. Infrastructure dependencies are never changed at runtime. 
Tools like _Packer, Terraform, CloudFormation_, and the like are the answer to today’s problems.

One of the inherent benefits behind immutability is a clear division between infrastructure and deployments. Until not long ago, the two meshed together into an inseparable process. With infrastructure becoming a service, deployment processes can be clearly separated, thus allowing different teams, individuals, and expertise to take control.

### Why to Combine Containers and Schedulers?

Containers provide benefits that other deployment mechanisms do not.

- Services deployed as containers are isolated and immutable.

- Isolation provides reliability.

- Isolation helps with networking and volume management. It avoids conflicts. It allows us to deploy anything, anywhere, without worrying whether that something will clash with other processes running on the same server.

- Schedulers, combined with containers and virtual machines, provide the ultimate cluster management nirvana.

- They allow us to combine the developer’s necessity for rapid and frequent deployments with a sysadmin’s goals of stability and reproducibility.

### Setting up a local Kubernetes cluster on your machine.


1. We could, for example, create a few nodes with [Vagrant](https://www.vagrantup.com/) (a tool for building and managing virtual machine environments in a single workflow) and execute quite a few shell commands that would convert them into a Kubernetes cluster.

2. We could go even further and create a VirtualBox image that would have all the required software pre-installed and use it to create Vagrant VMs.

3. We could also use Ansible to run provisioning of those images as well as to execute all the commands required to join VMs into a cluster.

4. Minikube installation:
 - Kubernetes’ command-line tool, **kubectl**, is used to manage a cluster and applications running inside it. 
 - [Commands](https://gist.github.com/vfarcic/77ca05f4d16125b5a5a5dc30a1ade7fc):
 
`curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl`

`chmod +x ./kubectl`

`sudo mv ./kubectl /usr/local/bin/kubectl`

`kubectl version --output=yaml`

`curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/`

Deep dive in VirtualBox:

`minikube start --vm-driver=virtualbox`

So far in minikube we have: Docker, rkt and localkube library (simplified minikube architecture).

`minikube status`

UI? - `minikube dashboard`


5. Checking the Environment Variables within minikube

`minikube docker-env`

**PoI**: Both docker-machine env and minikube docker-env serve the same purpose. 
They output the environment variables required for a local Docker client to communicate with a remote Docker server. 
In this case, that Docker server is the one inside a VM created by Minikube.

`eval $(minikube docker-env)`   - shell configuration:We evaluated (created) the environment variables provided through the minikube docker-env command. 
As a result, every command we send to our local Docker client will be executed on the Minikube VM. Thus, connecting Docker client with Docker Server.

Steps to get in VM and verify running containers:

- `minikube ssh`
- `docker container ls`
- `exit`


Verify where kubectl is pointing:  
`kubectl config current-context`

To see the nodes:
`kubectl get nodes`

Components in the cluster: 
`kubectl get all --all-namespaces`

`minikube stop` - this command shuts down the Minikube Virtual Machine, but preserves all cluster state and data. Starting the cluster again will restore it to its previous state.
`minikube start` - start it again
`minikube delete` - this command shuts down and deletes the Minikube Virtual Machine. No data or state is preserved.

###### To explore

rkt is an application container engine developed for modern production cloud-native environments. 
It features a pod-native approach, a pluggable execution environment, and a well-defined surface area that makes it ideal for integration with other systems.

? is rkt about the concept of Kubernetes orchestration system?
