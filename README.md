
# Python-Lectures

## Introduction

Python is a modern, robust, high level programming language. It is very easy to pick up even if you are completely new to programming.

## Python Installation

### 1. Official distribution

Mac OS X and Linux comes pre installed with python. Windows users can download python from https://www.python.org/downloads/ .

To install a package (for example jupyter) run,

    $> pip install --user jupyter[all]
    
This will install all the necessary dependencies for the notebook, qtconsole, tests etc.

### 2. Unofficial distributions

Installing all the necessary libraries might prove troublesome. Anaconda and Canopy comes pre packaged with all the necessary python libraries and also IPython.

#### Anaconda [RECOMMENDED]

Leading Open Data Science Platform Powered by Python

Anaconda Distribution gives superpowers to people that change the world with high performance, cross-platform Python and R that includes the best innovative data science from open source. Using over 720 packages for data preparation, data analysis, data visualization, machine learning and interactive data science applications that deliver results - everything from discovering gravitational waves to creating new revenue channels. Data Scientists worldwide rely on the Anaconda Distribution for easy package, dependency and environment management.


Download Anaconda from https://www.continuum.io/downloads

Anaconda is completely free and includes more than 700 python packages. Both python 2.7 and 3.5 options are available.

More information: https://docs.continuum.io/

#### Canopy

Download Canopy from https://store.enthought.com/downloads/#default

Canopy has a premium version which offers 300+ python packages. But the free version works just fine. Canopy as of now supports only 2.7 but it comes with its own text editor and IPython environment.

## Virtual environments

We will get you to install an extremely useful tool to help keep your coding environment tidy on your computer. It's possible to skip this step, but it's highly recommended. Starting with the best possible setup will save you a lot of trouble in the future!

So, let's create a virtual environment (also called a virtualenv). Virtualenv will isolate your Python setup on a per-project basis.

### 1. Using Anaconda

### Create virtual environment
Creating a virtualenv on both Linux and OS X is as simple as running

    $> conda create -n myenv python
myenv is the name of your virtualenv. You can use any other name, but stick to lowercase and use no spaces. It is also good idea to keep the name short as you'll be referencing it a lot.

### Using a virtual environment
     $> source activate myenvironment
You will know that you have virtualenv started when you see that the prompt in your console is prefixed with (myvenvironment).

### Installing packages
    $> conda install packagename
    
Example to install jupyter notebook
    
    $> conda install jupyter
    
For more information: https://docs.continuum.io/

### 2. Using the official distribution

### Create virtual environment
To create a virtualenv on both Linux and OS X you need to install virtualenv functionality:

    $> pip install virtualenv
    
And then create the virtual environment

    $> cd my_project_folder
    
    $> virtualenv myvirtualenv

myvirtualenv is the name of your virtualenv. You can use any other name, but stick to lowercase and use no spaces. It is also good idea to keep the name short as you'll be referencing it a lot.

### Using a virtual environment
    $> source myvirtualenv/bin/activate
    
You will know that you have virtualenv started when you see that the prompt in your console is prefixed with (myvirtualenv).

### Installing packages
    $> pip install packagename
    
Example to install jupyter notebook
    
    $> pip install jupyter

## Launching Jupyter Notebook

From the terminal, after activating the virtual environment:

    $> jupyter notebook


## How to learn from this resource?

Download all the jupyter notebooks from this repository https://github.com/atugores/Python-Lectures

Launch jupyter notebook from the folder which contains the notebooks. Open each one of them

    Cell > All Output > Clear
    
This will clear all the outputs and now you can understand each statement and learn interactively.

## License

This work is licensed under the Creative Commons Attribution 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by/3.0/