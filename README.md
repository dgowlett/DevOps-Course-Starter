# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. This project uses the official distribution of Python version 3.7+ the installation instrution below however will install these for you
(as found in the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

## Dependencies

This App uses the Trello site to store the Card and list information that the App uses, therefore the following variables will need to be provided after creating a trello account from https://trello.com and creation of a new Board followed by generation of a required api key and token from https://trello.com/1/appKey/generate, these will be requested when installing the App in the next section

TRELLO_API_KEY
TRELLO_API_TOKEN
TRELLO_BOARD_ID

## Installing and running the App

Note: These instructions below require that the user id is ec2-user is used

This App uses Ansible to install and run the App using a Control Node and Managed Node (aka the Host that runs the App)
It is required that the Control Node has ssh with no password required access to the Managed Node by creating a ssh key
pair using ssh-keygen command on the Control Node and this will generate the required key pair under the .ssh directory.  You will then need to copy the public key over from the Control Node to the Managed Node and using something like 'ssh-copy-id ec2-user@<ip address of then Managed Node> which will acheive this and you will be prompted for the password on last time.

From the Control node run 'ansible --version' to make sure that ansible is installed and available, if not install ansible using 'pip install ansible'

Copy the following files to the Control Node

inventory
playbook.yml
.env.j2

Change the IP address/s (Managed Node IP) under the ManagedNodes group in the inventory file if required
Change the IP address/s (Managed Node IP) in the Hosts setting in the playbook.yml file if required

Now run ansible from the Control Node to setup and run the App, you will be prompted first for the Trello authentication and Board id details

$ ansible-playbook playbook.yml -i inventory

After a sucessful installtion you can now open up a browser and navagate to the <Managed Node IP>:5000/ to acess the App
