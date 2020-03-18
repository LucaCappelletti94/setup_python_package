import os
import shutil
import stat
import subprocess
import platform

url = "https://github.com/LucaCappelletti94/setup_python_package_test_reporitory.git"
clone_target = "setup_python_package_test_reporitory"


def clone_test_repo():
    global url, clone_target
    result = subprocess.Popen(
        [
            'git',
            'clone',
            url
        ],
        shell=platform.system()=="Windows"
    )
    result.wait()
    os.chdir(clone_target)


def delete_test_repo():
    global clone_target
    os.chdir("../")
    result = subprocess.Popen(
        [
            'rm',
            '-fdr',
            clone_target
        ],
        shell=True
    )
    result.wait()