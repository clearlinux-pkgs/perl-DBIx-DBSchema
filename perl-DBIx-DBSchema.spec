#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DBIx-DBSchema
Version  : 0.45
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/I/IV/IVAN/DBIx-DBSchema-0.45.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IV/IVAN/DBIx-DBSchema-0.45.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libd/libdbix-dbschema-perl/libdbix-dbschema-perl_0.45-1.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-DBIx-DBSchema-license = %{version}-%{release}
Requires: perl-DBIx-DBSchema-perl = %{version}-%{release}
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
Requires: perl-DBIx-DBSchema = %{version}-%{release}

%description dev
dev components for the perl-DBIx-DBSchema package.


%package license
Summary: license components for the perl-DBIx-DBSchema package.
Group: Default

%description license
license components for the perl-DBIx-DBSchema package.


%package perl
Summary: perl components for the perl-DBIx-DBSchema package.
Group: Default
Requires: perl-DBIx-DBSchema = %{version}-%{release}

%description perl
perl components for the perl-DBIx-DBSchema package.


%prep
%setup -q -n DBIx-DBSchema-0.45
cd %{_builddir}
tar xf %{_sourcedir}/libdbix-dbschema-perl_0.45-1.debian.tar.xz
cd %{_builddir}/DBIx-DBSchema-0.45
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/DBIx-DBSchema-0.45/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-DBIx-DBSchema
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-DBIx-DBSchema/1e1de1390a83645aeb28c01e30741470dde8647b
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
/usr/share/package-licenses/perl-DBIx-DBSchema/1e1de1390a83645aeb28c01e30741470dde8647b

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/DBSchema.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/DBSchema/Column.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/DBSchema/DBD.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/DBSchema/DBD/Oracle.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/DBSchema/DBD/Pg.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/DBSchema/DBD/SQLite.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/DBSchema/DBD/Sybase.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/DBSchema/DBD/mysql.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/DBSchema/ForeignKey.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/DBSchema/Index.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/DBSchema/Table.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/DBSchema/_util.pm
