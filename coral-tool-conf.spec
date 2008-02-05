### RPM cms coral-tool-conf CMS_152a
%if "%{?use_system_gcc:set}" != "set"
Requires: gcc-toolfile
Requires: gmake
%endif

%if "%{?online_release:set}" != "set"
Requires: zlib
Requires: expat
Requires: openssl
Requires: db4
Requires: gdbm
Requires: qt
Requires: castor
Requires: mysql
Requires: libpng
Requires: libjpg
Requires: dcap
Requires: oracle
Requires: oracle-env
Requires: p5-dbd-oracle
Requires: libungif
Requires: libtiff
Requires: xerces-c
Requires: cppunit
Requires: systemtools
%else
Requires: onlinesystemtools
%define onlinesystemtoolsroot ${ONLINESYSTEMTOOLS_ROOT}
%endif

Requires: python
Requires: pcre
Requires: bz2lib
Requires: uuid
Requires: gccxml
Requires: boost
Requires: gsl
Requires: clhep
Requires: root
Requires: frontier_client
Requires: sqlite
Requires: seal

%define skipreqtools %{nil}
%define skipreqtools jcompiler

## IMPORT scramv1-tool-conf
