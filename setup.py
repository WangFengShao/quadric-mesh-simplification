from setuptools import Extension, setup
from Cython.Build import cythonize
import numpy as np

__version__ = '0.0.1'

url = 'https://github.com/jannessm/quadric-mesh-simplification'

files = [
	('pair', 'quad_mesh_simplify/pair.pyx'),
	('q', 'quad_mesh_simplify/q.pyx'),
	('simplify', 'quad_mesh_simplify/simplify.pyx'),
	('utils', 'quad_mesh_simplify/utils.pyx'),
]

ext_modules = [
	Extension(
		f[0],
		[f[1]],
        extra_compile_args=['-fopenmp'],
        extra_link_args=['-fopenmp'],
        include_dirs=[np.get_include()]
	)
	for f in files
]

setup(
  name='quad_mesh_simplify',
  version=__version__,
  author='Jannes Magnusson',
  url=url,
  ext_modules = cythonize(ext_modules)
)