
dist/checksum-1.0.tar.gz: checksum.c setup.py
	python3.11 setup.py sdist

.PHONY: clean
clean:
	$(RM) -r build dist

