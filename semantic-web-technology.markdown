---
layout: page
title: Semantic Web Technology
permalink: /semantic-web-technology

---
## Heterogeneity of digital data
In general a growing number of people produce in their activities, both professionally and leisurely, an ever faster growing amount of very heterogeneous digital data, resulting in a very complex information landscape.  
This heterogeneity has several causes.  
Humans have developed more than 7800 **natural languages**, each of them with more or less own interpretation and description models of the observation of reality. Even when different languages belong to the same group, a 1-1 translation is often impossible.  
Within a language, the way people describe things with a certain vocabulary or **terminology** or jargon differs along education, occupation, industry and other domains. But also intra-disciplinary terms not always bear exactly the same meaning.  
On the technological side, a lot of data are **little or not structured** (free text). One can secondarily structure data through parsing the text, but unless the accuracy of text recognition is 100%, a secondary data error is introduced. Creating possibilities to up-front input sufficiently structured data might be an easier, cheaper and more reliable approach.  
Last but not least, even when data input is structured in databases (e.g. in XML or SQL), and even when 2 databases contain very similar information, their schemas or **data models**, though capturing consented domain knowledge (as found in literature, or in tacit knowledge in the heads of domain specialists) are often **localized** through natural language and personal representations such as abbreviations and cryptic naming, not fully described. In other words they are not always stating meaning explicitly.

## Data and their semantics for humans and machines
In order to communicate the growing amount of heterogeneous information, humans need another paradigm of the interoperability of computer systems to enable enhanced data linkability. Hyperlinking identified resources on the Web, e.g. a wiki-page or an application, is only one part of the story. Going to the content of the pages, the meaning of every resource, e.g. a document, a subject, an image, has to be known, i.e. described, in a way a machine can handle it, in order to be really linkable in an automated way.  
This paradigm emerges as a **unifying standard language** to express the information's semantics in such a way that it solves the aformentioned issues.  
It is a tremendous advantage to escape from natural language translations and have a language with more basic semantics of logic and mathematics. It permits structuring information in a database with explicitly stated data models. And even as a standard, it will enable also the expression of subtle differences in terminologies, instead of needing to make the information landscape less complex by simplifying its semantics. The biggest advantage of such a unifying language of logic is making its **semantics machine interpretable**, because this enables formal logic inference with machine reasoning. With this kind of artificial intelligence, new knowledge can be derived from existing one.

## W3C Semantic Web standards
In 1990 at the onset of the World Wide Web (WWW), Tim Berners-Lee already envisioned a unifying language of logic. But it wasn't until 2001 that the [WWW Consortium (W3C)](https://www.w3.org/) started the development of the [Semantic Web (SW)](https://www.w3.org/standards/semanticweb/) aka Web 3.0, resulting in a set of technology standards. W3C is the international organization occupied with standardization of the technology driving the Web, also e.g. HTML and XML. The SW standards enhance the interoperability of computer systems through the introduction of **machine interpretable or formal semantics** of natural language.  

Figure 1 shows the common representation of the different technologies comprised in the SW stack.   

{% include image.html type="small-figure" url="/assets/images/semantic-web-stack.png" description="Figure 1: The Semantic Web Stack" %}

The Web already comes with digital resources bearing an IRI or Internationalized Resource Identifier (URI or Uniform Resource Identifier and URL or Uniform Resource Locator are respective sub-concepts).  
The Semantic Web provides 3 languages with increasing expressiveness: [Resource Description Framework (RDF), RDF Schema (RDFS)](https://www.w3.org/TR/rdf-mt/), and the [Web Ontology Language (OWL)](https://www.w3.org/TR/owl2-primer/), which can be used seperately to express formal elements in a growing complexity, resp. data, thesauri and ontologies (or formal dictionaries).  
In our project we always use the 3 together without making such distinctions.  
The author took the liberty to slightly change the previous graphic to the one in Figure 2 to emphasize the dependency on formal logic, and place ontologies at a basic level. 

{% include image.html type="small-figure" url="/assets/images/SWT-stack-N3.png" description="Figure 2: Adapted Semantic Web Stack featuring N3" %}

The figure shows the 3 foundational ontologies of the 3 languages themselves together as the basis, arguing that even for the simplest data expression the [RDF-ontology](http://www.w3.org/1999/02/22-rdf-syntax-ns#) is needed. Once declaring domain knowledge in [own ontologies](/ontologies), also elements of the [RDFS-](http://www.w3.org/2000/01/rdf-schema#) and [OWL-ontology](http://www.w3.org/2002/07/owl#) are needed.  
The next layer represents the formal data expressed using the ontologies.  
Ontologies and data can be serialized in [Turtle](https://www.w3.org/TR/turtle/), [RDF/XML](), or [N-Triples](https://www.w3.org/TR/n-triples/) syntax.  
[SPARQL](https://www.w3.org/TR/rdf-sparql-query/) is the RDF query language, to retrieve data from an RDF graph database or triple store. It has its own syntax.  
Rules are the means for inferring new data from data with machine reasoning.  
All these layers are embedded in the logic layer. More precisely the languages (except SPARQL) have their model (or interpretation) theory based on first order predicate logic and set theory (math).  
The [Notation 3 language (N3)](https://www.w3.org/TeamSubmission/n3/) is an overarching language and still a Team Submission, i.e. not a standard (or recommendation) yet. Besides ontologies and data, it permits the declaration of inference rules and queries, as "end-rule" (see also [N3-rule-based machine reasoning](/n3-rule-based-machine-reasoning)). As such Turtle is a sublanguage of N3.  

Note: there is a W3C N3-dev working group (of which T. Berners-Lee, Jod De Roo, the developer of the EYE reasoner, and Hans Cools, the author, are members) to further develop N3 and bring it to a possible standard.

## Advantages of SWT
- Semantics:
	- Natural language independent
	- Explicit → data and model quality control feedback loop → data management, comparison
	- Unified → linkable → semantic interoperability  
	- domain knowledge expressed in reusable consented ontologies and N3-rules  
	- Machine-interpretable  
		→ semi-automated semantic interoperability  
		→ machine reasoning  
		→ semantic conversion of data models ([2-step formalization](/two-step-formalization))  
		→ enrich data; analysis, mining, and, together with probability theory, enable decision support  

<!--- ° added value of RDF: e.g. no relation HDC and first publication in source data : adding relations between concepts ° Pre-processing year literals at conversion:--->

## Other Ontologies used in Humanities and Publishing
Note: not meant to be exhaustive.
- Generic ontologies:
	- [Simple Knowledge Organization System (SKOS)](https://www.w3.org/2009/08/skos-reference/skos.html)
	- Dublin Core (DC)
		- [DC Elements](http://dublincore.org/documents/2012/06/14/dces/)
		- [DC Terms](http://purl.org/dc/terms/)
	- [Place (coordinated): Geo (WGS84) Vocabulary](http://www.w3.org/2003/01/geo/wgs84_pos#)
	- [Friend of a Friend (FOAF)](http://xmlns.com/foaf/0.1/)
	- [Countries](http://eulersharp.sourceforge.net/2003/03swap/countries#)
- Natural science ontologies: also used in Humanities
	- [The Semantic Web for Earth and Environmental Terminology (SWEET) Ontologies](https://github.com/ESIPFed/sweet)
- Humanities domain ontologies:
	- [CIDOC Conceptual Reference Model (CRM)](http://www.cidoc-crm.org/)
	- [Functional Requirements for Bibliographic Records, Object Oriented (FRBRoo)](http://iflastandards.info/ns/fr/frbr/frbroo/)
        - [Scholastic Commentaries and Text Archive ontology (SCTA)](https://github.com/scta/scta-ontology/blob/master/SCTAOntologySpec.md)
	- [Semantic Publishing and Referencing (SPAR)](http://www.sparontologies.net/)
		- [FRBR-aligned Bibliographic Ontology (FaBiO)](http://www.sparontologies.net/ontologies/fabio)
		- [Citation Typing Ontology (CiTO)](http://purl.org/spar/cito)
		- [Bibliographic Reference Ontology (BiRO)](http://www.sparontologies.net/ontologies/biro)
		- [Document Components Ontology (DoCO)](http://www.sparontologies.net/ontologies/doco)
		- [Essential FRBR in OWL2 DL Ontology (FRBR DL)](http://www.sparontologies.net/ontologies/frbr)
		- [Document Elements Ontology (DEO)](http://www.sparontologies.net/ontologies/deo)
	- [International Council on Archives Records in Contexts Ontology (ICA RiC-O) version 0.1](https://www.ica.org/standards/RiC/RiC-O_v0-1.html)

Hans Cools
NIE-INE