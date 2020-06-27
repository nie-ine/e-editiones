---
layout: page
title: Ontology Modeling
permalink: /ontology-modeling
---
## Modeling dependencies
There are a series of dependencies that directly influence the modeling of ontologies.

<!---![figure](/assets/images/ontology-dependence.png)
**Figure 1: Resources on which ontology modeling is depending**--->

Directive are the [W3C Semantic Web standard ontologies](/semantic-web-technology#w3c-semantic-web-standards).  
When modeling for a certain domain, one does not have to start from scratch. The longer the SWT is among us, the more likely someone else already created an ontology to cover the needed semantics (partially), often more generic concepts.
There is a variety of [existing ontologies](/semantic-web-technology#other-ontologies-used-in-humanities-and-publishing). Some are very generic, others are quite specific. Some have become a de facto standard, e.g. SKOS and DC Elements, or practically are, e.g. Geo.  
We have chosen the [CIDOC-CRM](http://www.cidoc-crm.org/) and [FRBRoo](http://iflastandards.info/ns/fr/frbr/frbroo/) (depending on the former) ontologies to base on. Especially using such more generic domain ontologies will enable semantic interoperability.  

<!--- the aforementioned standard and existing domain ontologies, basic modeling patterns, and best practices.--->

NIE-INE supports overall eleven projects, eight of which currently on the SWT side. Moreover, several new projects already showed their willingness to collaborate with us. The input dependency is represented by the original data model and data, mostly in XML (5 projects using often, but not always TEI), SQL (2 projects), or mixed (1 project).
Last but not least, there is a dependency on the tacit knowledge of the domain specialists in the editing projects, needed for the implementation of domain knowledge besides the restricted database models. To uncover this knowledge, a commitment on the part of domain specialists is needed, in order to reach consensus on semantics that goes beyond their own specific research objectives.

All these dependencies represent a major challenge and, initially, a substantial overhead, but the return on investment (ROI) is big, and will be even bigger the more project database models are formalized along SWT. This formalization will also contribute to the more general, cross-project semantics, preventing possibly modeling the same concepts for new projects multiple times. Reaching a wide consensus (at the best on an international scale) on domain terminology contributes to the ROI and semantic interoperability.

  
To enable data expression in this new format, a series of ontologies are created, based on those standards.  
These semantic models adhere to the [model theory of W3C RDF, RDFS](https://www.w3.org/TR/rdf-mt/), and [OWL Full](https://www.w3.org/TR/owl-semantics/), and are declared in [Turtle syntax](https://www.w3.org/TR/turtle/). They are directly accessable in the [ontology library](/ontology).  
Whenever possible [ontologies developed by others (external)](https://github.com/nie-ine/Ontologies/wiki/1.-Introduction-to-Semantic-Web-technology#other-ontologies-used-in-humanities-and-publishing) are used to base on. Local copies of such ontologies, when not available in Turtle or RDF-XML, are in the [Other-ontologies](https://github.com/nie-ine/Ontologies/tree/master/Other-ontologies) folder.  
NIE-ontologies are highly interdependent and represent a networked collection of namespaces, rather than a strongly hierarchical pyramidal structure. They differ quite in size, granularity and specificity. A basic approach is to create a namespace that can be extended easily. Rarely ontological elements will be deprecated.  
All the used ontologies are referenced in a prefix header in the Turtle files.  
A series of [basic modeling patterns](https://github.com/nie-ine/Ontologies/wiki/2.-Basic-modeling-patterns) are also published on the wiki.

There are 2 series: more general and project ontologies. The former are grosso modo further divided into four levels: 1) general domain, 2) general Humanities, 3) specific Humanities, and 4) external terminology systems ontologies (see figure 1). This division is somehow arbitrary, meaning that it isn’t formalized, but it is convenient to illustrate the articulation of ontologies and their interrelations. Table 1 shows the status of the modeling at the end of September 2019. The most populated ontologies are ‘human’, ‘information carrier’, ‘document’, ‘text’, ‘text-expression’, ‘text-structure’, ‘scholarly-editing’, ‘publishing’, ‘literature’, and ‘linguistic-morphology’. The ‘time’-ontology contains properties mainly for N3-rule declarations.

![figure](/assets/images/ontologies-network.png)
**Figure 1: A simplified representation of the e-editiones web of ontologies**

<!---![figure](/assets/images/e-editiones-ontologies_numbers.png)
**Table 1: NIE ontologies in numbers at end of June 2020**--->

## General domain ontologies
Although all ontological classes are instantiable, the more general ones will often function as “glue” to search in an RDF-database with SPARQL queries, and to enhance machine reasoning, e.g. for subsumption (subclassing). For example, if a scholar wants to search for all translations of a certain text, the property ‘is translated into’ can be used without specifying the language. In another case, one would like to find all information carriers (e.g. manuscripts and prints) bearing creations from of a certain author, but crossing more than one project: one project refers to prints existing in an archive and having a signature, and another project uses manuscripts preserved in a library with a manuscript identifier; both the manuscripts and prints can be found with a super-property ‘is on carrier’.
As a general domain ontology, the concept-ontology (see figure 7 in 'Graphics') describes for example concepts created by a person as abstract ideas, e.g. symbolic and propositional, basing on CIDOC-CRM and FRBROO. It contains entities such as ‘information’, ‘identifier’, and ‘thought-method’, and their relations to each other and to other entities, e.g. persons. The document-ontology (see also figures 1, 8, 9, and 13 in 'Graphics') describes documents, document structures, e.g. tables, identifiers and references, such as footnotes. It also contains the abstract document expression as based on FRBROO, and different relations between document structures.

## General Humanities Ontologies
The “general Humanities ontologies” comprise the core concepts for scholarly editions, as well as the bulk of entities modeled so far in agreement with the edition projects. The following is a description of five core vocabularies for scientific editing in Humanities.

### Text
This ontology describes text as a human natural language expression serialized in writeable form (see figure 11 in 'Graphics'). It contains all kinds of text forms (e.g. written, typewritten, transcribed, and printed) and roles of persons processing text (e.g. editor, annotator, and citer). It serves as basis for all text-related ontologies: text-expression, text-structure, text-editing, and literature ontology.

### Text expression
The eponymous core concept bases (via the document-ontology) on FRBROO, as text abstracted from its carrier (see Figure 9 in 'Graphics'). The ontology declares further related roles (e.g. author and commentator) and general expression types (e.g. draft and commentary). It provides the basis for the literature- and scholarly-editing-ontology.

### Text structure
This ontology describes all kinds of textual structures (see figure 13 in 'Graphics'), e.g. syntactic, compositional, content, scientific, readability. They form an upper layer to enable more flexible and extensive search, as well as machine reasoning. More specific entities are: word, sentence, paragraph, section, line, and text column. Extensions of this ontology are the note-structure- (see figure 14 in 'Graphics') and the prosodic-structure-ontology (see figure 15 in 'Graphics'), containing entities such as marginal note and gloss, and verse and strophe respectively. An important relation between structures is ‘part of’, which, by its transitive nature, enables searching and machine reasoning in a way that do not require to explicitly state all possible relations between structures in the data, since they can be inferred via transitivity.

### Text editing and Scholarly editing
Both describe the necessary semantics for editing, the latter extending the former with specific scholarly entities, e.g. diplomatic transcription, critical edition, different types of apparatus, lemma, variant, editorial comment, witness, siglum and more alike. Also related roles are declared, e.g. editor, glossator, and critical text editor. An extensive set of properties relates these entities to each other, as well as to text, text structure and expression elements (see figures 1, 9, 16, and 17 in 'Graphics').

### Publishing
This ontology describes classes and properties related to publishing, e.g. publication and its subclasses, e.g. printed and web publication, serial like newspaper, periodical, or magazine. There is a substantial set of properties relating expressions and other entities to elements in this ontology.

### Literature
This ontology describes literary genres such as narrative and different kinds of poetry, and further different types of literary expressions (e.g. poem, hymn, novel) and their subclasses. It also contains related roles, e.g. poet and novelist. Different types of literary structures are declared, e.g. foreword, preface, prologue, and epilogue, and related properties (see figures 1, 9, 21, and 22 in 'Graphics').

## Specific Humanities ontologies
This series comprises more specific entities as used in different specialized domains in the Humanities, e.g. about scholasticism. Some ontologies are an onset (e.g. ‘indology’, ‘catholic organization’ and ‘philosophy’), providing the more general concepts as needed for the current projects, but they will be extended. ‘Catholic orders’ and ‘philosophies’ describe subclasses of classes in aforementioned ontologies, also to be extended.
Although the scope of these ontologies is narrower, i.e. more project-oriented, the entities can be reused in another context, if applicable, meaning that they do not need to be restricted to a specific project.

## External terminology systems ontology
This ontology contains formal descriptions of datatypes, functioning as link between terminology or coding systems, and OWL ontologies. Such coding systems in the Humanities are general ISO1 standards (e.g. for languages), more specific ISO standards such as OAIS2, and GND3 for the DACH countries. It is also planned to use SKOS schemes and properties for this purpose in the near future.

## Project ontologies
These ontologies contain entities linked to the specific subjects of the projects, but they are still usable outside the respective projects, if applicable. For example, another national or international project about a same author could reuse some elements in order to be linkable with one of the projects supported by NIE-INE. It then would be possible to query the two different SPARQL endpoints simultaneously, which is essential for research since the triple stores can contain complementary information on the same subject. This is actually the case for the DRCS project, a project dealing with the commentaries on the Sentences of Peter Lombard, which is linked to another project of the University of Baltimore, U.S.. This case demonstrates the added value of semantic interoperability between disparate databases, facilitated by the use of the same external ontologies CIDOC-CRM and FRBROO.