# Makefile for iSamples vocabularies
#
PYTHON := python3

# The vocabulary sources, should contain the root vocabularies only, ./src/*.ttl
SRC := vocabulary

# Vocabulary extensions, ./src/extensions/*.ttl
# EXTENSIONS := $(SRC)/extensions

ROOT_VOCAB_SOURCES := earthenv_material_extension_mineral_group earthenv_material_extension_rock_sediment earthenv_sampled_feature_role earthenv_specimen_type
ROOT_VOCAB_URIS := ming_mineralgroupvocabulary rksd_rocksedimentvocabulary essfrole_sfrolevocabulary  esmat_essampletype
# EXTENSION_VOCABS := $(wildcard $(EXTENSIONS)/*.ttl)

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
#cache: _$(CACHE_DIR) cache_root cache_extensions
cache: _$(CACHE_DIR) cache_root 

_$(CACHE_DIR):
	mkdir -p $(CACHE_DIR)

# Start with the root vocabularies, otherwise extensions do nothing
.PHONY: cache_root
cache_root: $(patsubst %,%.ttl,$(ROOT_VOCAB_SOURCES))
%.ttl:
	${PYTHON} tools/vocab.py --verbosity ERROR -s $(CACHE) load $(SRC)/$@

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
