#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libsoup
Version  : 2.62.2
Release  : 26
URL      : https://download.gnome.org/sources/libsoup/2.62/libsoup-2.62.2.tar.xz
Source0  : https://download.gnome.org/sources/libsoup/2.62/libsoup-2.62.2.tar.xz
Summary  : a glib-based HTTP library
Group    : Development/Tools
License  : LGPL-2.0
Requires: libsoup-data
Requires: libsoup-lib
Requires: libsoup-doc
Requires: libsoup-locales
BuildRequires : curl-dev32
BuildRequires : docbook-xml
BuildRequires : e2fsprogs-dev
BuildRequires : e2fsprogs-dev32
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gettext
BuildRequires : glib-networking
BuildRequires : glib-networking-lib32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(32libxml-2.0)
BuildRequires : pkgconfig(32sqlite3)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(sqlite3)

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
Requires: libsoup-lib
Requires: libsoup-data
Provides: libsoup-devel

%description dev
dev components for the libsoup package.


%package dev32
Summary: dev32 components for the libsoup package.
Group: Default
Requires: libsoup-lib32
Requires: libsoup-data
Requires: libsoup-dev

%description dev32
dev32 components for the libsoup package.


%package doc
Summary: doc components for the libsoup package.
Group: Documentation

%description doc
doc components for the libsoup package.


%package lib
Summary: lib components for the libsoup package.
Group: Libraries
Requires: libsoup-data

%description lib
lib components for the libsoup package.


%package lib32
Summary: lib32 components for the libsoup package.
Group: Default
Requires: libsoup-data

%description lib32
lib32 components for the libsoup package.


%package locales
Summary: locales components for the libsoup package.
Group: Default

%description locales
locales components for the libsoup package.


%prep
%setup -q -n libsoup-2.62.2
pushd ..
cp -a libsoup-2.62.2 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1525703985
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%configure --disable-static --enable-introspection --disable-vala --without-gssapi
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static --enable-introspection --disable-vala --without-gssapi   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%install
export SOURCE_DATE_EPOCH=1525703985
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
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

%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/libsoup-2.4/SoupAddress.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupAuth.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupAuthDomain.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupAuthDomainBasic.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupAuthDomainDigest.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupAuthManager.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupCache.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupContentDecoder.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupContentSniffer.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupCookie.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupCookieJar.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupCookieJarDB.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupCookieJarText.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupLogger.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupMessage.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupMessageBody.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupMessageHeaders.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupMultipart.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupMultipartInputStream.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupProxyResolverDefault.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupRequest.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupRequestData.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupRequestFile.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupRequestHTTP.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupServer.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupSession.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupSessionAsync.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupSessionFeature.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupSessionSync.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupSocket.html
/usr/share/gtk-doc/html/libsoup-2.4/SoupURI.html
/usr/share/gtk-doc/html/libsoup-2.4/annotation-glossary.html
/usr/share/gtk-doc/html/libsoup-2.4/ch01.html
/usr/share/gtk-doc/html/libsoup-2.4/ch02.html
/usr/share/gtk-doc/html/libsoup-2.4/ch03.html
/usr/share/gtk-doc/html/libsoup-2.4/ch04.html
/usr/share/gtk-doc/html/libsoup-2.4/ch05.html
/usr/share/gtk-doc/html/libsoup-2.4/home.png
/usr/share/gtk-doc/html/libsoup-2.4/index.html
/usr/share/gtk-doc/html/libsoup-2.4/ix01.html
/usr/share/gtk-doc/html/libsoup-2.4/left-insensitive.png
/usr/share/gtk-doc/html/libsoup-2.4/left.png
/usr/share/gtk-doc/html/libsoup-2.4/libsoup-2.4-HTML-Form-Support.html
/usr/share/gtk-doc/html/libsoup-2.4/libsoup-2.4-Soup-Miscellaneous-Utilities.html
/usr/share/gtk-doc/html/libsoup-2.4/libsoup-2.4-SoupServer-deprecated-API.html
/usr/share/gtk-doc/html/libsoup-2.4/libsoup-2.4-Top-Level-Domain-utils.html
/usr/share/gtk-doc/html/libsoup-2.4/libsoup-2.4-Version-Information.html
/usr/share/gtk-doc/html/libsoup-2.4/libsoup-2.4-WebSockets.html
/usr/share/gtk-doc/html/libsoup-2.4/libsoup-2.4-XMLRPC-Support.html
/usr/share/gtk-doc/html/libsoup-2.4/libsoup-2.4-soup-method.html
/usr/share/gtk-doc/html/libsoup-2.4/libsoup-2.4-soup-status.html
/usr/share/gtk-doc/html/libsoup-2.4/libsoup-2.4.devhelp2
/usr/share/gtk-doc/html/libsoup-2.4/libsoup-build-howto.html
/usr/share/gtk-doc/html/libsoup-2.4/libsoup-client-howto.html
/usr/share/gtk-doc/html/libsoup-2.4/libsoup-request-howto.html
/usr/share/gtk-doc/html/libsoup-2.4/libsoup-server-howto.html
/usr/share/gtk-doc/html/libsoup-2.4/libsoup-session-porting.html
/usr/share/gtk-doc/html/libsoup-2.4/right-insensitive.png
/usr/share/gtk-doc/html/libsoup-2.4/right.png
/usr/share/gtk-doc/html/libsoup-2.4/style.css
/usr/share/gtk-doc/html/libsoup-2.4/up-insensitive.png
/usr/share/gtk-doc/html/libsoup-2.4/up.png

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

%files locales -f libsoup.lang
%defattr(-,root,root,-)

