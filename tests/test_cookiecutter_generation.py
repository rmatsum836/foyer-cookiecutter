import os
import re
import pytest

PATTERN = r"{{(\s?cookiecutter)[.](.*?)}}"
RE_OBJ = re.compile(PATTERN)


@pytest.fixture
def context():
    return {
    "project_name": "test_ff",
    "directory_name": "organics",
    "first_module_name": "organics",
    "xml_name": "ORG",
    "DOI": "Made up DOI",
    "author_name": "Mike Vrabel",
    "author_email": "boomer@hotmail.com",
    "description": "A short description of the project.",
    "open_source_license": "MIT"
    }


def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files."""
    return [
        os.path.join(dirpath, file_path)
        for dirpath, subdirs, files in os.walk(root_dir)
        for file_path in files
    ]


def test_project_generation(cookies, context):
    """
    Test that project is generated and fully rendered.
    """
    result = cookies.bake(extra_context={**context})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'foyer_' + context['project_name']
    assert result.project.isdir()

    paths = build_files_list(str(result.project))
    assert paths
