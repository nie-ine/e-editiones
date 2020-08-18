---
layout: page
title: Introduction to Semantic Web Technology
permalink: /semantic-web-technology-introduction

---
* 
{:toc}

## Heterogeneity of digital data
In general a growing number of people produce in their activities, both professionally and leisurely, an ever faster growing amount of very heterogeneous digital data, resulting in a very complex information landscape.  
This heterogeneity has several causes.  
Humans have developed more than 7800 **natural languages**, each of them with more or less own interpretation and description models of the human observation of reality. Even when different languages belong to the same group, a 1-1 translation is often impossible.  
Within a language, the way people describe things with a certain vocabulary or **terminology** or jargon differs along education, science, occupation, industry and other **domains**. But also intra-disciplinary terms not always bear exactly the same meaning.  
On the technological side, a lot of data are **little or not structured** (free text). One can secondarily structure data through parsing the text, but unless the accuracy of text recognition is 100%, a secondary data error is introduced. Creating possibilities to up-front input sufficiently structured data might be an easier, cheaper and more reliable approach.  
Last but not least, even when data input is structured in databases (e.g. in XML or SQL), and even when 2 databases contain very similar information, their schemas or **data models**, though capturing consented domain knowledge (as found in literature, or in tacit knowledge in the heads of domain specialists) are often **localized** through natural language and personal representations such as abbreviations and cryptic naming, not fully described. In other words they are not always stating meaning explicitly.  

## Data and their semantics for humans and machines
In order to communicate the growing amount of heterogeneous information, humans need another paradigm of the interoperability of computer systems to enable enhanced data linkability. Hyperlinking identified resources on the Web, e.g. a wiki-page or an application, is only one part of the story. Going to the content of the pages, the meaning of every resource, e.g. a document, a subject, an image, has to be known, i.e. described, in a way a machine can handle it, in order to be really linkable in an automated way.  
This paradigm emerges as a **unifying standard language of logic** to express the information's semantics in such a way that it solves the aforementioned issues.  
It is a tremendous advantage to escape from natural language translations and have a language with more basic semantics of logic and mathematics. It permits structuring information in a database with explicitly stated data models. And even as a standard, it will enable also the expression of subtle differences in terminologies, instead of needing to make the information landscape less complex by simplifying its semantics. The biggest advantage of such a language of logic is making its **semantics machine interpretable**, because this enables formal logic inference with machine reasoning. With this kind of artificial intelligence, new knowledge can be derived from existing one.  

## W3C Semantic Web standards
In 1990 at the onset of the World Wide Web (WWW), Tim Berners-Lee already envisioned a unifying language of logic. But it wasn't until 2001 that the [WWW Consortium (W3C)](https://www.w3.org/) started the development of the [Semantic Web (SW)](https://www.w3.org/standards/semanticweb/) aka Web 3.0, resulting in a set of open source technology standards. W3C is the international organization occupied with standardization of the technology driving the Web, also e.g. HTML and XML.  
The SW standards enhance the interoperability of computer systems through the introduction of **machine interpretable or formal semantics** of natural language.  
For clarity it has to be said that the novel element in the SW is not the semantics, but the Web. First there was natural language and its semantics for  milennia, and later on logics of all kinds. Then there was Information Technology, the Internet connecting computers, and the Web connecting pages, documents and applications. And finally the SW environment with its standards is able to formalize the semantics of natural language and make it machine interpretable, which enables linking information resources in a meaningful way.

Figure 1 shows the common representation of the different technologies with their respective standards comprised in the SW stack.   

{% include image.html type="small-figure" url="/assets/images/semantic-web-stack.png" description="Figure 1: The Semantic Web Stack" %}

### Identify: IRI
The Web already comes with digital resources bearing an IRI or Internationalized Resource Identifier (URI or Uniform Resource Identifier and URL or Uniform Resource Locator are respective sub-concepts). So, it is already good to know what resource an agent—person or machine—is speaking about because the former is identified, and if another agent looks for it, it can find it (if accessible).  
The next step is for the other agent—again person or machine—to understand what the resource is about. The fact that also the machine 'understands' content is the game changer. Therefore it needs explicit formal semantics based on logic. More precisely the different standard languages (except SPARQL) have their [model (or interpretation) theory](https://en.wikipedia.org/wiki/Model_theory) based on [first order logic](https://en.wikipedia.org/wiki/First-order_logic) and [set theory](https://en.wikipedia.org/wiki/Set_theory).

### Formalize data, data models, and domain knowledge: languages of logic
Those languages are [Resource Description Framework (RDF), RDF Schema (RDFS)](https://www.w3.org/TR/rdf-mt/), and the [Web Ontology Language (OWL)](https://www.w3.org/TR/owl2-primer/), having an increasing expressiveness, i.e. they can be used separately to express formal statements in a growing complexity.  
RDF enables mere data expression, without declaring a model. RDFS already permits modeling a simple ontology, and OWL is meant for the declaration of a more complex ontology (or formal dictionary).  
OWL itself has different grades of expressiveness with [OWL 2 DL, OWL 2 Full](https://www.w3.org/TR/owl2-primer/#OWL_2_DL_and_OWL_2_Full) and [profiles](https://www.w3.org/TR/owl2-primer/#OWL_2_Profiles) as discussed in the W3C document. We use OWL 2 Full.  
Some descriptions of 'ontology' in the SW are: "a conceptualization of a domain to enable knowledge sharing" ([W3C 2009](https://www.w3.org/2005/Incubator/w3pm/XGR-w3pm-20091008/#A)) and "a representation of terms and their interrelationships" ([W3C 2004](https://www.w3.org/TR/2004/REC-owl-features-20040210/#s1)).  
Ontologies and data can be serialized in [Turtle](https://www.w3.org/TR/turtle/), [RDF/XML](https://www.w3.org/TR/rdf-syntax-grammar/), or [N-Triples](https://www.w3.org/TR/n-triples/) syntax.

### Query: SPARQL
[SPARQL](https://www.w3.org/TR/rdf-sparql-query/) is the RDF query language, to retrieve data from an RDF graph database or triple store. It has its own syntax.  
We use the open source [Apache Jena Fuseki SPARQL server](https://jena.apache.org/documentation/fuseki2/).

<!---link to SPARQL microservice with Jena-Fuseki-TDB2--->

### Formalize the means to infer: rule
Rules are the means for inferring new data from data with machine reasoning. The [Rule Interchange Format (RIF) Datatypes and Built-Ins 1.0](https://www.w3.org/TR/rif-dtb/) contains standard specifications.  

### Infer: unifying logic and machine reasoning
Unifying logic establishes consistency and correctness of data sets and permits to infer conclusions not explicitly stated but required by or consistent with a known set of data, by applying the rules using a machine reasoner having the logic implemented.  

### Proof: machine reasoning
Proof provides trace or explanation of the steps of logical reasoning and needs to be given by the reasoner.  

### Trust
A trust layer offers authentication of identity and evidence of the trustworthiness of data, services, and agents.  
All but the last layer subjects are further discussed in separate sections.  

### Focus on logic and machine reasoning
The author took the liberty to slightly change the previous graphic to the one in Figure 2 to emphasize the dependency on formal logic, and place ontologies at a basic level. 

{% include image.html type="small-figure" url="/assets/images/SWT-stack-N3.png" description="Figure 2: Adapted Semantic Web Stack featuring N3" %}

We always use RDF, RDFS, and OWL together without making the aforementioned distinctions. The figure shows the foundational ontologies of the 3 languages themselves together as the basis, arguing that even for the simplest data expression the [RDF-ontology](http://www.w3.org/1999/02/22-rdf-syntax-ns#) is needed. Once declaring domain knowledge in [own ontologies](/_includes/ontologies), also elements of the [RDFS-](http://www.w3.org/2000/01/rdf-schema#) and [OWL-ontology](http://www.w3.org/2002/07/owl#) are needed.  
From a formal model point of view we can describe an ontology further as a collection of classes (or sets, categories) and properties (or relations, predicates)  between instances (individuals) of classes.
The next layer represents the formal data expressed using the ontologies.  

### Notation 3 language
[Notation 3 (N3)](https://www.w3.org/TeamSubmission/n3/) is an assertion and logic language which is a superset of RDF, and still a Team Submission, i.e. not a standard (or recommendation) yet. N3 extends the RDF datamodel by adding formulae (literals which are graphs themselves), variables, logical implication ('if...then'; =>), and functional predicates, as well as providing a textual syntax (alternative to RDF/XML). Besides ontologies and data, it permits the declaration of inference N3-rules and N3-queries (see also [N3-rule-based machine reasoning](/n3-rule-based-machine-reasoning)). In this way Turtle is a subset of N3.  

Note: there is a W3C N3-dev working group (of which e.g. T. Berners-Lee, Jos De Roo, the developer of the EYE reasoner, and Hans Cools, the author, are members) to further develop N3 and bring it to a possible standard.

## A reflection
Implementing the SW standards or *RDF-izing* data (as *pars pro toto*) just for (long-term) data storage is not that fruitful. RDF is not 'yet another data format'. To create and/or reuse the necessary ontologies to formalize data is an investment that often meets misunderstanding and reluctance. RDF is not suitable for very quick ad hoc development, but aims at a fundamentally different data processing of which the translation of source data into RDF is only the beginning. Of course development complexity and time depend on the needed semantics to express data and solve academic, industrial or other data flow and research issues. On one hand an existing ontology can suffice and a limited set of rules can solve the issues. On the other hand a library of new ontologies (mostly basing on existing ones) has to be created and a series of rules sets has to be developed providing very different functionalities to solve all kinds of issues, as is the case in our environment.  
If modeling the needed domain semantics is not your cup of tea (it can be pretty time-consuming) you can try to learn it by adopting certain best practices and efficiency or leave it to people who are interested in this kind of work. It is a kind of job covering different aspects: semiotics, linguistics, formal logic, math, analysis, an eye for detail but also keeping an overview, participation in conceptual discussions with domain specialists, and very iterative, possibly taking a while until satisfying.  
There are people in the RDF community that want SWT to be more digestible for 'the average IT developer'. This should not be translated into ad hoc usage of the W3C standards, deviating from the original goals of the Semantic Web. Semantic interoperability and machine reasoning should be at all time be preserved.

## Domain ontologies used in Humanities and Publishing
Note: not meant to be exhaustive.
- Generic ontologies:
	- [Simple Knowledge Organization System (SKOS)](https://www.w3.org/2009/08/skos-reference/skos.html)
	- Dublin Core (DC)
		- [DC Elements](http://dublincore.org/documents/2012/06/14/dces/)
		- [DC Terms](http://purl.org/dc/terms/)
	- [Place (coordinated): Geo (WGS84) Vocabulary](http://www.w3.org/2003/01/geo/wgs84_pos#)
	- [Friend of a Friend (FOAF)](http://xmlns.com/foaf/0.1/)
	- [Schema.org](http://schema.org/)
	- [Countries](http://eulersharp.sourceforge.net/2003/03swap/countries#)
- Natural science ontologies: also used in Humanities
	- [The Semantic Web for Earth and Environmental Terminology (SWEET) Ontologies](https://github.com/ESIPFed/sweet)
- Humanities domain ontologies:
	- [CIDOC Conceptual Reference Model (CRM)](http://www.cidoc-crm.org/get-last-official-release)
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