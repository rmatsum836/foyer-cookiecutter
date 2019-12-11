import os
import glob
from pkg_resource import resource_filename

def get_ff_path():
    return [resource_filename('{{ cookiecutter.project_name }}', 'xml')]

def get_{{ cookiecutter.project_name }}_forcefield_path():
    for dir_path in get_ff_path():
        file_pattern = os.path.join(dir_path, '*.xml')
        file_paths = [file_path for file_path in glob.glob(file_pattern)]
    return file_paths

def get_{{ cookiecutter.project_name }}_forcefield():
    from foyer import Forcefield
    return Forcefield(get_{{ cookiecutter.project_name }}_forcefield_path())


load_{{ cookiecutter.class_name }} = get_{{ cookiecutter.project_name }}_forcefield
