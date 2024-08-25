#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v18
# autospec commit: f35655a
#
Name     : libsoup
Version  : 3.6.0
Release  : 81
URL      : https://download.gnome.org/sources/libsoup/3.6/libsoup-3.6.0.tar.xz
Source0  : https://download.gnome.org/sources/libsoup/3.6/libsoup-3.6.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.0
Requires: libsoup-data = %{version}-%{release}
Requires: libsoup-lib = %{version}-%{release}
Requires: libsoup-license = %{version}-%{release}
Requires: libsoup-locales = %{version}-%{release}
Requires: glib-networking
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : curl-dev32
BuildRequires : e2fsprogs-dev
BuildRequires : e2fsprogs-dev32
BuildRequires : glib-networking
BuildRequires : glib-networking-lib32
BuildRequires : gnutls-dev
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : libpsl-dev32
BuildRequires : libxml2-dev
BuildRequires : libxml2-dev32
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gnutls)
BuildRequires : sqlite-autoconf-dev32
BuildRequires : vala
BuildRequires : vala-dev
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
libsoup is an HTTP client/server library for GNOME. It uses GObjects
and the glib main loop, to integrate well with GNOME applications.

%package data
Summary: data components for the libsoup package.
Group: Data

%description data
data components for the libsoup package.


%package dev
Summary: dev components for the libsoup package.
Group: Development
Requires: libsoup-lib = %{version}-%{release}
Requires: libsoup-data = %{version}-%{release}
Provides: libsoup-devel = %{version}-%{release}
Requires: libsoup = %{version}-%{release}

%description dev
dev components for the libsoup package.


%package lib
Summary: lib components for the libsoup package.
Group: Libraries
Requires: libsoup-data = %{version}-%{release}
Requires: libsoup-license = %{version}-%{release}

%description lib
lib components for the libsoup package.


%package license
Summary: license components for the libsoup package.
Group: Default

%description license
license components for the libsoup package.


%package locales
Summary: locales components for the libsoup package.
Group: Default

%description locales
locales components for the libsoup package.


%package tests
Summary: tests components for the libsoup package.
Group: Default
Requires: libsoup = %{version}-%{release}
Requires: curl

%description tests
tests components for the libsoup package.


%prep
%setup -q -n libsoup-3.6.0
cd %{_builddir}/libsoup-3.6.0
pushd ..
cp -a libsoup-3.6.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724626265
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain --wrap-mode=nodownload \
-Dgssapi=disabled \
-Dinstalled_tests=true \
-Ddocs=disabled  builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain --wrap-mode=nodownload \
-Dgssapi=disabled \
-Dinstalled_tests=true \
-Ddocs=disabled  builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/libsoup
cp %{_builddir}/libsoup-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libsoup/ba8966e2473a9969bdcab3dc82274c817cfd98a1 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang libsoup-3.0
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Soup-3.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/libsoup-3.0.deps
/usr/share/vala/vapi/libsoup-3.0.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/libsoup-3.0/libsoup/soup-auth-domain-basic.h
/usr/include/libsoup-3.0/libsoup/soup-auth-domain-digest.h
/usr/include/libsoup-3.0/libsoup/soup-auth-domain.h
/usr/include/libsoup-3.0/libsoup/soup-auth-manager.h
/usr/include/libsoup-3.0/libsoup/soup-auth.h
/usr/include/libsoup-3.0/libsoup/soup-cache.h
/usr/include/libsoup-3.0/libsoup/soup-content-decoder.h
/usr/include/libsoup-3.0/libsoup/soup-content-sniffer.h
/usr/include/libsoup-3.0/libsoup/soup-cookie-jar-db.h
/usr/include/libsoup-3.0/libsoup/soup-cookie-jar-text.h
/usr/include/libsoup-3.0/libsoup/soup-cookie-jar.h
/usr/include/libsoup-3.0/libsoup/soup-cookie.h
/usr/include/libsoup-3.0/libsoup/soup-date-utils.h
/usr/include/libsoup-3.0/libsoup/soup-enum-types.h
/usr/include/libsoup-3.0/libsoup/soup-form.h
/usr/include/libsoup-3.0/libsoup/soup-headers.h
/usr/include/libsoup-3.0/libsoup/soup-hsts-enforcer-db.h
/usr/include/libsoup-3.0/libsoup/soup-hsts-enforcer.h
/usr/include/libsoup-3.0/libsoup/soup-hsts-policy.h
/usr/include/libsoup-3.0/libsoup/soup-logger.h
/usr/include/libsoup-3.0/libsoup/soup-message-body.h
/usr/include/libsoup-3.0/libsoup/soup-message-headers.h
/usr/include/libsoup-3.0/libsoup/soup-message-metrics.h
/usr/include/libsoup-3.0/libsoup/soup-message.h
/usr/include/libsoup-3.0/libsoup/soup-method.h
/usr/include/libsoup-3.0/libsoup/soup-multipart-input-stream.h
/usr/include/libsoup-3.0/libsoup/soup-multipart.h
/usr/include/libsoup-3.0/libsoup/soup-server-message.h
/usr/include/libsoup-3.0/libsoup/soup-server.h
/usr/include/libsoup-3.0/libsoup/soup-session-feature.h
/usr/include/libsoup-3.0/libsoup/soup-session.h
/usr/include/libsoup-3.0/libsoup/soup-status.h
/usr/include/libsoup-3.0/libsoup/soup-tld.h
/usr/include/libsoup-3.0/libsoup/soup-types.h
/usr/include/libsoup-3.0/libsoup/soup-uri-utils.h
/usr/include/libsoup-3.0/libsoup/soup-version.h
/usr/include/libsoup-3.0/libsoup/soup-websocket-connection.h
/usr/include/libsoup-3.0/libsoup/soup-websocket-extension-deflate.h
/usr/include/libsoup-3.0/libsoup/soup-websocket-extension-manager.h
/usr/include/libsoup-3.0/libsoup/soup-websocket-extension.h
/usr/include/libsoup-3.0/libsoup/soup-websocket.h
/usr/include/libsoup-3.0/libsoup/soup.h
/usr/lib64/libsoup-3.0.so
/usr/lib64/pkgconfig/libsoup-3.0.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libsoup-3.0.so.0.7.1
/usr/lib64/libsoup-3.0.so.0
/usr/lib64/libsoup-3.0.so.0.7.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libsoup/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files tests
%defattr(-,root,root,-)
/V3/usr/libexec/installed-tests/libsoup-3.0/brotli-decompressor-test
/V3/usr/libexec/installed-tests/libsoup-3.0/cache-test
/V3/usr/libexec/installed-tests/libsoup-3.0/chunk-io-test
/V3/usr/libexec/installed-tests/libsoup-3.0/coding-test
/V3/usr/libexec/installed-tests/libsoup-3.0/context-test
/V3/usr/libexec/installed-tests/libsoup-3.0/continue-test
/V3/usr/libexec/installed-tests/libsoup-3.0/cookies-test
/V3/usr/libexec/installed-tests/libsoup-3.0/date-test
/V3/usr/libexec/installed-tests/libsoup-3.0/forms-test
/V3/usr/libexec/installed-tests/libsoup-3.0/header-parsing-test
/V3/usr/libexec/installed-tests/libsoup-3.0/hsts-db-test
/V3/usr/libexec/installed-tests/libsoup-3.0/hsts-test
/V3/usr/libexec/installed-tests/libsoup-3.0/http2-body-stream-test
/V3/usr/libexec/installed-tests/libsoup-3.0/http2-test
/V3/usr/libexec/installed-tests/libsoup-3.0/libtest-utils.so
/V3/usr/libexec/installed-tests/libsoup-3.0/logger-test
/V3/usr/libexec/installed-tests/libsoup-3.0/misc-test
/V3/usr/libexec/installed-tests/libsoup-3.0/mock-pkcs11.so
/V3/usr/libexec/installed-tests/libsoup-3.0/multipart-test
/V3/usr/libexec/installed-tests/libsoup-3.0/multithread-test
/V3/usr/libexec/installed-tests/libsoup-3.0/no-ssl-test
/V3/usr/libexec/installed-tests/libsoup-3.0/ntlm-test
/V3/usr/libexec/installed-tests/libsoup-3.0/ntlm-test-helper
/V3/usr/libexec/installed-tests/libsoup-3.0/redirect-test
/V3/usr/libexec/installed-tests/libsoup-3.0/request-body-test
/V3/usr/libexec/installed-tests/libsoup-3.0/samesite-test
/V3/usr/libexec/installed-tests/libsoup-3.0/server-auth-test
/V3/usr/libexec/installed-tests/libsoup-3.0/server-test
/V3/usr/libexec/installed-tests/libsoup-3.0/session-test
/V3/usr/libexec/installed-tests/libsoup-3.0/sniffing-test
/V3/usr/libexec/installed-tests/libsoup-3.0/ssl-test
/V3/usr/libexec/installed-tests/libsoup-3.0/streaming-test
/V3/usr/libexec/installed-tests/libsoup-3.0/timeout-test
/V3/usr/libexec/installed-tests/libsoup-3.0/tld-test
/V3/usr/libexec/installed-tests/libsoup-3.0/unix-socket-test
/V3/usr/libexec/installed-tests/libsoup-3.0/uri-parsing-test
/V3/usr/libexec/installed-tests/libsoup-3.0/websocket-test
/V3/usr/libexec/installed-tests/libsoup-3.0/ws-test-helper
/usr/libexec/installed-tests/libsoup-3.0/brotli-data/compressed.br
/usr/libexec/installed-tests/libsoup-3.0/brotli-data/corrupt.br
/usr/libexec/installed-tests/libsoup-3.0/brotli-data/uncompressed.txt
/usr/libexec/installed-tests/libsoup-3.0/brotli-decompressor-test
/usr/libexec/installed-tests/libsoup-3.0/cache-test
/usr/libexec/installed-tests/libsoup-3.0/chunk-io-test
/usr/libexec/installed-tests/libsoup-3.0/coding-test
/usr/libexec/installed-tests/libsoup-3.0/context-test
/usr/libexec/installed-tests/libsoup-3.0/continue-test
/usr/libexec/installed-tests/libsoup-3.0/cookies-test
/usr/libexec/installed-tests/libsoup-3.0/date-test
/usr/libexec/installed-tests/libsoup-3.0/forms-test
/usr/libexec/installed-tests/libsoup-3.0/header-parsing-test
/usr/libexec/installed-tests/libsoup-3.0/hsts-db-test
/usr/libexec/installed-tests/libsoup-3.0/hsts-test
/usr/libexec/installed-tests/libsoup-3.0/http2-body-stream-test
/usr/libexec/installed-tests/libsoup-3.0/http2-test
/usr/libexec/installed-tests/libsoup-3.0/index.txt
/usr/libexec/installed-tests/libsoup-3.0/libtest-utils.so
/usr/libexec/installed-tests/libsoup-3.0/logger-test
/usr/libexec/installed-tests/libsoup-3.0/misc-test
/usr/libexec/installed-tests/libsoup-3.0/mock-pkcs11.so
/usr/libexec/installed-tests/libsoup-3.0/multipart-test
/usr/libexec/installed-tests/libsoup-3.0/multithread-test
/usr/libexec/installed-tests/libsoup-3.0/no-ssl-test
/usr/libexec/installed-tests/libsoup-3.0/ntlm-test
/usr/libexec/installed-tests/libsoup-3.0/ntlm-test-helper
/usr/libexec/installed-tests/libsoup-3.0/redirect-test
/usr/libexec/installed-tests/libsoup-3.0/request-body-test
/usr/libexec/installed-tests/libsoup-3.0/samesite-test
/usr/libexec/installed-tests/libsoup-3.0/server-auth-test
/usr/libexec/installed-tests/libsoup-3.0/server-test
/usr/libexec/installed-tests/libsoup-3.0/session-test
/usr/libexec/installed-tests/libsoup-3.0/sniffing-test
/usr/libexec/installed-tests/libsoup-3.0/soup-tests.gresource
/usr/libexec/installed-tests/libsoup-3.0/ssl-test
/usr/libexec/installed-tests/libsoup-3.0/streaming-test
/usr/libexec/installed-tests/libsoup-3.0/test-cert-2.pem
/usr/libexec/installed-tests/libsoup-3.0/test-cert.pem
/usr/libexec/installed-tests/libsoup-3.0/test-key-2.pem
/usr/libexec/installed-tests/libsoup-3.0/test-key.pem
/usr/libexec/installed-tests/libsoup-3.0/timeout-test
/usr/libexec/installed-tests/libsoup-3.0/tld-test
/usr/libexec/installed-tests/libsoup-3.0/unix-socket-test
/usr/libexec/installed-tests/libsoup-3.0/uri-parsing-test
/usr/libexec/installed-tests/libsoup-3.0/websocket-test
/usr/libexec/installed-tests/libsoup-3.0/ws-test-helper
/usr/share/installed-tests/libsoup-3.0/brotli-decompressor-test.test
/usr/share/installed-tests/libsoup-3.0/cache-test.test
/usr/share/installed-tests/libsoup-3.0/chunk-io-test.test
/usr/share/installed-tests/libsoup-3.0/coding-test.test
/usr/share/installed-tests/libsoup-3.0/context-test.test
/usr/share/installed-tests/libsoup-3.0/continue-test.test
/usr/share/installed-tests/libsoup-3.0/cookies-test.test
/usr/share/installed-tests/libsoup-3.0/date-test.test
/usr/share/installed-tests/libsoup-3.0/forms-test.test
/usr/share/installed-tests/libsoup-3.0/header-parsing-test.test
/usr/share/installed-tests/libsoup-3.0/hsts-db-test.test
/usr/share/installed-tests/libsoup-3.0/hsts-test.test
/usr/share/installed-tests/libsoup-3.0/http2-body-stream-test.test
/usr/share/installed-tests/libsoup-3.0/http2-test.test
/usr/share/installed-tests/libsoup-3.0/logger-test.test
/usr/share/installed-tests/libsoup-3.0/misc-test.test
/usr/share/installed-tests/libsoup-3.0/multipart-test.test
/usr/share/installed-tests/libsoup-3.0/multithread-test.test
/usr/share/installed-tests/libsoup-3.0/no-ssl-test.test
/usr/share/installed-tests/libsoup-3.0/ntlm-test.test
/usr/share/installed-tests/libsoup-3.0/redirect-test.test
/usr/share/installed-tests/libsoup-3.0/request-body-test.test
/usr/share/installed-tests/libsoup-3.0/samesite-test.test
/usr/share/installed-tests/libsoup-3.0/server-auth-test.test
/usr/share/installed-tests/libsoup-3.0/server-test.test
/usr/share/installed-tests/libsoup-3.0/session-test.test
/usr/share/installed-tests/libsoup-3.0/sniffing-test.test
/usr/share/installed-tests/libsoup-3.0/ssl-test.test
/usr/share/installed-tests/libsoup-3.0/streaming-test.test
/usr/share/installed-tests/libsoup-3.0/timeout-test.test
/usr/share/installed-tests/libsoup-3.0/tld-test.test
/usr/share/installed-tests/libsoup-3.0/unix-socket-test.test
/usr/share/installed-tests/libsoup-3.0/uri-parsing-test.test
/usr/share/installed-tests/libsoup-3.0/websocket-test.test

%files locales -f libsoup-3.0.lang
%defattr(-,root,root,-)

