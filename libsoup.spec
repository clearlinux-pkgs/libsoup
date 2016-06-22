#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libsoup
Version  : 2.54.1
Release  : 6
URL      : http://ftp.gnome.org/pub/gnome/sources/libsoup/2.54/libsoup-2.54.1.tar.xz
Source0  : http://ftp.gnome.org/pub/gnome/sources/libsoup/2.54/libsoup-2.54.1.tar.xz
Summary  : a glib-based HTTP library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: libsoup-lib
Requires: libsoup-data
Requires: libsoup-doc
Requires: libsoup-locales
BuildRequires : curl-dev
BuildRequires : docbook-xml
BuildRequires : e2fsprogs-dev
BuildRequires : gettext
BuildRequires : glib-networking
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : krb5-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
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


%package locales
Summary: locales components for the libsoup package.
Group: Default

%description locales
locales components for the libsoup package.


%prep
%setup -q -n libsoup-2.54.1

%build
%configure --disable-static --enable-introspection --disable-vala
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
%find_lang libsoup

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/gir-1.0/Soup-2.4.gir
/usr/share/gir-1.0/SoupGNOME-2.4.gir

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
/usr/lib64/*.so
/usr/lib64/girepository-1.0/Soup-2.4.typelib
/usr/lib64/girepository-1.0/SoupGNOME-2.4.typelib
/usr/lib64/pkgconfig/*.pc

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
/usr/share/gtk-doc/html/libsoup-2.4/index.sgml
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
/usr/lib64/*.so.*

%files locales -f libsoup.lang 
%defattr(-,root,root,-)

