%global srcname cryptography

%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}

%global python3_pkgversion %{nil}

%bcond_with tests

Name:           %{?scl_prefix}python-%{srcname}
Version:        2.8
Release:        4%{?dist}
Summary:        PyCA's cryptography library

License:        ASL 2.0 or BSD
URL:            https://cryptography.io/en/latest/
Source0:        https://pypi.io/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz

%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
BuildRequires:  openssl-devel
BuildRequires:  gcc

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-asn1crypto >= 0.21
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-cffi >= 1.7
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-idna >= 2.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-six >= 1.4.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-rpm-macros

%if %{with tests}
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-cryptography-vectors = %{version}
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-hypothesis >= 1.11.4
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-iso8601
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pretend
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest >= 3.2.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytz
%endif

Requires:       openssl-libs
Requires:       %{?scl_prefix}python%{python3_pkgversion}-idna >= 2.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-asn1crypto >= 0.21
Requires:       %{?scl_prefix}python%{python3_pkgversion}-six >= 1.4.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-cffi >= 1.7

%description
cryptography is a package designed to expose cryptographic primitives and
recipes to Python developers.

%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -p1 -n %{srcname}-%{version}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
# Actually other *.c and *.h are appropriate
# see https://github.com/pyca/cryptography/issues/1463
find . -name .keep -print -delete
%py3_install
%{?scl:EOF}


%check
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%if %{with tests}
PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} -m pytest -k "not (test_buffer_protocol_alternate_modes or test_dh_parameters_supported or test_load_ecdsa_no_named_curve)"
%endif


%{?scl:EOF}


%files
%doc README.rst docs
%license LICENSE LICENSE.APACHE LICENSE.BSD
%{python3_sitearch}/%{srcname}
%{python3_sitearch}/%{srcname}-%{version}-py*.egg-info


%changelog
* Thu Feb 06 2020 Lumír Balhar <lbalhar@redhat.com> - 2.8-4
- Import from the python38 module and modified for rh-python38 RHSCL
Resolves: rhbz#1671025

* Fri Dec 13 2019 Tomas Orsava <torsava@redhat.com> - 2.8-3
- Exclude unsupported i686 arch

* Thu Nov 21 2019 Lumír Balhar <lbalhar@redhat.com> - 2.8-2
- Adjusted for Python 3.8 module in RHEL 8

* Thu Oct 17 2019 Christian Heimes <cheimes@redhat.com> - 2.8-1
- Update to 2.8
- Resolves: rhbz#1762779

* Sun Oct 13 2019 Christian Heimes <cheimes@redhat.com> - 2.7-3
- Skip unit tests that fail with OpenSSL 1.1.1.d
- Resolves: rhbz#1761194
- Fix and simplify Python 3 packaging

* Sat Oct 12 2019 Christian Heimes <cheimes@redhat.com> - 2.7-2
- Drop Python 2 package
- Resolves: rhbz#1761081

* Tue Sep 03 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.7-1
- Update to 2.7 (#1715680).

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 28 2019 Christian Heimes <cheimes@redhat.com> - 2.6.1-1
- New upstream release 2.6.1, resolves RHBZ#1683691

* Wed Feb 13 2019 Alfredo Moralejo <amoralej@redhat.com> - 2.5-1
- Updated to 2.5.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 13 2018 Christian Heimes <cheimes@redhat.com> - 2.3-2
- Use TLSv1.2 in test as workaround for RHBZ#1615143

* Wed Jul 18 2018 Christian Heimes <cheimes@redhat.com> - 2.3-1
- New upstream release 2.3
- Fix AEAD tag truncation bug, RHBZ#1602752

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-2
- Rebuilt for Python 3.7

* Wed Mar 21 2018 Christian Heimes <cheimes@redhat.com> - 2.2.1-1
- New upstream release 2.2.1

* Sun Feb 18 2018 Christian Heimes <cheimes@redhat.com> - 2.1.4-1
- New upstream release 2.1.4

* Sun Feb 18 2018 Christian Heimes <cheimes@redhat.com> - 2.1.3-4
- Build requires gcc

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1.3-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild