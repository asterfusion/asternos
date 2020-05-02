# SONiC make file


%::
	@echo "+++ --- Making $@ --- +++"
	BLDENV=buster make -f Makefile.work $@

clean reset init configure showtag sonic-slave-build sonic-slave-bash :
	@echo "+++ Making $@ +++"
	BLDENV=buster make -f Makefile.work $@
