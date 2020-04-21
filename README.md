# e-editiones

This will be the website for making the NIE-INE ontologies available outside of GitHub. 
In a first version, it will be available through GitHub Pages on: https://nie-ine.github.io/e-editiones/ 

## Dependencies

- [Ruby](https://www.ruby-lang.org/en/documentation/installation/)
- [Bundler](https://bundler.io/)
- [Jekyll](https://jekyllrb.com/)

## Develop and run locally

1. Clone repository
2. cd into repository
3. Check [Jekyll](https://jekyllrb.com/) to see how the pieces fit together
4. To build the static site locally: ``bundle exec jekyll build`` 
   The files will be available in the \_site folder
5. To run locally: ``bundle exec jekyll serve``
   The site will be available on http://localhost:4000/

## Publish on GitHub Pages

Push to the repository as usual.
The \_site folder will not be pushed to the repository. GitHub Pages is selfaware of Jekyll and will build the site from the given source files in the master branch. 