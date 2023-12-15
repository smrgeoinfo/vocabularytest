---
comment: | 
  WARNING: This file is generated. Any edits will be lost!
title: "Earth and Environmental Science specimen type extension"
date: "2023-12-15T17:30:20.838618+00:00"
subtitle: |
  This concept scheme contains skos concepts for categorizing kinds of Earth Material sample types, extending the iSamples Material Sample Type vocabulary. Defintions from SESAR, ODM2, wikipedia, ESS-DIVE, and other sources; sources are cited with each term.
execute:
  echo: false
---

Namespace: 
[`https://w3id.org/isample/1.0/esmaterialsample/essampletype`](https://w3id.org/isample/1.0/esmaterialsample/essampletype)

**History**

* 2023-07-07 SMR add solid material sample and broader relations from classes it subsumes.
* 2023-07-27 SMR modify base specimen type vocabulary, add 'Non biologic solid object' to replace 'solid material sample', change broader relations in this vocab to use that as parent class where appropriate. 'Solid material sample' is too closely linked to material type, created confusion. Intention is a specimen category for solid objects that are not biologic. Obviously there is some overlap with Research specimens.

**Concepts**

- [Analytical preparation](#analyticalpreparation)
    - [Cell culture](#cellculture)
    - [Dissolved chemical fraction](#dissolvedchemicalfraction)
        - [Eluate](#eluate)
    - [FIB lamella](#fiblamella)
    - [Glass slide smear](#glassslidesmear)
    - [Individual solid cube](#individualsolidcube)
    - [Magnetic fraction](#magneticfraction)
    - [Mechanical fraction](#mechanicalfraction)
    - [Mineral separate](#mineralseparate)
        - [Magnetic fraction](#magneticfraction)
        - [Non-magnetic fraction](#nonmagneticfraction)
    - [Sectioned specimen](#mountedsection)
        - [Thick section](#thicksection)
        - [Thin section](#thinsection)
            - [Polished thin section](#polishedthinsection)
        - [Ultra thin section](#ultrathinsection)
    - [Non-magnetic fraction](#nonmagneticfraction)
    - [Peel](#peel)
    - [Prepared powder](#preparedpowder)
        - [Prepared rock powder](#preparedrockpowder)
    - [Pressed pellet](#pressedpellet)
    - [Residual material](#residualmaterial)
    - [Slab](#slab)

- [Bundle biome aggregation](#bundlebiomeaggregation)
    - [Cell culture](#cellculture)

- [Fluid in container](#fluidincontainer)
    - [Direct fluid sample](#directfluidsample)
    - [Dissolved chemical fraction](#dissolvedchemicalfraction)
        - [Eluate](#eluate)
    - [Processed fluid sample](#processedfluidsample)
        - [Filtrate](#filtrate)

- [genericAggregation](#genericaggregation)
    - [Boxed core](#boxedcore)
    - [Composite sample](#compositesample)
        - [Chip Channel Sample](#chipchannelsample)
        - [High Grade Sample](#highgradesample)
        - [Site composite sample](#sitecompositesample)
    - [Core Catcher](#corecatcher)
    - [Cuttings](#cuttings)
    - [Dredge](#dredge)
    - [Material Captured in Filter](#materialcapturedinfilter)
    - [Mechanical fraction](#mechanicalfraction)
    - [Mineral separate](#mineralseparate)
        - [Magnetic fraction](#magneticfraction)
        - [Non-magnetic fraction](#nonmagneticfraction)
    - [Natural aggregate specimen](#naturalaggregate)
    - [Prepared powder](#preparedpowder)
        - [Prepared rock powder](#preparedrockpowder)
    - [Trawl](#trawl)
    - [Resonance ionization mass spectrometry](#temgrid)

- [Other solid Object](#othersolidobject)
    - [Dust wipe](#dustwipe)
    - [Glass slide smear](#glassslidesmear)
    - [Peel](#peel)

##  Analytical preparation

[]{#analyticalpreparation}

Concept: [`analyticalpreparation`](https://w3id.org/isample/vocabulary/specimentype/1.0/analyticalpreparation)


###  Cell culture

[]{#cellculture}

Concept: [`cellculture`](https://w3id.org/isample/1.0/esmaterialsample/cellculture)

Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`bundlebiomeaggregation`](#bundlebiomeaggregation)

a collection of cells are grown under controlled conditions, generally
outside of their natural environment

###  Dissolved chemical fraction

[]{#dissolvedchemicalfraction}

Concept: [`dissolvedchemicalfraction`](https://w3id.org/isample/1.0/esmaterialsample/dissolvedchemicalfraction)

Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`fluidincontainer`](#fluidincontainer)

A fluid concentrating some constituent of interest from a parent
sample. The dissolved constituent is actually the sample material of
interest.

####  Eluate

[]{#eluate}

Concept: [`eluate`](https://w3id.org/isample/vocabulary/specimentype/1.0/eluate)

Child of:
 [`dissolvedchemicalfraction`](#dissolvedchemicalfraction)

The fluid product that contains the analyte of interest washed from a
chromatography column

###  FIB lamella

[]{#fiblamella}

Concept: [`fiblamella`](https://w3id.org/isample/1.0/esmaterialsample/fiblamella)

Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`solidmaterialspecimen`](#solidmaterialspecimen)

very thin sheet of solid material milled from a larger sample using a
focused ion beam. Used for TEM analysis.

###  Glass slide smear

[]{#glassslidesmear}

Concept: [`glassslidesmear`](https://w3id.org/isample/1.0/esmaterialsample/glassslidesmear)

Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`othersolidobject`](#othersolidobject)

sample from a cell culture (or other microparticulate suspension)
spread into a thin layer on a glass slide for optical investigation

###  Individual solid cube

[]{#individualsolidcube}

Concept: [`individualsolidcube`](https://w3id.org/isample/1.0/esmaterialsample/individualsolidcube)

Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`solidmaterialspecimen`](#solidmaterialspecimen)

A sample that is a prepared cube of material, intended as a sample of
that material.

###  Magnetic fraction

[]{#magneticfraction}

Concept: [`magneticfraction`](https://w3id.org/isample/1.0/esmaterialsample/magneticfraction)

Child of:
 [`mineralseparate`](#mineralseparate)
 [`analyticalpreparation`](#analyticalpreparation)

a collection of particles separated from a crushed rock sample based
on their attraction to a magnet.

###  Mechanical fraction

[]{#mechanicalfraction}

Concept: [`mechanicalfraction`](https://w3id.org/isample/1.0/esmaterialsample/mechanicalfraction)

Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`genericaggregation`](#genericaggregation)

defined by sample preparation involving mechanical processing, e.g.
grain size, density, or grain shape separation.

###  Mineral separate

[]{#mineralseparate}

Concept: [`mineralseparate`](https://w3id.org/isample/1.0/esmaterialsample/mineralseparate)

Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`genericaggregation`](#genericaggregation)

an aggregation of particles of the same mineral extracted and
concentrated from a rock.

####  Magnetic fraction

[]{#magneticfraction}

Concept: [`magneticfraction`](https://w3id.org/isample/1.0/esmaterialsample/magneticfraction)

Child of:
 [`mineralseparate`](#mineralseparate)
 [`analyticalpreparation`](#analyticalpreparation)

a collection of particles separated from a crushed rock sample based
on their attraction to a magnet.

####  Non-magnetic fraction

[]{#nonmagneticfraction}

Concept: [`nonmagneticfraction`](https://w3id.org/isample/1.0/esmaterialsample/nonmagneticfraction)

Child of:
 [`mineralseparate`](#mineralseparate)
 [`analyticalpreparation`](#analyticalpreparation)

collection of particles from a crushed rock sample based on their lack
of attraction to a magnet

###  Sectioned specimen

[]{#mountedsection}

Concept: [`mountedsection`](https://w3id.org/isample/1.0/esmaterialsample/mountedsection)

Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`solidmaterialspecimen`](#solidmaterialspecimen)

a thin slice of a solid material that has been mounted on a glass
slide for study

####  Thick section

[]{#thicksection}

Concept: [`thicksection`](https://w3id.org/isample/1.0/esmaterialsample/thicksection)

Child of:
 [`mountedsection`](#mountedsection)

Thick sections are like thin sections, but milled to a greater
thickness. Typcially polished on one or both sides and used for fluid
or melt inclusion studies, Raman analyses, and infrared spectroscopy
analyses, and SEM or electron microprobe. The standard thickness for a
fluid inclusion thick section is 50 micrometers, but thick sections
can be made at any thickness.  Thick sections can be attached to a
glass slide, or can be prepared so that they can be removed from their
mount as a stand-alone slice of rock.

####  Thin section

[]{#thinsection}

Concept: [`thinsection`](https://w3id.org/isample/1.0/esmaterialsample/thinsection)

Child of:
 [`mountedsection`](#mountedsection)

thin sliver of rock cut from a sample with a diamond saw and ground
optically flat, and then mounted on a glass slide and ground smooth
using progressively finer abrasive grit until the sample is 30 microns
thick.

#####  Polished thin section

[]{#polishedthinsection}

Concept: [`polishedthinsection`](https://w3id.org/isample/1.0/esmaterialsample/polishedthinsection)

Child of:
 [`thinsection`](#thinsection)

a thin section that has its free surface polished until perfectly
planar and free of pits and scratches. Used for reflected light
petrography and for electron microprobe or SEM investigation.

####  Ultra thin section

[]{#ultrathinsection}

Concept: [`ultrathinsection`](https://w3id.org/isample/1.0/esmaterialsample/ultrathinsection)

Child of:
 [`mountedsection`](#mountedsection)

An ordinary thin section that is attached to the glass slide using a
soluble cement such as Canada balsam (soluble in ethanol) to allow
both sides to be worked on. The section is polished on both sides
using a fine diamond paste until it has a thickness in the range of
2-12 microns. This technique has been used to study the microstructure
of very fine-grained carbonate rocks, and also in the preparation of
mineral and rock specimens for transmission electron microscopy.

###  Non-magnetic fraction

[]{#nonmagneticfraction}

Concept: [`nonmagneticfraction`](https://w3id.org/isample/1.0/esmaterialsample/nonmagneticfraction)

Child of:
 [`mineralseparate`](#mineralseparate)
 [`analyticalpreparation`](#analyticalpreparation)

collection of particles from a crushed rock sample based on their lack
of attraction to a magnet

###  Peel

[]{#peel}

Concept: [`peel`](https://w3id.org/isample/1.0/esmaterialsample/peel)

Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`othersolidobject`](#othersolidobject)

Acetate peels are made by polishing a planar surface on a sample,
etching it with acid to give it some relief, and then chemically
melting a piece of acetate onto that surface. The acetate is then
pulled off for examination under a microscope. The acetate preserves a
fingerprint of the internal structure of the sample surface. Used in
paleontology to study complex fossils, e.g. bryozoan.

###  Prepared powder

[]{#preparedpowder}

Concept: [`preparedpowder`](https://w3id.org/isample/1.0/esmaterialsample/preparedpowder)

Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`genericaggregation`](#genericaggregation)

distinguish from particulate in that particulate is sampled as a
micron-size aggregate, whereas this material is ground to a powder for
subsequent analysis; it is a powder as a function of some preparation
process (e.g. chemical precipitation)

####  Prepared rock powder

[]{#preparedrockpowder}

Concept: [`preparedrockpowder`](https://w3id.org/isample/1.0/esmaterialsample/preparedrockpowder)

Child of:
 [`preparedpowder`](#preparedpowder)

a powder manufactured by pulverizing a rock.

###  Pressed pellet

[]{#pressedpellet}

Concept: [`pressedpellet`](https://w3id.org/isample/1.0/esmaterialsample/pressedpellet)

Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`solidmaterialspecimen`](#solidmaterialspecimen)

a sample prepared by grinding a parent sample to a fine powder, mixing
it with a binder, and pressing the mixture into a die at a pressure of
between 15 and 35 tons to produce a solid disc for subsequent
analysis, typically by X-Ray fluorescence.

###  Residual material

[]{#residualmaterial}

Concept: [`residualmaterial`](https://w3id.org/isample/1.0/esmaterialsample/residualmaterial)

Child of:
 [`analyticalpreparation`](#analyticalpreparation)

Sample is material remaining after processing to extract some other
components of interest from the sample.

###  Slab

[]{#slab}

Concept: [`slab`](https://w3id.org/isample/1.0/esmaterialsample/slab)

Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`solidmaterialspecimen`](#solidmaterialspecimen)

a relatively planar rock sample,cut from a large sample to produce a
tabular peice of rock with the irregular outline of the original
sample on the diameter where the cut was mate.


##  Bundle biome aggregation

[]{#bundlebiomeaggregation}

Concept: [`bundlebiomeaggregation`](https://w3id.org/isample/vocabulary/specimentype/1.0/bundlebiomeaggregation)


###  Cell culture

[]{#cellculture}

Concept: [`cellculture`](https://w3id.org/isample/1.0/esmaterialsample/cellculture)

Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`bundlebiomeaggregation`](#bundlebiomeaggregation)

a collection of cells are grown under controlled conditions, generally
outside of their natural environment


##  Fluid in container

[]{#fluidincontainer}

Concept: [`fluidincontainer`](https://w3id.org/isample/vocabulary/specimentype/1.0/fluidincontainer)


###  Direct fluid sample

[]{#directfluidsample}

Concept: [`directfluidsample`](https://w3id.org/isample/1.0/esmaterialsample/directfluidsample)

Child of:
 [`fluidincontainer`](#fluidincontainer)

a fluid collected from the sampled feature (e.g. water body,
hydrothermal vent, atmosphere...) with no processing. (e.g.
filtration, addition of preservatives).

###  Dissolved chemical fraction

[]{#dissolvedchemicalfraction}

Concept: [`dissolvedchemicalfraction`](https://w3id.org/isample/1.0/esmaterialsample/dissolvedchemicalfraction)

Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`fluidincontainer`](#fluidincontainer)

A fluid concentrating some constituent of interest from a parent
sample. The dissolved constituent is actually the sample material of
interest.

####  Eluate

[]{#eluate}

Concept: [`eluate`](https://w3id.org/isample/vocabulary/specimentype/1.0/eluate)

Child of:
 [`dissolvedchemicalfraction`](#dissolvedchemicalfraction)

The fluid product that contains the analyte of interest washed from a
chromatography column

###  Processed fluid sample

[]{#processedfluidsample}

Concept: [`processedfluidsample`](https://w3id.org/isample/1.0/esmaterialsample/processedfluidsample)

Child of:
 [`fluidincontainer`](#fluidincontainer)

fluid sample that has been processed in some way during or after
collection, e.g. by filtering, addition of preservatives.

####  Filtrate

[]{#filtrate}

Concept: [`filtrate`](https://w3id.org/isample/1.0/esmaterialsample/filtrate)

Child of:
 [`processedfluidsample`](#processedfluidsample)

A sample that has gone through a filtration process to separate solids
from fluids (liquids or gases), using a filter medium through which
only the fluid can pass. Must be associated with a filter size.


##  genericAggregation

[]{#genericaggregation}

Concept: [`genericaggregation`](https://w3id.org/isample/vocabulary/specimentype/1.0/genericaggregation)


###  Boxed core

[]{#boxedcore}

Concept: [`boxedcore`](https://w3id.org/isample/1.0/esmaterialsample/boxedcore)

Child of:
 [`genericaggregation`](#genericaggregation)

A collection of core peices that are stored in an individual box.
Typically the box will contain core peices from the same core.

###  Composite sample

[]{#compositesample}

Concept: [`compositesample`](https://w3id.org/isample/1.0/esmaterialsample/compositesample)

Child of:
 [`genericaggregation`](#genericaggregation)

a sample composed of multiple peices, representative of some material,
or representative of some site. The peices do not all originate from
the same object.

####  Chip Channel Sample

[]{#chipchannelsample}

Concept: [`chipchannelsample`](https://w3id.org/isample/1.0/esmaterialsample/chipchannelsample)

Child of:
 [`compositesample`](#compositesample)

small chips of rock collected over a specified interval, with the
objective to obtain a representative sample for that interval. Most of
the time chip channel samples are collected in succession along a
sample line which is laid out in advance using a tape.  The freshest
material possible is sampled, preferably chipping directly from
bedrock. Sample intervals are set at a specified width, usually
ranging from 30cm to 7m. Due to the method of sampling, chip channel
samples tend to be rather large (up to 20 pounds for a five foot
interval)

####  High Grade Sample

[]{#highgradesample}

Concept: [`highgradesample`](https://w3id.org/isample/1.0/esmaterialsample/highgradesample)

Child of:
 [`compositesample`](#compositesample)

in mineral exploration, selective pieces of the most highly
mineralized material from a mineralize site, intentionally excluding
less mineralized material. A high grade sample might be collected to
indicate what the best possible values are, or to provide material for
certain types of trace element analyses.

####  Site composite sample

[]{#sitecompositesample}

Concept: [`sitecompositesample`](https://w3id.org/isample/1.0/esmaterialsample/sitecompositesample)

Child of:
 [`compositesample`](#compositesample)

an aggregation of peices of uniform material collected over some area
(generally greater than 2.5m across). These are the ideal
'representative' samples used in mineral exploration. A composite
sample might be collected to determine the background values of trace
elements in a particular type of rock, or to determine if ore grade
mineralization is present over a large area.

###  Core Catcher

[]{#corecatcher}

Concept: [`corecatcher`](https://w3id.org/isample/1.0/esmaterialsample/corecatcher)

Child of:
 [`genericaggregation`](#genericaggregation)

material recovered from the core catcher of a sedimentary core and
which is treated as a separate section from the core. The core catcher
is a device at the bottom of the core barrel that prevents the core
from sliding out while the barrel is retrieved from the hole.
(http://publications.iodp.org/proceedings/323/102/102_.htm)

###  Cuttings

[]{#cuttings}

Concept: [`cuttings`](https://w3id.org/isample/1.0/esmaterialsample/cuttings)

Child of:
 [`genericaggregation`](#genericaggregation)

unconsolidated Earth material produced by the grinding action of a
drill bit during drilling of a borehole.

###  Dredge

[]{#dredge}

Concept: [`dredge`](https://w3id.org/isample/1.0/esmaterialsample/dredge)

Child of:
 [`genericaggregation`](#genericaggregation)

an aggregation of material sampled by dragging a collection bucket
(dredge) across the bottom of a water body

###  Material Captured in Filter

[]{#materialcapturedinfilter}

Concept: [`materialcapturedinfilter`](https://w3id.org/isample/1.0/esmaterialsample/materialcapturedinfilter)

Child of:
 [`genericaggregation`](#genericaggregation)

A material sample captured in filter, for example from a water sample
that was filtered. Must be associated with filter size field.

###  Mechanical fraction

[]{#mechanicalfraction}

Concept: [`mechanicalfraction`](https://w3id.org/isample/1.0/esmaterialsample/mechanicalfraction)

Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`genericaggregation`](#genericaggregation)

defined by sample preparation involving mechanical processing, e.g.
grain size, density, or grain shape separation.

###  Mineral separate

[]{#mineralseparate}

Concept: [`mineralseparate`](https://w3id.org/isample/1.0/esmaterialsample/mineralseparate)

Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`genericaggregation`](#genericaggregation)

an aggregation of particles of the same mineral extracted and
concentrated from a rock.

####  Magnetic fraction

[]{#magneticfraction}

Concept: [`magneticfraction`](https://w3id.org/isample/1.0/esmaterialsample/magneticfraction)

Child of:
 [`mineralseparate`](#mineralseparate)
 [`analyticalpreparation`](#analyticalpreparation)

a collection of particles separated from a crushed rock sample based
on their attraction to a magnet.

####  Non-magnetic fraction

[]{#nonmagneticfraction}

Concept: [`nonmagneticfraction`](https://w3id.org/isample/1.0/esmaterialsample/nonmagneticfraction)

Child of:
 [`mineralseparate`](#mineralseparate)
 [`analyticalpreparation`](#analyticalpreparation)

collection of particles from a crushed rock sample based on their lack
of attraction to a magnet

###  Natural aggregate specimen

[]{#naturalaggregate}

Concept: [`naturalaggregate`](https://w3id.org/isample/1.0/esmaterialsample/naturalaggregate)

Child of:
 [`genericaggregation`](#genericaggregation)

E.g beach sand, soil, river sediment, scoop of regolith.
Specimen is aggregate of non-consolidated material formed by natural
processes. Particles have not been intentionally modified from the
sampled feature.

###  Prepared powder

[]{#preparedpowder}

Concept: [`preparedpowder`](https://w3id.org/isample/1.0/esmaterialsample/preparedpowder)

Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`genericaggregation`](#genericaggregation)

distinguish from particulate in that particulate is sampled as a
micron-size aggregate, whereas this material is ground to a powder for
subsequent analysis; it is a powder as a function of some preparation
process (e.g. chemical precipitation)

####  Prepared rock powder

[]{#preparedrockpowder}

Concept: [`preparedrockpowder`](https://w3id.org/isample/1.0/esmaterialsample/preparedrockpowder)

Child of:
 [`preparedpowder`](#preparedpowder)

a powder manufactured by pulverizing a rock.

###  Trawl

[]{#trawl}

Concept: [`trawl`](https://w3id.org/isample/1.0/esmaterialsample/trawl)

Child of:
 [`genericaggregation`](#genericaggregation)

an aggregation of biogenic or non-biogenic material extracted from a
water body

###  Resonance ionization mass spectrometry

[]{#temgrid}

Concept: [`temgrid`](https://w3id.org/isample/vocabulary/specimentype/1.0/temgrid)

Child of:
 [`genericaggregation`](#genericaggregation)

FIB sections and microtome slices set onto a small grid for handling,
transport, and analysis using a transmission electron microscope
(TEM). The grid itself can be given a single sample identifier
(similar to how there are multiple grains in a grain mount). The
linkage from the individual samples in the grid to their parent
sample(s) should be documented


##  Other solid Object

[]{#othersolidobject}

Concept: [`othersolidobject`](https://w3id.org/isample/vocabulary/specimentype/1.0/othersolidobject)


###  Dust wipe

[]{#dustwipe}

Concept: [`dustwipe`](https://w3id.org/isample/1.0/esmaterialsample/dustwipe)

Child of:
 [`othersolidobject`](#othersolidobject)

a pre-weighed and packaged paper towel (wipe) used to wipe over a
surface to collect particulates from the surface

###  Glass slide smear

[]{#glassslidesmear}

Concept: [`glassslidesmear`](https://w3id.org/isample/1.0/esmaterialsample/glassslidesmear)

Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`othersolidobject`](#othersolidobject)

sample from a cell culture (or other microparticulate suspension)
spread into a thin layer on a glass slide for optical investigation

###  Peel

[]{#peel}

Concept: [`peel`](https://w3id.org/isample/1.0/esmaterialsample/peel)

Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`othersolidobject`](#othersolidobject)

Acetate peels are made by polishing a planar surface on a sample,
etching it with acid to give it some relief, and then chemically
melting a piece of acetate onto that surface. The acetate is then
pulled off for examination under a microscope. The acetate preserves a
fingerprint of the internal structure of the sample surface. Used in
paleontology to study complex fossils, e.g. bryozoan.


