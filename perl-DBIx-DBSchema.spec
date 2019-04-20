#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DBIx-DBSchema
Version  : 0.45
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/I/IV/IVAN/DBIx-DBSchema-0.45.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IV/IVAN/DBIx-DBSchema-0.45.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libd/libdbix-dbschema-perl/libdbix-dbschema-perl_0.45-1.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-DBIx-DBSchema-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(DBI)

%description
DBIx::DBSchema
All rights reserved.
This program is free software; you can redistribute it and/or modify it under
the same terms as Perl itself.

%package dev
Summary: dev components for the perl-DBIx-DBSchema package.
Group: Development
Provides: perl-DBIx-DBSchema-devel = %{version}-%{release}

%description dev
dev components for the perl-DBIx-DBSchema package.


%package license
Summary: license components for the perl-DBIx-DBSchema package.
Group: Default

%description license
license components for the perl-DBIx-DBSchema package.


%prep
%setup -q -n DBIx-DBSchema-0.45
cd ..
%setup -q -T -D -n DBIx-DBSchema-0.45 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/DBIx-DBSchema-0.45/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-DBIx-DBSchema
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-DBIx-DBSchema/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/DBIx/DBSchema.pm
/usr/lib/perl5/vendor_perl/5.28.2/DBIx/DBSchema/Column.pm
/usr/lib/perl5/vendor_perl/5.28.2/DBIx/DBSchema/DBD.pm
/usr/lib/perl5/vendor_perl/5.28.2/DBIx/DBSchema/DBD/Oracle.pm
/usr/lib/perl5/vendor_perl/5.28.2/DBIx/DBSchema/DBD/Pg.pm
/usr/lib/perl5/vendor_perl/5.28.2/DBIx/DBSchema/DBD/SQLite.pm
/usr/lib/perl5/vendor_perl/5.28.2/DBIx/DBSchema/DBD/Sybase.pm
/usr/lib/perl5/vendor_perl/5.28.2/DBIx/DBSchema/DBD/mysql.pm
/usr/lib/perl5/vendor_perl/5.28.2/DBIx/DBSchema/ForeignKey.pm
/usr/lib/perl5/vendor_perl/5.28.2/DBIx/DBSchema/Index.pm
/usr/lib/perl5/vendor_perl/5.28.2/DBIx/DBSchema/Table.pm
/usr/lib/perl5/vendor_perl/5.28.2/DBIx/DBSchema/_util.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DBIx::DBSchema.3
/usr/share/man/man3/DBIx::DBSchema::Column.3
/usr/share/man/man3/DBIx::DBSchema::DBD.3
/usr/share/man/man3/DBIx::DBSchema::DBD::Oracle.3
/usr/share/man/man3/DBIx::DBSchema::DBD::Pg.3
/usr/share/man/man3/DBIx::DBSchema::DBD::SQLite.3
/usr/share/man/man3/DBIx::DBSchema::DBD::Sybase.3
/usr/share/man/man3/DBIx::DBSchema::DBD::mysql.3
/usr/share/man/man3/DBIx::DBSchema::ForeignKey.3
/usr/share/man/man3/DBIx::DBSchema::Index.3
/usr/share/man/man3/DBIx::DBSchema::Table.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-DBIx-DBSchema/deblicense_copyright
