---
layout: page
title: Semantic Web Technology
permalink: /semantic-web-technology

---

## Data and their semantics for humans and machines:
In general most human activities, both professionally and leisurely, produce an ever faster growing amount of very heterogeneous digital data. Also the number and kind of users communicating these data grows steadily, implying a more complex multidisciplinary information landscape. This leads to an increased need for the interoperability of computer systems to enable data exchange, and therefore for a different paradigm in the way digital data are processed. There is an (r)evolution going on wherein a transition from human to **machine interpretation** of data takes place, leading to more capable systems using the knowledge and experience of many people.

### Heterogeneity of digital data:
Humans have developed more than 7800 natural **languages**, each of them with more or less own interpretation/description models of the observation of reality. Even when different languages belong to the same group, a 1-1 translation is often impossible.  
**Terminologies** differ between domains in education, occupation, industry, etc. But also intra-disciplinary terms not always mean the same thing.  
A lot of data are **little or not structured** (free text). In order to be machine-interpretable these data need to be structured. This can be done secondarily by technology that can parse free text. But a more reliable approach is to primarily create an environment where information is sufficiently structured.  
Last but not least **databases**, even containing very similar information, can differ substantially in schemes (information models), and not really representing domain knowledge, in a way it is found in literature, let alone as existing in the heads of domain specialists.

### What do we - and machines - need?
In order to cope with the amount, heterogeneity and especially the communication of information, the latter needs to be expressed in a format that makes their **semantics machine interpretable**, in other words explicit and unified, independent of natural languages. **Explicit** means automated disambiguation or having least hidden assumptions. **Unified** means bearing one or more standards of terminology, reaching a certain level of consensus of the semantics of domain knowledge, expressed in formal vocabularies or ontologies. These information features will enhance data quality assurance, data management, (semi-)automatic data integration, data comparison, analysis, mining, and, together with probability theory, will enable decision support.

## Semantic Web technology:
The [World Wide Web Consortium (W3C)](https://www.w3.org/) is an international organization occupied with standardization of the technology driving the Web, e.g. HTML and XML. In 2001 W3C started the Semantic Web initiative aka Web 3.0. The basic idea, already envisioned by Tim Berners-Lee in 1990, is to enhance the interoperability of computer systems through the introduction of machine interpretable or formal semantics of natural language. Basic elements of the Semantic Web technology are 3 languages with increasing expressiveness: Resource Description Framework (RDF), RDF Schema (RDFS) and Web Ontology Language (OWL). They are based on logic and math (first order predicate logic, model theory and set theory). The languages have their own vocabularies or ontologies wherein their semantic elements are declared. Data of any kind, of every knowledge domain, can be expressed in these languages, requiring extension of the very basic semantics by declaring domain-specific ontologies.

## Other Ontologies used in Humanities and Publishing:
- Generic ontologies:
	- Dublin Core (DC)
		- [DC Elements](http://dublincore.org/documents/2012/06/14/dces/)
		- [DC Terms](http://purl.org/dc/terms/)
	- [Friend of a Friend (FOAF)](http://xmlns.com/foaf/0.1/)
	- [Countries](http://eulersharp.sourceforge.net/2003/03swap/countries#)
	- [Place (coordinated)](http://www.w3.org/2003/01/geo/wgs84_pos#)
- Humanities domain ontologies:
	- [CIDOC Conceptual Reference Model (CRM)](http://www.cidoc-crm.org/)
	- [Functional Requirements for Bibliographic Records, Object Oriented (FRBROO)](http://iflastandards.info/ns/fr/frbr/frbroo/)
        - [Scholastic Commentaries and Text Archive ontology (SCTA)](https://github.com/scta/scta-ontology/blob/master/SCTAOntologySpec.md)
	- [Semantic Publishing and Referencing (SPAR)](http://www.sparontologies.net/)
		- [FRBR-aligned Bibliographic Ontology (FaBiO)](http://www.sparontologies.net/ontologies/fabio)
		- [Citation Typing Ontology (CiTO)](http://purl.org/spar/cito)
		- [Bibliographic Reference Ontology (BiRO)](http://www.sparontologies.net/ontologies/biro)
		- [Document Components Ontology (DoCO)](http://www.sparontologies.net/ontologies/doco)
		- [Essential FRBR in OWL2 DL Ontology (FRBR DL)](http://www.sparontologies.net/ontologies/frbr)
		- [Document Elements Ontology (DEO)](http://www.sparontologies.net/ontologies/deo)
	- [International Council on Archives Records in Contexts Ontology (ICA RiC-O) version 0.1](https://www.ica.org/standards/RiC/RiC-O_v0-1.html)