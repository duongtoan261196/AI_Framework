# coding: utf-8

import project
import itertools

## Create Project Manager
projectManager = project.ProjectManager()
## Set up project variables
projectManager.load_yaml('/Users/bguillouet/Insa/TP_Insa/dev/IA-Frameworks/tp_google_cloud/conf.yml')

## Initialize instance
projectManager.set_instance_name('instance-2')
projectManager.instance_init()

## Update data
projectManager.execute_code_ssh("'mkdir " + projectManager.remote_folder+ "'")
projectManager.execute_code_ssh("'mkdir " + projectManager.remote_data+ "'")
projectManager.execute_code_ssh("'mkdir " + projectManager.remote_results+ "'")
projectManager.execute_code_ssh("'mkdir " + projectManager.remote_code+ "'")

#projectManager.update_data("sample_2.zip")

## Update last version of code
projectManager.update_code()


## Start container
projectManager.manage_container("run", "tfimg", "container_background",  docker_dir="/root/CatsVsDogs")


## Execute Job


args = [["epochs", "10"], ["batch_size", "100"]]


projectManager.execute_python_script_container("learning_solution.py", "sample_2", "container_background", args = args)
projectManager.execute_python_script_container("prediction_solution.py", "sample_2", "container_background", args = args)




## stop and remove container
projectManager.manage_container("stop", "tfimg", "container_background", docker_dir ="/root/vm_dir/")
projectManager.manage_container("remove", "tfimg", "container_background", docker_dir ="/root/vm_dir/")


## Collect job output
projectManager.collect_results()

## Finalize instance
projectManager.instance_end()
