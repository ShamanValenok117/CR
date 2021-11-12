# python code

import os

#checking ipython and kaggle in installed apps
from pip._internal.utils.misc import get_installed_distributions

installed = [i.project_name for i in get_installed_distributions()]

if 'ipython' not in installed: 
    os.system('pip install ipython')

if 'kaggle' not in installed: 
    os.system('pip install kaggle')
    
#execute ipython code
os.system('ipython load_data.ipy')

