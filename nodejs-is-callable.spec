%{?nodejs_find_provides_and_requires}
Name:                nodejs-is-callable
Version:             1.1.4
Release:             2
Summary:             Is this JS value callable?
License:             MIT
URL:                 https://github.com/ljharb/is-callable
Source0:             https://registry.npmjs.org/is-callable/-/is-callable-%{version}.tgz
BuildArch:           noarch
ExclusiveArch:       %{nodejs_arches} noarch
BuildRequires:       nodejs-packaging
BuildRequires:       npm(foreach) npm(make-arrow-function) npm(make-generator-function) npm(tape)
%description
Is this JS value callable? Works with Functions and
GeneratorFunctions, despite ES6 @@toStringTag.

%prep
%setup -q -n package
rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/is-callable
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/is-callable
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} --harmony test.js

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/is-callable

%changelog
* Thu Mar 01 2022 Yongqing chen <chenyongqingdl@gmail.com> - 1.1.4-2
- Replace --es-staging  with --harmony option 

* Thu Aug 20 2020 wangxiao <wangxiao65@huawei.com> - 1.1.4-1
- Package init
