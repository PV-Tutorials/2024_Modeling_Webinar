# OSS Webinar Python Tutorial
Welcome! The goal of this tutorial is to introduce attendees to the following packages:
* PySAM: https://nrel-pysam.readthedocs.io/en/main/
* pvlib-python: https://pvlib-python.readthedocs.io/en/stable/

## Tutorial Setup
These tutorials are made with [Jupyter](https://jupyter.org), which is a
browser based interactive Python notebook.

### Jupyter Books

The tutorial content is also hosted as a [Jupyter book](https://jupyterbook.org/intro.html):

[![Jupyter Book Badge](https://jupyterbook.org/badge.svg)](<https://pv-tutorials.github.io/2024_Modeling_Webinar/>)


### Running Locally

You can run the tutorial locally with
[miniconda](https://docs.conda.io/en/latest/miniconda.html) by following thes
steps:

1. Install [miniconda](https://docs.conda.io/en/latest/miniconda.html).

1. Clone the repository:

   ```
   git clone https://github.com/PV-Tutorials/2024_Analytics_Webinar.git
   ```

1. Create the environment and install the requirements. The repository includes
   a `requirements.txt` file that contains a list the packages needed to run
   this tutorial. The requirements file pins versions to those shown in the demo.
   This ensures you will get the same results as were presented in the webinar, but
   we encourage you to check out the latest versions of all the packages for the most
   up to date functionality. To install them using conda and pip run:

   ```
   conda create --name modeling_demo python==3.10 notebook==6.48
   conda activate modeling_demo
   pip install -r requirements.txt
   ```

1. Start a Jupyter session:

   ```
   jupyter notebook
   ```

1. Use the file explorer in Jupyter lab to browse to `2024_Analytics_Webinar`
   and start the first Tutorial.


### Licensing

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
