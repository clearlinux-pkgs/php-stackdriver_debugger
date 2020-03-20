#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-stackdriver_debugger
Version  : 0.2.0
Release  : 5
URL      : https://pecl.php.net//get/stackdriver_debugger-0.2.0.tgz
Source0  : https://pecl.php.net//get/stackdriver_debugger-0.2.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: php-stackdriver_debugger-lib = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : pcre2-dev

%description
# Stackdriver Debugger PHP Extension [![CircleCI](https://circleci.com/gh/GoogleCloudPlatform/stackdriver-debugger-php-extension.svg?style=svg)](https://circleci.com/gh/GoogleCloudPlatform/stackdriver-debugger-php-extension)

%package lib
Summary: lib components for the php-stackdriver_debugger package.
Group: Libraries

%description lib
lib components for the php-stackdriver_debugger package.


%prep
%setup -q -n stackdriver_debugger-0.2.0
cd %{_builddir}/stackdriver_debugger-0.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20190902/stackdriver_debugger.so
