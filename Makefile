# Makefile for iSamples vocabularies
#
PYTHON := python3
# The vocabulary sources, should contain the root vocabularies only, ./src/*.ttl
SRC := vocabulary
ROOT_VOCAB_SOURCES := earthenv_material_extension_mineral_group earthenv_material_extension_rock_sediment earthenv_sampled_feature_role earthenv_specimen_type
ROOT_VOCAB_URIS := ming_mineralgroupvocabulary rksd_rocksedimentvocabulary essfrole_sfrolevocabulary  esmat_essampletype
# RDFLib triplestore cache
CACHE_DIR := cache
CACHE := "$(CACHE_DIR)/vocabularies.db"
# Generated documentation
DOCS := docs

# all is the default rule if no rule is specified in the make call
.PHONY: all
all: docs cache

# === cache ===
# Cache is a triple store containing all the vocabularies and extensions
.PHONY: cache
cache: _$(CACHE_DIR) cache_root
	@echo "in cache makefile"
_$(CACHE_DIR):
	mkdir -p $(CACHE_DIR)
# Start with the root vocabularies, otherwise extensions do nothing
.PHONY: cache_root
cache_root: $(patsubst %,%.ttl,$(ROOT_VOCAB_SOURCES))

# === docs ===
# Docs are markdown generated from the vocabularies.
# Basically ordered hierarchies of concepts with associated descriptions
.PHONY: docs
docs: setup_docs $(ROOT_VOCAB_URIS)
setup_docs:
	@echo "in set_up docs makefile"
	mkdir -p $(DOCS)


# this rule applies to any target name with a .ttl extension. This will run on all
#  the $(ROOT_VOCAB_SOURCES)  becasue of the cache_root rule.
%.ttl:
	${PYTHON} tools/vocab.py --verbosity ERROR -s $(CACHE) load $(SRC)/$@
	@echo "running vocab.py on "  $@

# this rule applies to any target name/ will run al the $(ROOT_VOCAB_URIS)
#  becasue of the docs: rule
%:
	@echo $(subst _,:,$@)
	@echo "running vocab2md on " $@
	${PYTHON} tools/vocab2md.py $(CACHE) $(subst _,:,$@) > $(DOCS)/$@.md

# ===HELP===
.PHONY: help
help:
	@echo "Make artifacts from vocabulary sources"
	@echo "  cache: generate triplestore cache of all vocabs and extensions"
	@echo "  clean: remove all generate artifacts"
	@echo "  docs: generate documentation in /docs"
	@echo "  uijson: generate the JSON vocabulary configurations for WebUI"



# === clean ===
# Remove any generated artifacts
clean:
	rm -rf $(DOCS)
	rm -rf $(CACHE)
