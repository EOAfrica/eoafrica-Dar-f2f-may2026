# Additional course materials for the face 2 face course **Face-to-Face course on Modern Tools for River Monitoring**

see [also the announcement site](https://www.eoafrica-rd.org/space-academy/face-to-face-courses-rdf2/face-to-face-course-on-modern-tools-for-river-monitoring/)


## A: Getting started on the Innovation Lab

### Step A1: Login to the EOAfrica Innovation Lab 

### Step A2: clone this repository in your home folder, and link the data directory

Either execute from a terminal (File-> New -> Terminal):
1. `cd` without arguments to nativaget to your home
and then
2. `git clone https://github.com/EOAfrica/eoafrica-Dar-f2f-may2026.git`
3. `cd eoafrica-Dar-f2f-may2026` (Change in your cloned directory)
4. `ln -s /home/eoafrica/resources/F2FDar26/wbalance_assignment_data data` (creates a symbolic link to the shared resources folder, avoiding a copy)

or use the left panel to navigate to your home directory and click on the 'git' symbol to *Clone a Repository* using the https link from above. You need to also perform step *3.* and *4.* from a terminal.

## B setup a conda environment with the necessary tools
In a terminal
1. `cd` (navigate to your home directory, if your not there already)
2. `conda create -n pywater python` (create a new conda environment) 
3. `conda activate pywater` conda activate the environment
4. `conda install ipykernel` Install the ipykernel needed for using in Jupyeter notebooks  
5. `pip install shxarray` install [shxarray](https://github.com/ITC-Water-Resources/shxarray)
6. `python -m ipykernel install --user --name myenv --display-name "pywater"` (Install the ipython kernel so you can use it in your notebooks)
    
## C Alternative to B: use the prepared Conda environment in the Innovation Lab
1. `conda activate /home/eoafrica/resources/F2FDar26/pywater` (Activate the environment)
2. Run step 6 from *B* to install the conda IPython kernel for your Jupyter notebooks 

## D Getting started with the exercises
You should now be able to use the tools from the conda environment from your notebook. And start with the exercises from the `practicals` folder in your cloned repositories. These files are copies under your control and you change them to your liking.








