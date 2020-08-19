---
layout: page
title: Advantages of Semantic Web Technology
permalink: /semantic-web-technology-advantages

---
* 
{:toc}

The advantages of implementing SWT with formal semantics are multifold.
## Independence from natural language
Translating data models and data into a formal lingua franca, i.e. the unifying standard language of logic mentioned in the introduction, the **meaning of concepts becomes natural language independent**. Of course this also implies that in the modeling process of the concepts there needs to be a minimal international concensus between domain specialists speaking different languages.
**Unifying** formal semantics directly leads to **semantic interoperability** and also makes **data** from different sources **comparable**.
## Conceptual enrichment by merging natural languages
Since there are natural language specific concepts only existing in 1 language or languages of the same group, a formal vocabulary means a conceptual enrichment compaired to a domain specialist's natural language. At the end different domain specialists will mutually benefit from each other using formal vocabularies based on different natural languages.  
Similarly there will be a conceptual enrichment **between different domains of discours** in the same natural language, e.g. between different scientific domains, or a scientific and industrial domain, and even between different groups within the same domain.  
## Explicit data models
For a machine to deal with formal semantics all intended **meaning has to be stated explicitly** (no hidden assumtions). In first instance this can be confronting for a researcher, realizing that own data are not transparent and bearing some gaps, only well understood by the creator(s) of the data model(s).
### Quality control
This need for explicitness creates a **quality control feedback loop for the source data model and data**.
### Easier data management
More transparant data models also lead to **easier data management**, less depending on specific persons. In this context it is worthwhile to mention that OWL-ontologies are self-describing formal vocabularies, by means of the human oriented labels and comments (definitions) of ontological elements, and documentation in queries and rules.
## Reusable consented domain knowledge
From a pure content point of view domain knowledge becomes highly exchangeable and reusable through expression in formal domain ontologies and N3-rules.
## Machine-interpretable semantics
The built-in logic of the W3C SW standards makes the semantics machine-interpretable enabling automated semantic interoperability and machine reasoning.
### Automated semantic interoperability
Interoperability on the semantic level is the highest, crossing the borders of natural languages and knowledge domains. This strongly enhances **data availability**, since very disparate data sources will be usable together, generating unprecedented research possibilites.
It has to be pointed out that for adding new knowledge in ontologies and rules human intervention is mostly still needed.
### Machine reasoning
The biggest advantage, building further on the previous one, is [machine reasoning](/n3-rule-based-machine-reasoning), to make inferences of all kinds by deriving new from existing data.
#### Semantic conversion and enrichment
For example data expressed with a simpler model can be in a deductive way **converted to data expressed with more complex domain ontologies** ([two-step formalization](/two-step-formalization)). Lifting a tip of the veil, a plain literal value indicating implicitly a year (e.g. "1789") can be converted to a year period of which the start and end are explicitly expressed with a datatyped literal date in the Gregorian calendar (e.g. "1789-01-01^^xsd:date" and "1789-12-31^^xsd:date"), with which can be calculated as time indicators. Also measurements of a certain quantity can be formally expressed in a certain unit (e.g. length in foot), and converted to an SI unit (e.g. meter). This other unit together with the foot-related scale factor (0.3048) is then the formal built-in domain knowledge in this case, stored in an ontology and used in an N3-rule, which can **automatedly enriched the processed data**. Such formal knowledge can also come from linked (external) RDF-data  sources.
#### Research
Rules can also be applied to analyse data, e.g. text. All kinds of research questions can be answered.
Further advanced applications are data mining and decision support, requiring implementation of probability theory (e.g. Bayesian inference).

<!---The advantages of SWT are summerized in Table 1.  
- Formal Semantics:
	- Natural language independent ← unifying standard language of logic
	- Unified → semantic interoperability → data comparison
	- Conceptual enrichment ← merging natural languages
	- Explicit → data and model quality control feedback loop → data management
	- Domain knowledge expressed in reusable consented ontologies and N3-rules
	- Machine-interpretable ← unifying standard language of logic
		→ semi-automated semantic interoperability  
		→ machine reasoning  
		→ semantic conversion of data models and enrichment of data ([2-step formalization](/two-step-formalization))  
		→ enrich data; analysis, mining, and, together with probability theory, decision support  

{% include image.html type="small-figure" url="/assets/images/advantages-of-swt.png" description="Table 1: Advantages of SWT" %}

° added value of RDF: e.g. no relation HDC and first publication in source data : adding relations between concepts ° Pre-processing year literals at conversion:--->