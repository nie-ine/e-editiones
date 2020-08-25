# e-editiones

These are the files necessary to develop, build and maintain [e-editiones.ch](https://e-editiones.ch) - the website of the ontologies published in the [NIE-INE project](https://www.nie-ine.ch/). 

## Basic Workflow
1. Ontologies are developed as turtle files.
1. A script validates the turtle files and converts them to RDF/XML, N-Triples, and JSON-LD as well as to a human-readable HTML version.
1. The ontologies are made available through a [dockerized][docker] static website built with [Jekyll][jekyll] and hosted on the same server as [inseri][inseri].

## Develop, Build and Maintain Locally

### Dependencies

- [Ruby][ruby]
  - [Ruby Gems][gems]
  - [Bundler][bundler]
  - [Jekyll][jekyll]
- [Python 3][python3]
  - with the ability to create a virtual environment (e.g. [venv][venv])
- [Docker][docker]

### Get Started

1. Make sure you have the above listed dependencies installed.
1. Clone repository.
1. cd into repository with ``cd e-editiones``.
1. Run ``bundle install`` to fetch the needed Ruby gems.
1. cd into "ttl_conv" with ``cd ttl_conv``.
1. Set up a Python virtual environment. E.g. ``virtualenv ttl_conv``
1. Activate your virtual environment. E.g. ``source ttl_conv/bin/activate`` (type ``deactivate`` to deactivate).
1. Run ``pip3 install -r requirements.txt`` to fetch the needed Python packages.
1. cd back to "e-editiones" with ``cd ..``.

You should now be all set to develop, build and maintain the website locally. 

### Develop

The folder and file structure you see is based on [Jekyll][jekyll]'s needs but there are some additional non-Jekyll folders and files. Below is a quick overview of the top-level files. You might want to visit the [Jekyll Docs](https://jekyllrb.com/docs/) to see how Jekyll itself works. 

Folder/File        | Description                                
 ----------------- | -------------------------------------------
 \_includes        | Jekyll folder containing HTML building blocks. The subfolder "ontologies" contains the human-readable HTML version of each ontology.
 \_layouts         | Jekyll folder containing HTML templates.
 \_posts           | Jekyll folder for blogging content. Currently not in use for this website.
 \_sass            | Jekyll folder containing scss stylesheets. These files are compiled to a single css file for the final static website.
 \_site            | Jekyll folder containing the static files version of the website. The folder and its content are created when running ``jekyll build``. This is the content that gets dockerized and published. 
 assets            | Jekyll folder containing asset files for the static website. 
 collections       | Jekyll folder to group content into collections. This folder is needed to group the created ontologies into "generic" and "project".
 nginx_conf        | Custom folder containing files for the [NGINX][nginx] configuration used during dockerizing the website. 
 ontology          | Custom Jekyll folder containing all the ontology files. 
 ttl_conv          | Custom folder containing a Python script and additional resources to convert turtle files into needed formats and files. 
 .gitignore        | Gitingore file.
 404.html          | 404 error page for the static website.
 \_config.yml      | Jekyll file for site-wide configurations.
 about.markdown    | Jekyll file with the content of the About page.
 Dockerfile        | Dockerfile used to dockerize the website.
 Gemfile           | Jekyll file used to list the needed Ruby Gems to run Jekyll.
 Gemfile.lock      | Jekyll file listing all the necessary Ruby Gem dependencies.
 index.markdown    | Jekyll file with the content of the Home page.
 README.md         | The very file you're reading right now.
 semantic-web-technolgoy.markdown | Jekyll file with the content of the Semantic Web Technology page.
 
#### Serve Locally

To serve the website locally, run ``bundle exec jekyll serve`` and visit http://localhost:4000.

#### Build Locally

To build the static website, run ``bundle exec jekyll build`` and all necessary files will be available in the "\_site" folder.

### Turtle File Conversion

To convert turtle files to the needed formats: 

1. Any turtle file needs to be in the "ontology" folder.
   - Be aware of the correct file naming (see [Add New Ontologies](#add-new-ontologies) below)
1. cd into "ttl_conv" with ``cd ttl_conv``.
1. Activate your virtual environment, if not activated, with ``source ttl_conv/bin/activate``.
1. Run ``python3 -W ignore convert_files.py``.
   - ``-W ignore`` is optional but it ignores some default RDFlib messages.
   - The script validates available turtle files and stops with error messages if there are invalid files.
   - If there are no errors, the script converts the turtle files to RDF/XML, N-Triples and JSON-LD.
   - The script then continues to convert the RDF/XML files to HTML.
1. RDF/XML, N-Triples and JSON-LD files are saved in the "ontology" folder.
1. HTML files are saved in  "\_includes/ontologies".

### Dockerize

The static website will be made available as a Docker container running an [NGINX][nginx] web server with the website on it. 

To dockerize the website, run ``docker build -t nieine/e-editiones .``

To run the container locally, run ``docker run -p 80:80 nieine/e-editiones`` and visit http://localhost.

#### NGINX Configuration

During the build of the Docker container, the following default NGINX configuration files are replaced with custom versions available in the "nginx_conf" folder:  
- /etc/nginx/nginx.conf
- /etc/nginx/mime.types
- /etc/nginx/conf.d/default.conf

The customized files take care of file permissions as well as content negotiation for ontology files. The web server checks the accept header of GET requests and serves an ontology file accordingly: 

- text/turtle
- application/rdf+xml
- application/n-triples
- application/ld+json

By default, the server returns HTML. 

### Deploy

1. Dockerize the website with a current date tag (YYYY-MM-DD) with ``docker build -t nieine/e-editiones:YYYY-MM-DD .``
1. Push the new image to dockerhub with ``docker push nieine/e-editiones:YYYY-MM-DD``
1. Change docker compose file accordingly, if necessary.
1. Restart the server.

### Add New Ontologies

To add a new ontology to the website, the following steps are necessary: 

1. Have the ontology ready as a turtle file.
1. Name the ontology file in accordance with the ending of the IRI.
   - I.e. if the base IRI is http://e-editiones.ch/ontology/agent, the ontology file should be agent.ttl.
1. Save the ontology file in the "ontology" folder.
1. Create a new markdown file in the "collections" folder (either within "\_generic" or "\_project").
   - The name of the file must be the same as the name of the ontolgoy file.
   - You can create a new collection by creating a new subfolder and updating the "\_config.yml" file accordingly.
1. Add front-matter meta data to the newly created markdown file (title, description, file). E.g.:
   ```
   ---
   title: Petrus Lombardus Sentences
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
[docker]: https://www.docker.com/get-started
[nginx]: https://www.nginx.com/
