Name     : tensorflow-probability
Version  : 0.6.0
Release  : 3
URL      : https://github.com/tensorflow/probability/archive/v0.6.0.tar.gz
Source0  : https://github.com/tensorflow/probability/archive/v0.6.0.tar.gz



%define __strip /bin/true
%define debug_package %{nil}


#Source104: 0001-enum34-is-only-required-for-Python-3.4.patch

Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 GPL-3.0 MPL-2.0-no-copyleft-exception
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : wheel
BuildRequires : openjdk
BuildRequires : openjdk-dev
BuildRequires : numpy
#BuildRequires : six
#BuildRequires : protobuf
#BuildRequires : protobuf-c
BuildRequires : bazel
BuildRequires : Keras
BuildRequires : Keras_Applications
BuildRequires : Keras_Preprocessing
BuildRequires : mkl-dnn-dev
BuildRequires : c-ares-dev
BuildRequires : tensorflow




Requires: Werkzeug
Requires: Markdown
Requires: bleach
Requires: backports.weakref
Requires: tensorboard
Requires: absl-py
Requires: astor
Requires: grpcio
Requires: gast
Requires : Keras
Requires : Keras_Applications
Requires : Keras_Preprocessing
Requires : termcolor


%description
TensorFlow

%prep
%setup -q  -n probability-0.6.0

#%patch2 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1485959355

InstallCache() {
	sha256=`sha256sum $1 | cut -f1 -d" "`
	mkdir -p /tmp/cache/content_addressable/sha256/$sha256/
	cp $1 /tmp/cache/content_addressable/sha256/$sha256/file
}

bazel build --copt=-O3  :pip_pkg
./bazel-bin/pip_pkg  /tmp/probability_pip


%install
export SOURCE_DATE_EPOCH=1485959355


pip3 install --no-deps --force-reinstall --root %{buildroot}  /tmp/probability_pip/tfp_nightly-0.6.20190304-py2.py3-none-any.whl

%files
%defattr(-,root,root,-)
/usr/lib/python3.7/site-packages/tensorflow_probability*
/usr/lib/python3.7/site-packages/tfp_nightly*