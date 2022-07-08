"""
    Setup.py to build .exe file with ex_freeze.
"""

import os
import sys
import shutil

from os.path import isfile
from cx_Freeze import setup, Executable

from os import listdir
from os.path import join, exists


BASE = 'Console'
WORK_DIR = sys.path[0]
FILES_TO_INCLUDE = [
    'configs.json',
    'ChromeSetup.exe',
    'chromedriver.exe',
    'README.md',
]
BASE_SCRIPT_NAME = [
    x for x in listdir(
        WORK_DIR
    ) if not 'setup' in x and '.py' in x
][0]
BUILD_DIR = join(WORK_DIR, BASE_SCRIPT_NAME.replace('.py', ''))
FINAL_BUILD_ZIP = join(WORK_DIR, BASE_SCRIPT_NAME.replace('.py', '.zip'))


if sys.platform == 'win32':
    WINDOWS_DLL_LIBS = [
        'C:\\Windows\\SysWOW64\\vcruntime140.dll']
    for DLL_LIB in WINDOWS_DLL_LIBS:
        FILES_TO_INCLUDE.append(DLL_LIB)
    if BASE != 'Console':
        BASE = 'Win32GUI'

build_exe_options = {
    'build_exe': BUILD_DIR,
    'packages': ['os'],
    'include_files': FILES_TO_INCLUDE,
    'bin_includes': [
        join(x, WORK_DIR) for x in os.listdir(join(WORK_DIR, 'lib')) if x.endswith('.py')
    ]
}

setup(
    name=BASE_SCRIPT_NAME.replace('.py', ''),
    version='0.1',
    description=f'{BASE_SCRIPT_NAME} app',
    options={'build_exe': build_exe_options},
    executables=[
        Executable(
            BASE_SCRIPT_NAME,
            base=BASE,
            icon=join(WORK_DIR, 'qc.ico')
        )
    ],
)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

if exists(BUILD_DIR):
    print("BUILD_DIR, encontrado!")
    if isfile(FINAL_BUILD_ZIP):
        os.remove(FINAL_BUILD_ZIP)
        print(".zip antigo deletado!")

    shutil.make_archive(FINAL_BUILD_ZIP.replace(".zip", ""), 'zip', BUILD_DIR)
    print("Arquivo .zip gerado com sucesso!")

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
