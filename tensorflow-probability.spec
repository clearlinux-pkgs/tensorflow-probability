Name     : tensorflow-probability
Version  : 0.7
Release  : 6
URL      : https://github.com/tensorflow/probability/archive/v0.7.tar.gz
Source0  : https://github.com/tensorflow/probability/archive/v0.7.tar.gz
Source1  : https://mirror.bazel.build/github.com/bazelbuild/rules_cc/archive/0d5f3f2768c6ca2faca0079a997a97ce22997a0c.zip


%define __strip /bin/true
%define debug_package %{nil}


Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 GPL-3.0 MPL-2.0-no-copyleft-exception
BuildRequires : pip

BuildRequires : Keras
BuildRequires : Keras_Applications
BuildRequires : Keras_Preprocessing
BuildRequires : bazel
BuildRequires : c-ares-dev
BuildRequires : mkl-dnn-dev
BuildRequires : numpy
BuildRequires : openjdk
BuildRequires : openjdk-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tensorflow
BuildRequires : wheel

Requires : Keras
Requires : Keras_Applications
Requires : Keras_Preprocessing
Requires : Markdown
Requires : Werkzeug
Requires : absl-py
Requires : astor
Requires : backports.weakref
Requires : bleach
Requires : decorator
Requires : gast
Requires : grpcio
Requires : tensorboard
Requires : termcolor


%description
TensorFlow

%prep
%setup -q  -n probability-0.7

#%patch2 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1485959355

InstallCache() {
	sha256=`sha256sum $1 | cut -f1 -d" "`
        mkdir -p /builddir/.cache/bazel/_bazel_mockbuild/cache/repos/v1/content_addressable/sha256/$sha256/
	cp $1 /builddir/.cache/bazel/_bazel_mockbuild/cache/repos/v1/content_addressable/sha256/$sha256/file
}

InstallCache %{SOURCE1}

bazel build --copt=-O3  :pip_pkg
./bazel-bin/pip_pkg  /tmp/probability_pip


%install
export SOURCE_DATE_EPOCH=1485959355


pip3 install --no-deps --force-reinstall --root %{buildroot}  /tmp/probability_pip/tfp_nightly-0.7.0-py2.py3-none-any.whl

%files
%defattr(-,root,root,-)
/usr/lib/python3.7/site-packages/tensorflow_probability*
/usr/lib/python3.7/site-packages/tfp_nightly*
