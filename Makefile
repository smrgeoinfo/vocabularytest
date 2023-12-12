# Makefile for iSamples vocabularies
#
PYTHON := python3

# The vocabulary sources, should contain the root vocabularies only, ./src/*.ttl
SRC := src

# Vocabulary extensions, ./src/extensions/*.ttl
EXTENSIONS := $(SRC)/extensions

ROOT_VOCAB_SOURCES := materialtype sampledfeature specimentype
ROOT_VOCAB_URIS := mat_materialsvocabulary sf_sampledfeaturevocabulary spec_specimentypevocabulary
EXTENSION_VOCABS := $(wildcard $(EXTENSIONS)/*.ttl)

# RDFLib triplestore cache
CACHE_DIR := cache
CACHE := "$(CACHE_DIR)/vocabularies.db"

# Generated documentation
DOCS := docs

.PHONY: all
all: docs cache

.PHONY: help
help:
	@echo "Make artifacts from vocabulary sources"
	@echo "  cache: generate triplestore cache of all vocabs and extensions"
	@echo "  clean: remove all generate artifacts"
	@echo "  docs: generate documentation in /docs"
	@echo "  uijson: generate the JSON vocabulary configurations for WebUI"

# === cache ===
# Cache is a triple store containing all the vocabularies and extensions
.PHONY: cache
cache: _$(CACHE_DIR) cache_root cache_extensions

_$(CACHE_DIR):
	mkdir -p $(CACHE_DIR)

# Start with the root vocabularies, otherwise extensions do nothing
.PHONY: cache_root
cache_root: $(patsubst %,%.ttl,$(ROOT_VOCAB_SOURCES))
%.ttl:
	${PYTHON} tools/vocab.py --verbosity ERROR -s $(CACHE) load $(SRC)/$@

.PHONY: cache_extensions
cache_extensions: $(EXTENSION_VOCABS)
	for src_file in $^ ; do \
		echo "Loading $${src_file} ..." ; \
		$(PYTHON) tools/vocab.py --verbosity ERROR -s $(CACHE) load $${src_file} ; \
	done


# === docs ===
# Docs are markdown generated from the vocabularies.
# Basically ordered hierarchies of concepts with associated descriptions
.PHONY: docs
docs: setup_docs $(ROOT_VOCAB_URIS)

setup_docs:
	mkdir -p $(DOCS)

%:
	@echo $(subst _,:,$@)
	${PYTHON} tools/vocab2md.py $(CACHE) $(subst _,:,$@) > $(DOCS)/$@.md

# === clean ===
# Remove any generated artifacts
clean:
	rm -rf $(DOCS)
	rm -rf $(CACHE)
