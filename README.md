# e-editiones

These are the files necessary to develop, build and maintain [e-editiones.ch](https://e-editiones.ch) - the website of the ontologies developed on GitHub in the repository [Ontologies](https://github.com/nie-ine/Ontologies). 

## Basic Workflow
1. Ontologies are developed as turtle files.
1. A script validates the turtle files and converts them to RDF/XML, N-Triples, and JSON-LD as well as to a human-readable HTML version.
1. The ontologies are made available through [e-editiones.ch](https://e-editiones.ch), which simply points to a GitHub Pages page provided by this repository.

## Develop, Build and Maintain Locally

### Dependencies

- [Ruby][ruby]
  - [Ruby Gems][gems]
  - [Bundler][bundler]
  - [Jekyll][jekyll]
- [Python 3][python3]
  - with the ability to create a virtual environment (e.g. [venv][venv])

### Get Started

1. Make sure you have the above listed dependencies installed.
1. Clone repository.
1. cd into repository with ``cd e-editiones``.
1. Run ``bundle install`` to fetch the needed Ruby gems.
1. cd into "ttl_conv" with ``cd ttl_conv``.
1. Set up a Python virtual environment. E.g. ``virtualenv env``
1. Activate your virtual environment. E.g. ``source env/bin/activate`` (type ``deactivate`` to deactivate).
1. Run ``pip3 install -r requirements.txt`` to fetch the needed Python packages.
1. cd back to "e-editiones" with ``cd ..``.

You should now be all set to develop, build and maintain the website locally. 

### Develop

The folder and file structure you see is based on [Jekyll][jekyll]'s needs but there are some additional non-Jekyll folders and files. Below is a quick overview of the top-level files. You might want to visit the [Jekyll Docs](https://jekyllrb.com/docs/) to see how Jekyll itself works. 

Folder/File        | Description                                
 ----------------- | -------------------------------------------
 \_includes        | Jekyll folder containing HTML building blocks. The subfolder "ontologies" contains the human-readable HTML version of each ontology.
 \_layouts         | Jekyll folder containing HTML templates.
 \_sass            | Jekyll folder containing scss stylesheets. These files are compiled to a single css file for the final static website.
 \_site            | Jekyll folder containing the static files version of the website when serving locally.
 \docs             | Custom Jekyll folder to save the built website files. 
 assets            | Jekyll folder containing asset files for the static website. 
 collections       | Jekyll folder to group content into collections. This folder is needed to group the created ontologies into "generic" and "project".
 ontology          | Custom Jekyll folder containing all the ontology files. 
 ttl_conv          | Custom folder containing a Python script and additional resources to convert turtle files into needed formats and files. 
 .gitignore        | Gitingore file.
 404.html          | 404 error page for the static website.
 \_config.yml      | Jekyll file for site-wide configurations.
 Gemfile           | Ruby file used to list the needed Ruby Gems to run Jekyll.
 Gemfile.lock      | Ruby file listing all the necessary Ruby Gem dependencies.
 index.md          | Jekyll file with the content of the Home page.
 ... .md           | Jekyll files for specific pages.
 README.md         | The very file you're reading right now.
 
#### Serve Locally

To serve the website locally, run ``bundle exec jekyll serve`` and visit [http://localhost:4000/e-editiones/](http://localhost:4000/e-editiones/).

#### Build Locally

To build the static website, run ``bundle exec jekyll build`` and all necessary files will be available in the "\docs" folder.

### Turtle File Conversion

To convert turtle files to the needed formats: 

1. Any turtle file needs to be in the "ontology" folder.
   - Be aware of the correct file naming (see [Add New Ontologies](#add-new-ontologies) below)
1. cd into "ttl_conv" with ``cd ttl_conv``.
1. Activate your virtual environment, if not activated, with ``source env/bin/activate``.
1. Run ``python3 -W ignore convert_files.py``.
   - ``-W ignore`` is optional but it ignores some default RDFlib messages.
   - The script validates available turtle files and stops with error messages if there are invalid files.
   - If there are no errors, the script converts the turtle files to RDF/XML, N-Triples and JSON-LD.
   - The script then continues to convert the RDF/XML files to HTML.
1. RDF/XML, N-Triples and JSON-LD files are saved in the "ontology" folder.
1. HTML files are saved in  "\_includes/ontologies".

### Deploy to GitHub Pages

1. Build the site by running ``bundle exec jekyll build``, which will generate static page files in the /docs directory.
1. Add changes to Git, commit them and push everything to GitHub:
   1. ``git add .``
   1. ``git commit -m "Deploy site to GitHub Pages"`` (or whatever message suits your needs)
   1. ``git push``

You might need to wait a few minutes to see any changes on the actual website.

### Add New Ontologies

To add a new ontology to the website, the following steps are necessary: 

1. Have the ontology ready as a turtle file.
1. Name the ontology file in accordance with the ending of the IRI.
   - I.e. if the base IRI is http://e-editiones.ch/ontology/agent, the ontology file should be agent.ttl.
1. Save the ontology file in the "ontology" folder.
1. Create a new markdown file in the of the "collections" subfolders ("\_external", "\_generalDomain", "\_generalHumanities", "\_project", "\_specificHumanities").
   - The name of the file must be the same as the name of the ontolgoy file.
   - You can create a new collection by creating a new subfolder and updating the "\_config.yml" file accordingly.
1. Add front-matter meta data to the newly created markdown file (title, description, file). E.g.:
   ```
   ---
   title: Petrus Lombard' Sentences
   description: An ontology for the Digital Repertory of Commentaries on Peter Lombard’s Sentences
   file: drcs
   ---
   ```
   Everything written below the front matter will be shown on the ontology page as well. 
1. Convert the available turtle files as described above.

[jekyll]: https://jekyllrb.com/
[inseri]: https://github.com/nie-ine/inseri
[ruby]: https://www.ruby-lang.org/en/documentation/installation/
[gems]: https://rubygems.org/pages/download
[bundler]: https://bundler.io/
[python3]: https://www.python.org/downloads/
[venv]: https://docs.python.org/3/library/venv.html
