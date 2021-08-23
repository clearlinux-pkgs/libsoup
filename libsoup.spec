#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libsoup
Version  : 2.74.0
Release  : 47
URL      : https://download.gnome.org/sources/libsoup/2.74/libsoup-2.74.0.tar.xz
Source0  : https://download.gnome.org/sources/libsoup/2.74/libsoup-2.74.0.tar.xz
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
BuildRequires : curl
BuildRequires : curl-dev32
BuildRequires : e2fsprogs-dev
BuildRequires : e2fsprogs-dev32
BuildRequires : glib-networking
BuildRequires : glib-networking-lib32
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : libpsl-dev32
BuildRequires : libxml2-dev
BuildRequires : libxml2-dev32
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : sqlite-autoconf-dev32
BuildRequires : vala
BuildRequires : vala-dev
BuildRequires : zlib-dev
BuildRequires : zlib-dev32

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
%setup -q -n libsoup-2.74.0
cd %{_builddir}/libsoup-2.74.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1629731680
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain --wrap-mode=nodownload \
-Dgssapi=disabled \
-Dinstalled_tests=true  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libsoup
cp %{_builddir}/libsoup-2.74.0/COPYING %{buildroot}/usr/share/package-licenses/libsoup/ba8966e2473a9969bdcab3dc82274c817cfd98a1
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang libsoup

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Soup-2.4.typelib
/usr/lib64/girepository-1.0/SoupGNOME-2.4.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/libsoup-2.4.deps
/usr/share/vala/vapi/libsoup-2.4.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/libsoup-2.4/libsoup/soup-address.h
/usr/include/libsoup-2.4/libsoup/soup-auth-domain-basic.h
/usr/include/libsoup-2.4/libsoup/soup-auth-domain-digest.h
/usr/include/libsoup-2.4/libsoup/soup-auth-domain.h
/usr/include/libsoup-2.4/libsoup/soup-auth-manager.h
/usr/include/libsoup-2.4/libsoup/soup-auth.h
/usr/include/libsoup-2.4/libsoup/soup-autocleanups.h
/usr/include/libsoup-2.4/libsoup/soup-cache.h
/usr/include/libsoup-2.4/libsoup/soup-content-decoder.h
/usr/include/libsoup-2.4/libsoup/soup-content-sniffer.h
/usr/include/libsoup-2.4/libsoup/soup-cookie-jar-db.h
/usr/include/libsoup-2.4/libsoup/soup-cookie-jar-text.h
/usr/include/libsoup-2.4/libsoup/soup-cookie-jar.h
/usr/include/libsoup-2.4/libsoup/soup-cookie.h
/usr/include/libsoup-2.4/libsoup/soup-date.h
/usr/include/libsoup-2.4/libsoup/soup-enum-types.h
/usr/include/libsoup-2.4/libsoup/soup-form.h
/usr/include/libsoup-2.4/libsoup/soup-headers.h
/usr/include/libsoup-2.4/libsoup/soup-hsts-enforcer-db.h
/usr/include/libsoup-2.4/libsoup/soup-hsts-enforcer.h
/usr/include/libsoup-2.4/libsoup/soup-hsts-policy.h
/usr/include/libsoup-2.4/libsoup/soup-logger.h
/usr/include/libsoup-2.4/libsoup/soup-message-body.h
/usr/include/libsoup-2.4/libsoup/soup-message-headers.h
/usr/include/libsoup-2.4/libsoup/soup-message.h
/usr/include/libsoup-2.4/libsoup/soup-method.h
/usr/include/libsoup-2.4/libsoup/soup-misc.h
/usr/include/libsoup-2.4/libsoup/soup-multipart-input-stream.h
/usr/include/libsoup-2.4/libsoup/soup-multipart.h
/usr/include/libsoup-2.4/libsoup/soup-password-manager.h
/usr/include/libsoup-2.4/libsoup/soup-portability.h
/usr/include/libsoup-2.4/libsoup/soup-proxy-resolver-default.h
/usr/include/libsoup-2.4/libsoup/soup-proxy-resolver.h
/usr/include/libsoup-2.4/libsoup/soup-proxy-uri-resolver.h
/usr/include/libsoup-2.4/libsoup/soup-request-data.h
/usr/include/libsoup-2.4/libsoup/soup-request-file.h
/usr/include/libsoup-2.4/libsoup/soup-request-http.h
/usr/include/libsoup-2.4/libsoup/soup-request.h
/usr/include/libsoup-2.4/libsoup/soup-requester.h
/usr/include/libsoup-2.4/libsoup/soup-server.h
/usr/include/libsoup-2.4/libsoup/soup-session-async.h
/usr/include/libsoup-2.4/libsoup/soup-session-feature.h
/usr/include/libsoup-2.4/libsoup/soup-session-sync.h
/usr/include/libsoup-2.4/libsoup/soup-session.h
/usr/include/libsoup-2.4/libsoup/soup-socket.h
/usr/include/libsoup-2.4/libsoup/soup-status.h
/usr/include/libsoup-2.4/libsoup/soup-tld.h
/usr/include/libsoup-2.4/libsoup/soup-types.h
/usr/include/libsoup-2.4/libsoup/soup-uri.h
/usr/include/libsoup-2.4/libsoup/soup-value-utils.h
/usr/include/libsoup-2.4/libsoup/soup-version.h
/usr/include/libsoup-2.4/libsoup/soup-websocket-connection.h
/usr/include/libsoup-2.4/libsoup/soup-websocket-extension-deflate.h
/usr/include/libsoup-2.4/libsoup/soup-websocket-extension-manager.h
/usr/include/libsoup-2.4/libsoup/soup-websocket-extension.h
/usr/include/libsoup-2.4/libsoup/soup-websocket.h
/usr/include/libsoup-2.4/libsoup/soup-xmlrpc-old.h
/usr/include/libsoup-2.4/libsoup/soup-xmlrpc.h
/usr/include/libsoup-2.4/libsoup/soup.h
/usr/include/libsoup-gnome-2.4/libsoup/soup-cookie-jar-sqlite.h
/usr/include/libsoup-gnome-2.4/libsoup/soup-gnome-features.h
/usr/include/libsoup-gnome-2.4/libsoup/soup-gnome.h
/usr/lib64/libsoup-2.4.so
/usr/lib64/libsoup-gnome-2.4.so
/usr/lib64/pkgconfig/libsoup-2.4.pc
/usr/lib64/pkgconfig/libsoup-gnome-2.4.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsoup-2.4.so.1
/usr/lib64/libsoup-2.4.so.1.11.1
/usr/lib64/libsoup-gnome-2.4.so.1
/usr/lib64/libsoup-gnome-2.4.so.1.11.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libsoup/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files tests
%defattr(-,root,root,-)
/usr/libexec/installed-tests/libsoup-2.4/cache-test
/usr/libexec/installed-tests/libsoup-2.4/chunk-io-test
/usr/libexec/installed-tests/libsoup-2.4/chunk-test
/usr/libexec/installed-tests/libsoup-2.4/coding-test
/usr/libexec/installed-tests/libsoup-2.4/context-test
/usr/libexec/installed-tests/libsoup-2.4/continue-test
/usr/libexec/installed-tests/libsoup-2.4/cookies-test
/usr/libexec/installed-tests/libsoup-2.4/date-test
/usr/libexec/installed-tests/libsoup-2.4/forms-test
/usr/libexec/installed-tests/libsoup-2.4/header-parsing-test
/usr/libexec/installed-tests/libsoup-2.4/hsts-db-test
/usr/libexec/installed-tests/libsoup-2.4/hsts-test
/usr/libexec/installed-tests/libsoup-2.4/index.txt
/usr/libexec/installed-tests/libsoup-2.4/libtest-utils.so
/usr/libexec/installed-tests/libsoup-2.4/misc-test
/usr/libexec/installed-tests/libsoup-2.4/multipart-test
/usr/libexec/installed-tests/libsoup-2.4/no-ssl-test
/usr/libexec/installed-tests/libsoup-2.4/ntlm-test
/usr/libexec/installed-tests/libsoup-2.4/ntlm-test-helper
/usr/libexec/installed-tests/libsoup-2.4/redirect-test
/usr/libexec/installed-tests/libsoup-2.4/requester-test
/usr/libexec/installed-tests/libsoup-2.4/resource-test
/usr/libexec/installed-tests/libsoup-2.4/samesite-test
/usr/libexec/installed-tests/libsoup-2.4/server-auth-test
/usr/libexec/installed-tests/libsoup-2.4/server-test
/usr/libexec/installed-tests/libsoup-2.4/session-test
/usr/libexec/installed-tests/libsoup-2.4/sniffing-test
/usr/libexec/installed-tests/libsoup-2.4/socket-test
/usr/libexec/installed-tests/libsoup-2.4/soup-tests.gresource
/usr/libexec/installed-tests/libsoup-2.4/ssl-test
/usr/libexec/installed-tests/libsoup-2.4/streaming-test
/usr/libexec/installed-tests/libsoup-2.4/test-cert.pem
/usr/libexec/installed-tests/libsoup-2.4/test-key.pem
/usr/libexec/installed-tests/libsoup-2.4/timeout-test
/usr/libexec/installed-tests/libsoup-2.4/tld-test
/usr/libexec/installed-tests/libsoup-2.4/uri-parsing-test
/usr/libexec/installed-tests/libsoup-2.4/websocket-test
/usr/share/installed-tests/libsoup-2.4/cache-test.test
/usr/share/installed-tests/libsoup-2.4/chunk-io-test.test
/usr/share/installed-tests/libsoup-2.4/chunk-test.test
/usr/share/installed-tests/libsoup-2.4/coding-test.test
/usr/share/installed-tests/libsoup-2.4/context-test.test
/usr/share/installed-tests/libsoup-2.4/continue-test.test
/usr/share/installed-tests/libsoup-2.4/cookies-test.test
/usr/share/installed-tests/libsoup-2.4/date-test.test
/usr/share/installed-tests/libsoup-2.4/forms-test.test
/usr/share/installed-tests/libsoup-2.4/header-parsing-test.test
/usr/share/installed-tests/libsoup-2.4/hsts-db-test.test
/usr/share/installed-tests/libsoup-2.4/hsts-test.test
/usr/share/installed-tests/libsoup-2.4/misc-test.test
/usr/share/installed-tests/libsoup-2.4/multipart-test.test
/usr/share/installed-tests/libsoup-2.4/no-ssl-test.test
/usr/share/installed-tests/libsoup-2.4/ntlm-test.test
/usr/share/installed-tests/libsoup-2.4/redirect-test.test
/usr/share/installed-tests/libsoup-2.4/requester-test.test
/usr/share/installed-tests/libsoup-2.4/resource-test.test
/usr/share/installed-tests/libsoup-2.4/samesite-test.test
/usr/share/installed-tests/libsoup-2.4/server-auth-test.test
/usr/share/installed-tests/libsoup-2.4/server-test.test
/usr/share/installed-tests/libsoup-2.4/session-test.test
/usr/share/installed-tests/libsoup-2.4/sniffing-test.test
/usr/share/installed-tests/libsoup-2.4/socket-test.test
/usr/share/installed-tests/libsoup-2.4/ssl-test.test
/usr/share/installed-tests/libsoup-2.4/streaming-test.test
/usr/share/installed-tests/libsoup-2.4/timeout-test.test
/usr/share/installed-tests/libsoup-2.4/tld-test.test
/usr/share/installed-tests/libsoup-2.4/uri-parsing-test.test
/usr/share/installed-tests/libsoup-2.4/websocket-test.test

%files locales -f libsoup.lang
%defattr(-,root,root,-)

