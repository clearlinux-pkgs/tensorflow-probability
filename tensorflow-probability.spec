Name     : tensorflow-probability
Version  : 0.11.1
Release  : 14
URL      : https://github.com/tensorflow/probability/archive/v0.11.1/tensorflow-probability-0.11.1.tar.gz
Source0  : https://github.com/tensorflow/probability/archive/v0.11.1/tensorflow-probability-0.11.1.tar.gz
Summary  : Probabilistic reasoning and statistical analysis in TensorFlow
Group    : Development/Tools
License  : Apache-2.0 GPL-3.0 MPL-2.0-no-copyleft-exception
Requires : cloudpickle
Requires : decorator
Requires : dm-tree
Requires : gast
Requires : numpy
Requires : six
BuildRequires : Keras
BuildRequires : Keras_Applications
BuildRequires : Keras_Preprocessing
BuildRequires : bazel
BuildRequires : c-ares-dev
BuildRequires : mkl-dnn-dev
BuildRequires : numpy
BuildRequires : openjdk
BuildRequires : openjdk-dev
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tensorflow
BuildRequires : wheel

%define __strip /bin/true
%define debug_package %{nil}

# SOURCES BEGIN
Source10: https://mirror.bazel.build/github.com/bazelbuild/rules_cc/archive/8bd6cd75d03c01bb82561a96d9c1f9f7157b13d0.zip
Source11: https://mirror.bazel.build/github.com/bazelbuild/rules_java/archive/7cf3cefd652008d0a64a419c34c13bdca6c8f178.zip
# SOURCES END

%description
TensorFlow Probability is a library for probabilistic reasoning and statistical
analysis in TensorFlow. As part of the TensorFlow ecosystem, TensorFlow
Probability provides integration of probabilistic methods with deep networks,
gradient-based inference via automatic differentiation, and scalability to
large datasets and models via hardware acceleration (e.g., GPUs) and
distributed computation.

%prep
%setup -q -n probability-%{version}

InstallCacheBazel() {
  sha256=$(sha256sum $1 | cut -f1 -d" ")
  mkdir -p /var/tmp/cache/content_addressable/sha256/$sha256
  cp $1 /var/tmp/cache/content_addressable/sha256/$sha256/file
}

# CACHE BAZEL BEGIN
InstallCacheBazel %{SOURCE10}
InstallCacheBazel %{SOURCE11}
# CACHE BAZEL END

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1485959355
export GCC_IGNORE_WERROR=1

bazel build \
  --repository_cache=/var/tmp/cache \
  --copt=-O3 \
  --verbose_failures \
  //:pip_pkg

./bazel-bin/pip_pkg /var/tmp/probability_pip --release

%install
export SOURCE_DATE_EPOCH=1485959355
rm -rf %{buildroot}
pip3 install \
  --no-deps \
  --force-reinstall \
  --ignore-installed \
  --root %{buildroot} \
  /var/tmp/probability_pip/tensorflow_probability-%{version}-py2.py3-none-any.whl

%files
%defattr(-,root,root,-)
/usr/lib/python3*/site-packages/tensorflow_probability*
