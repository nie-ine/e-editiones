---
layout: page
title: Advantages of Semantic Web Technology
permalink: /semantic-web-technology-advantages

---
* 
{:toc}

The advantages of implementing SWT or 'RDF-izing data' (as *pars pro toto*) are multifold.
## Independent from natural language through its formalization
Having a formal lingua franca, the aforementioned unifying standard language of logic, the **meaning of concepts becomes natural language independent**. Of course this also implies that in the modeling process of the concepts there needs to be a minimal international concensus between domain specialists speaking different languages.
Unifying formal semantics directly leads to **semantic interoperability** and also makes cross-project **data comparison** possible.
## Conceptual enrichment by merging natural languages
Since there are natural language specific concepts only existing in 1 language or languages of the same group, a formal vocabulary means a conceptual enrichment compaired to a domain specialist's natural language. At the end different domain specialists will mutually benefit from each other using formal vocabularies based on different natural languages.  
Similarly there will be a conceptual enrichment **between different domains of discours** in the same natural language, e.g. between different scientific domains, or a scientific and industrial domain, and even between different groups within the same domain.  
## Explicit data models and quality control
For a machine to deal with formal semantics all intended **meaning has to be stated explicitly** (no hidden assumtions). In first instance this can be confronting for a researcher, realizing that own data are not transparent and bearing some gaps, only well understood by the creator(s) of the data model(s). This need for explicitness creates a **quality control feedback loop for the source data model and data**.  
More transparant data models also lead to **easier data management**, less depending on specific persons. In this context it is worthwhile to mention that OWL-ontologies are self-describing formal vocabularies, by means of the human oriented labels and comments (definitions) of ontological elements, and documentation in queries and rules.
## Reusable consented domain knowledge
From a pure content point of view domain knowledge becomes highly exchangeable and reusable through expression in formal domain ontologies and N3-rules.
## Machine-interpretable semantics
The built-in logic of the W3C SW standards makes the semantics machine-interpretable enabling **semi-automated semantic interoperability**. Semi because to add new knowledge human intervention is still mostly needed.
The biggest advantage is [**machine reasoning**](/n3-rule-based-machine-reasoning), to make inferences of all kinds. For example simpler semantics expressed with a source data model can be converted to more complex semantics expressed with domain ontologies ([two-step formalization](/two-step-formalization)). Ex. Data automatedly enriched with domain knowledge.

<!---The advantages of SWT are summerized in Table 1.  
- Formal Semantics:
	- Natural language independent ← unifying standard language of logic
	- Unified → semantic interoperability, data comparison
	- Conceptual enrichment
	- Explicit → data and model quality control feedback loop → data management
	- Domain knowledge expressed in reusable consented ontologies and N3-rules
	- Machine-interpretable ← unifying standard language of logic
		→ semi-automated semantic interoperability  
		→ machine reasoning  
		→ semantic conversion of data models ([2-step formalization](/two-step-formalization))  
		→ enrich data; analysis, mining, and, together with probability theory, enable decision support  

{% include image.html type="small-figure" url="/assets/images/advantages-of-swt.png" description="Table 1: Advantages of SWT" %}

° added value of RDF: e.g. no relation HDC and first publication in source data : adding relations between concepts ° Pre-processing year literals at conversion:--->