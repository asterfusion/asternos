.ONESHELL:
SHELL = /bin/bash
.SHELLFLAGS += -e

PYTHON_VER=3.7.3
PYTHON_DEB_VER=2+deb10u1
PYTHON_PNAME=python3.7

MAIN_TARGET = lib$(PYTHON_PNAME)-minimal_$(PYTHON_VER)-$(PYTHON_DEB_VER)_$(CONFIGURED_ARCH).deb
DERIVED_TARGETS = lib$(PYTHON_PNAME)-stdlib_$(PYTHON_VER)-$(PYTHON_DEB_VER)_$(CONFIGURED_ARCH).deb \
				  lib$(PYTHON_PNAME)-all_$(PYTHON_VER)-$(PYTHON_DEB_VER)_$(CONFIGURED_ARCH).deb \
				  $(PYTHON_PNAME)-minimal_$(PYTHON_VER)-$(PYTHON_DEB_VER)_$(CONFIGURED_ARCH).deb \
				  $(PYTHON_PNAME)-all_$(PYTHON_VER)-$(PYTHON_DEB_VER)_$(CONFIGURED_ARCH).deb \
				  lib$(PYTHON_PNAME)-dev_$(PYTHON_VER)-$(PYTHON_DEB_VER)_$(CONFIGURED_ARCH).deb \
				  $(PYTHON_PNAME)-dev_$(PYTHON_VER)-$(PYTHON_DEB_VER)_$(CONFIGURED_ARCH).deb

$(addprefix $(DEST)/, $(MAIN_TARGET)): $(DEST)/% :
	# Remove any stale files
	rm -rf $(PYTHON_PNAME)-$(PYTHON_VER)

#	## Obtaining the python3
	wget 'http://deb.debian.org/debian/pool/main/p/python3.7/$(PYTHON_PNAME)_$(PYTHON_VER).orig.tar.xz' 
	wget 'http://deb.debian.org/debian/pool/main/p/python3.7/$(PYTHON_PNAME)_$(PYTHON_VER)-$(PYTHON_DEB_VER).dsc'
	wget 'http://deb.debian.org/debian/pool/main/p/python3.7/$(PYTHON_PNAME)_$(PYTHON_VER)-$(PYTHON_DEB_VER).debian.tar.xz'
#	## Build
	dpkg-source -x $(PYTHON_PNAME)_$(PYTHON_VER)-$(PYTHON_DEB_VER).dsc
	pushd $(PYTHON_PNAME)-$(PYTHON_VER)
	mk-build-deps --arch $(CONFIGURED_ARCH)
	
	echo "====" $@ "===="
	# put a lock here because dpkg does not allow installing packages in parallel
	while true; do
	if mkdir $(DEST)/dpkg_lock ; then
	{ echo here && (sudo apt-get -y install ./$(PYTHON_PNAME)-build-deps_$(PYTHON_VER)-$(PYTHON_DEB_VER)_$(CONFIGURED_ARCH).deb || sudo apt-get install -f) && rm -d $(DEST)/dpkg_lock && break; } || { rm -d $(DEST)/dpkg_lock && exit 1 ; }
	fi
	done

	dpkg-buildpackage -rfakeroot -us -uc -b -j$(SONIC_CONFIG_MAKE_JOBS)
	popd

	cp $(DERIVED_TARGETS) $* $(DEST)/

$(addprefix $(DEST)/, $(DERIVED_TARGETS)): $(DEST)/% : $(DEST)/$(MAIN_TARGET)
