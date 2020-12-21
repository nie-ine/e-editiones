---
layout: page
title: About
permalink: /about
---
These web pages present the outcome of the NIE-INE-project (Nationale Infrastruktur für Editionen - Infrastructure Nationale pour les Éditions), in terms of know how, best practices, products and services.  
<!---(http://www.nie-ine.ch)--->
NIE-INE is part of the [swissuniversities'](https://www.swissuniversities.ch/en/?r=1) national program "Scientific information: Access, processing and safeguarding" and runs at the Universities of Basel, Bern and Zürich, since October 2016 and until the end of 2020.  

The project focuses on the development of two major domains:  
1) Semantic Web technologies (SWT), with the aim to allow researchers in the humanities to express their data in an enriched format adhering to the FAIR principles.
Thanks to the collaboration with many different edition projects, NIE-INE was able to define some best practices and develop different methodologies, notably the Two-Step Formalization. With this methodology original data (in XML, SQL or other formats) are converted to a different i.e. machine-interpretable format through the **end-to-end implementation of the W3C’s [Semantic Web (SW)](/semantic-web-technology-introduction) standards**, and by making the semantics of the data explicit.  
2) [inseri](http://test-nieos.nie-ine.ch/home), a web environment/framework for the online publishing and editing of scholarly editions, and more generally results produced by projects in the humanities. Inseri provides the projects with the necessary apps and visualizations, and ensures long-term storage of the data, partially by transferring those to another framework, the Data and Service Center for the humanities (DaSCH)<!---(https://dasch.swiss/)--->.

The formalization along SWT entails a series of [advantages](/semantic-web-technology-advantages), of which **semantic interoperability** is the most prominent one.  
To enable domain data expression in this new format, a series of formal dictionaries or [domain ontologies](/ontology) are developed in a [GitHub project](https://github.com/nie-ine). There are also the repositories complementary to SWT.  
The [modeling](/ontology-modeling) of these ontologies is based on W3C's standards and general ontologies for the Humanities (among them [CIDOC-CRM](http://www.cidoc-crm.org/get-last-official-release) and [FRBRoo](http://iflastandards.info/ns/fr/frbr/frbroo/)), and makes use of basic modelling patterns and a [Two-Step Formalization (2SF)](/two-step-formalization) methodology.  

The ontologies and the formal data expressed along them are used in [N3-rule-based machine reasoning](/n3-rule-based-machine-reasoning) to infer new data from existing data, increasing the research potential by bringing **new domain knowledge** through formal data analysis and data mining.    

<!---Having semantic interoperability is only the beginning of the journey and part of the return on investment.
The crux of SWT, and the other part of the ROI, is using the ontologies and the formal data expressed by them in [N3-rule-based machine reasoning](/n3-rule-based-machine-reasoning) to infer new data from existing data, bringing ultimately new domain knowledge.  ---> 

This novel way of modeling and processing data is also applicable to science outside the humanities, and other domains.

After 2020 the website will be maintained and the ontologies and rules will be further developed on GitHub.  


Hans Cools  
e-editiones.ch  
hanscoolssw@gmail.com