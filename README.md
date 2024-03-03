# Introduction
An attempt to learn LangChain and LLM with Ollama.

## Environment setup:
The following steps have to be done manually

### Infrastructure:
* Create a GCP VM instance --  32 GB, 8 Cores, 100 GB storage - OS: Debian/Ubuntu
* Setup firewall to allow http, https and other ports (like 8888 for jupyter notebooks)
* Setup static IP
* Verify ssh connectivity based on key from your local system -> [see this page for more info](https://cloud.google.com/compute/docs/connect/standard-ssh#thirdpartytools)



### Software to be installed:


Python3 if not already installed:

```bash
$ sudo apt install python3
```

Install pip:

```bash
$ sudo apt install pip
```

Next, install python virtual environemnts - [venv](https://peps.python.org/pep-0668/). 

```bash
$ sudo apt install python3.11-venv
```

Create a activate a virtual envrionment as follows:

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
```

After this only pip can be used for installing python packages (otherwise we will get ["error:externally-managed-environment"](https://stackoverflow.com/questions/75608323/how-do-i-solve-error-externally-managed-environment-every-time-i-use-pip-3) error message).

Install pip dependencies for Langchain as shown below:

```bash
$ pip install langchain
$ pip install beautifulsoup4
$ pip install langchain_community
$ pip install faiss-cpu

```

Install ollama by using the following command:

```bash
$ curl -fsSL https://ollama.com/install.sh | sh
```

Pull llama2 and mistral models by the following command:

```bash
$ ollama pull llama2
$ ollama pull mistral
```

## Setup Git
### Install Git
Install git as follows:
```bash
$ sudo apt install git
```

### Setup configs
Setup configuration for git as follows:

```bash
$ git config --global user.name "FIRST_NAME LAST_NAME"
$ git config --global user.email "MY_NAME@example.com"

```

### Gitignore file
Create a gitignore file and add .venv/ as an entry


### Jupyter Lab setup
Jupyter Lab notebook is useful for testing langchain code samples. Can be installed as follows:

```bash
$ pip install jupyterlab
```

After the installation, it can be laucnhed as follows:

```bash
$ jupyterlab lab
```

This will launch jupyterlab application webserver at localhost:8888

#### Accessing this from remote/dev computer
Since the Jupyter application is hosted in remote environment, it would be good to access it from the development computer. In order do to that, an SSL Tunnel can be opened as follows:

```bash
$ # ssh tunnel
$ ssh -L 8888:localhost:8888 [user]@[vm-external-ip]
```

Post this the application can be reached from development computer's localhost:8888


### Streamlit Integration

Streamlit provides a quick and easy way to integrate python based backend apps to a nice and functional UI. To get going, install the following dependencies

```bash
$ pip install streamlit
$ pip install litellm
```

Pull Mistral 7B model as follows:

```bash
$ ollama pull mistral
```

Verify that model is pulled by checking if mistral is dowloaded and available by listing the available models in ollama

```bash
$ ollama list
```

Then start the streamlit app that is available as part of the src dir as follows:

```bash
$ streamlit run src/streamlit_app.py 
```

#### Configuring networks, VPC in Google compute instance
Make sure we connect our VM to an external VPC (not the default VPC) that has a connectivity/route to the Internet gateway. You may have to stop the VM to disassociate the existing default VPC and add the new external VPC.

Post this, add firewall rules in the external VPC for ssh and the ports used by streamlit. After this, we should be access the application at http://[Google_VM's_Ext_IP]:[Streamlit_Port]