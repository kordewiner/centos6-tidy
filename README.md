# centos6-tidy
SPEC file for CentOS 6 and latest Tidy from http://www.html-tidy.org as replacement for 
http://vault.centos.org/6.7/os/Source/SPackages/tidy-0.99.0-19.20070615.1.el6.src.rpm .

Does not touch `libtidy 0.99.0`.

Use like this:

    rpmdev-setuptree
    cd ~/rpmbuild
    wget -SPECS/tidy.spec https://raw.githubusercontent.com/kordewiner/centos6-tidy/master/tidy.spec
    spectool --get-files --sourcedir SPECS/tidy.spec
    rpmbuild --ba SPECS/tidy.spec
