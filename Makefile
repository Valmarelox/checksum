
dist/checksum-1.0.linux-x86_64.tar.gz: checksum.c setup.py
	python3.11 setup.py bdist

.PHONY: clean
clean:
	$(RM) -r build dist
