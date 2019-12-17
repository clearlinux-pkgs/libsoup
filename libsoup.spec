#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libsoup
Version  : 2.68.3
Release  : 41
URL      : https://download.gnome.org/sources/libsoup/2.68/libsoup-2.68.3.tar.xz
Source0  : https://download.gnome.org/sources/libsoup/2.68/libsoup-2.68.3.tar.xz
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
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glib-networking
BuildRequires : glib-networking-lib32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
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


%package dev32
Summary: dev32 components for the libsoup package.
Group: Default
Requires: libsoup-lib32 = %{version}-%{release}
Requires: libsoup-data = %{version}-%{release}
Requires: libsoup-dev = %{version}-%{release}

%description dev32
dev32 components for the libsoup package.


%package lib
Summary: lib components for the libsoup package.
Group: Libraries
Requires: libsoup-data = %{version}-%{release}
Requires: libsoup-license = %{version}-%{release}

%description lib
lib components for the libsoup package.


%package lib32
Summary: lib32 components for the libsoup package.
Group: Default
Requires: libsoup-data = %{version}-%{release}
Requires: libsoup-license = %{version}-%{release}

%description lib32
lib32 components for the libsoup package.


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


%prep
%setup -q -n libsoup-2.68.3
cd %{_builddir}/libsoup-2.68.3
pushd ..
cp -a libsoup-2.68.3 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576618139
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dgssapi=disabled  builddir
ninja -v -C builddir
pushd ../build32
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
meson --libdir=lib32 --prefix=/usr --buildtype=plain -Dgssapi=disabled  builddir
ninja -v -C builddir
popd

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libsoup
cp %{_builddir}/libsoup-2.68.3/COPYING %{buildroot}/usr/share/package-licenses/libsoup/ba8966e2473a9969bdcab3dc82274c817cfd98a1
pushd ../build32
DESTDIR=%{buildroot} ninja -C builddir install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang libsoup

%files
%defattr(-,root,root,-)
/usr/lib32/girepository-1.0/Soup-2.4.typelib
/usr/lib32/girepository-1.0/SoupGNOME-2.4.typelib

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

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libsoup-2.4.so
/usr/lib32/libsoup-gnome-2.4.so
/usr/lib32/pkgconfig/32libsoup-2.4.pc
/usr/lib32/pkgconfig/32libsoup-gnome-2.4.pc
/usr/lib32/pkgconfig/libsoup-2.4.pc
/usr/lib32/pkgconfig/libsoup-gnome-2.4.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsoup-2.4.so.1
/usr/lib64/libsoup-2.4.so.1.8.0
/usr/lib64/libsoup-gnome-2.4.so.1
/usr/lib64/libsoup-gnome-2.4.so.1.8.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libsoup-2.4.so.1
/usr/lib32/libsoup-2.4.so.1.8.0
/usr/lib32/libsoup-gnome-2.4.so.1
/usr/lib32/libsoup-gnome-2.4.so.1.8.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libsoup/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files locales -f libsoup.lang
%defattr(-,root,root,-)

