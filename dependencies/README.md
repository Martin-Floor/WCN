To install dependencies, create a new conda environment from the wcn_environment.yml file in this repository as follows:

conda env create -f wcn_environment.yml

After this you need to activate the wcn environment:

conda activate wcn

Finally, install the WCN library from the library's root direcetory (i.e., where the setup.py script is located)

python setup.py install
