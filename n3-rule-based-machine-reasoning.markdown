---
layout: page
title: N3-rule-based Machine Reasoning
permalink: /n3-rule-based-machine-reasoning
---
* 
{:toc}

## The semantics in the machine
Once having domain ontologies as formal dictionaries and RDF-data expressed by them, a machine can interpret their semantics thanks to the built-in logic of the formal standard languages in which the ontologies and data are expressed.  
A machine reasoner is software that has basic built-in functionality and needs **inference units or rules** to derive new data from existing data, consuming ontologies, data and other rules.  
Built-in functions are for instance mathematical (e.g. addition and subtraction), and logical operations (e.g. implication), and others like string manipulation.  
A short description of the [advantages](/semantic-web-technology-advantages#machine-reasoning) of machine reasoning (MR) is in the SWT part.  
Basic rules, e.g. for model-theoretic inference (e.g. for subsumption or transitivity), or temporal reasoning, can come with a reasoner or have to be created or reused from other developers. Rules for processing own domain data have to be developed.
Rules are expressed in the [Notation 3 language](/semantic-web-technology-introduction#notation-3-language), hence called N3-rules.  
Also rules are declared by using domain ontologies, but also external ontologies providing specific properties to invoke the built-in functions fo the reasoner.  

The following namespaces contain general external ontologies for N3-rule declaration:  
	<http://www.w3.org/2000/10/swap/string#>  
	<http://www.w3.org/2000/10/swap/list#>  
	<http://www.w3.org/2000/10/swap/log#>  
	<http://www.w3.org/2000/10/swap/math#>  
	<http://www.w3.org/2000/10/swap/crypto#>  
	<http://eulersharp.sourceforge.net/2003/03swap/log-rules#>  
	<http://eulersharp.sourceforge.net/2003/03swap/xsd-rules#>  


They provide class and property declarations for built-ins representing an extensive variety of functionalities.  
These built-ins are mentioned in some of the following rule examples.

## N3-rules serve different purposes: 
Note: also mentioned in the use case catalogue.
### Implementation of the RDF model theory:
A set of [N3-rules implementing the RDF model theory](https://github.com/josd/eye/tree/master/reasoning/rpo) permits to infer data from data based on the built-in logic of the W3C Semantic Web standard languages.
Examples are rules for the implementation of:

```
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix owl: <http://www.w3.org/2002/07/owl#>.

	rdfs:subClassOf
	rdfs:subPropertyOf
	owl:TransitiveProperty
	owl:disjointWith
	owl:oneOf
	owl:unionOf
	owl:disjointUnionOf
	owl:propertyChainAxiom
```

A complete reasoning example on transitivity for the 'is part of' property for text and text structures as prosodic entities is given in the repository, also involving a series of other RDFS- and OWL-rules. The data and query files are commented.

### Consistency check for user defined restrictions:
User-defined restrictions can be checked upon, e.g. a cardinality restriction for the object value of a certain property of a certain subject class instance. Figure 1 shows part of the 'human' class declaration in Turtle with a cardinality restriction of maximum 1 on the property 'has biological sex', IOW a human can only have exactly 1 biological sex, i.e. female, male or intersexual (see [human-ontology](https://github.com/nie-ine/Ontologies/blob/master/Nie-ontologies/Generic-ontologies/human.ttl)).

```
@prefix human: <http://www.e-editiones.ch/ontology/human#>.

	human:Human rdfs:subClassOf [
		a owl:Restriction;
		owl:onProperty human:hasBiologicalSex;
		owl:maxCardinality "1"^^xs:nonNegativeInteger].
```
**Figure 1: Class declaration with a cardinality restriction of maximum 1**

A reasoning example on cardinality is given in the repository, using 2 external ontologies and an RDF data set on images of the [Knora server application](https://www.knora.org/), developed by the [DHLab (DHL)](https://dhlab.philhist.unibas.ch/en/home/) at the University of Basel and the [Data and Service Center for humanities (DaSCH)](https://dasch.swiss/).

### Temporal reasoning:
This type of reasoning is crucial for formal data to be reusable and interchangeable, because its first step is a unification of time expressions in different calendars and/or with different accuracy.  
Time expressions with the accuracy of a day (date) from different calendars are converted to the respective Julian Day Numbers, and in this way comparable.  
A time expression with less accuracy than a day, i.e. a year or year-month, is converted to the period with the start and end date of the specific calendar, and with the start and end Julian Day Number.
For this process the machine reasoner provides an extensive set of [Time and RIF Built-ins](https://raw.githubusercontent.com/josd/eye/master/eye-builtins.n3) based on W3C standards [RIF Datatypes and Built-Ins 1.0](https://www.w3.org/TR/2013/REC-rif-dtb-20130205/), using for instance literals typed with e.g. xsd:date, xsd:dateTime, and xsd:duration from the <http://www.w3.org/2001/XMLSchema#> namespace.
Further functionality is provided by the [time-ontology](https://github.com/nie-ine/Ontologies/blob/master/Nie-ontologies/Generic-ontologies/time.ttl), and the [calendar-ontology](https://github.com/nie-ine/Ontologies/blob/master/Nie-ontologies/Generic-ontologies/calendar.ttl), declaring the properties used in N3-rules.

A temporal reasoning example is given in the repository, converting calendrical time expressions to a unifying Julian Day Number.  
Another example deals with an event without a start or end date, with the specific example of missing birth- or death date.

### Miscellaneous functionalities and calculations:
Also for this type of N3-rules a large set of [built-ins](https://raw.githubusercontent.com/josd/eye/master/eye-builtins.n3) is available, dealing with e.g. logical and mathematical operators, lists, and strings.
For example string manipulation, e.g. parsing using regular expressions, is possible with formal expressions, offering the advantage of staying in the formal N3/RDF environment until a fully reasoned upon data set or deductive closure is obtained, which can be stored in an RDF database and queried with SPARQL, or which can be transformed to JSON(-LD) for GUI application.  

The repository contains a reasoning example on sequence numbers or ordinals, derived from entity identifiers, using following properties declared in the respective ontology:

```
@prefix math: <http://www.e-editiones.ch/ontology/mathematics#>.

	math:hasOrdinalLiteral  
	math:hasOrdinalNumeral  
```

and a set of rules that can be made as general as possible, but very likely only within a certain project, considering the numerous possible combinations in creating alphanumeric identifiers.

## Machine Reasoner EYE (Euler Yet another proof Engine):
See also [Verborg and De Roo 2015](/literature).  
[Development](https://github.com/josd/eye)  
[Download](https://sourceforge.net/projects/eulersharp/files/eulersharp/)  
<!---http://eulersharp.sourceforge.net/2003/03swap/eye-owl2.html--->
EYE comes with syntax check and intrinsic functionality provided by [built-ins](https://raw.githubusercontent.com/josd/eye/master/eye-builtins.n3).  
All other reasoning material has to be input, i.e. OWL-ontologies, RDF-data, N3-rules.  

## Basic command example for EYE:

Note: the command for the reasoner is written for Unix OS, but can be easily converted for Windows OS.

```
eye                      # call the machine reasoner  
                         # one or more options can be used, e.g.  
--nope                   # option for output without a proof
--traditional            # option for N3 syntax, e.g. @prefix instead of PREFIX  
                         # local or remote references can be added to assert ontology-, data, or rule graphs:  
.../rdf-data.ttl         # ref. to one or more RDF data sets expressed in Turtle syntax (.ttl, subset of N3); .ttl can be replaced by .n3  
.../owl-ontology.ttl     # ref. to one or more OWL ontologies expressed in OWL Full or lesser sublanguage, using all possible elements of RDF/S-OWL ontologies  
.../rule.n3              # ref. to one or more N3-rules; EYE is a 'stateless' reasoner, meaning that all inferencing formalisms have to be fed to it  
                         # output as a pass OR an N3-query:  
--pass                   # output deductive closure: all the stated and inferred triples except the rules 
--pass-all               # output deductive closure plus rules  
--query                  # output filtered with N3-query  
>                        # output can be written to a file
.../result.n3            # result file
```
