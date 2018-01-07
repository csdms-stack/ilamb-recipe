"""Test ILAMB"""
import os
import subprocess


os.environ['MPLBACKEND'] = 'Agg'
import ILAMB


r = subprocess.check_output(['ilamb-run', '--help'])
print r
