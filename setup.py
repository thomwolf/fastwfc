from skbuild import setup

REQUIRED_PKGS = [
    "numpy>=1.18",  # We use numpy>=1.17 to have np.random.Generator
    'scikit-build',  # For compiling extensions pybind11
]

TESTS_REQUIRE = [
    "pytest"
]

QUALITY_REQUIRE = ["black[jupyter]~=22.0", "flake8>=3.8.3", "isort>=5.0.0", "pyyaml>=5.3.1"]

EXTRAS_REQUIRE = {
    "test": TESTS_REQUIRE,
    "quality": QUALITY_REQUIRE,
}


setup(
    name="fastwfc",
    version="0.1.0",
    author='Thomas Wolf and Mathieu Fehr and Nathanaël Courant',
    author_email='thomas@huggingface.co',
    url='https://github.com/thomwolf/fastwfc',
    description='Python bindings for Fast-wfc',
    long_description='Python bindings for Fast-wfc',
    install_requires=REQUIRED_PKGS,
    extras_require=EXTRAS_REQUIRE,
    packages=['fastwfc'],
    package_dir={'': 'src'},
    cmake_install_dir='src/fastwfc')

# When building extension modules `cmake_install_dir` should always be set to the
# location of the package you are building extension modules for.
# Specifying the installation directory in the CMakeLists subtley breaks the relative
# paths in the helloTargets.cmake file to all of the library components.
