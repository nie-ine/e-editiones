import os
import glob
import rdflib
import subprocess
from pathlib import Path

# Get file paths
def file_path(relative_path):
    folder = os.path.dirname(os.path.abspath(__file__))
    path_parts = relative_path.split("/")
    new_path = os.path.join(folder, *path_parts)
    return new_path

# Turtle to rdf conversion
def ttl2rdf(ttl):
	graph = rdflib.Graph()
	graph.parse(ttl, format="turtle")
	new_graph = graph.serialize(destination=ttl.replace(".ttl",".rdf"), format="pretty-xml")

# Turtle to ... conversion
def ttl2n3(ttl):
	graph = rdflib.Graph()
	graph.parse(ttl, format="turtle")
	new_graph = graph.serialize(destination=ttl.replace(".ttl",".rdf"), format="pretty-xml")

# Xsl transformation
def xsl_transform(jar, inpt, xslt, outpt):
	subprocess.call(['java', '-cp', '%s' % jar, 'net.sf.saxon.Transform', '-s:%s' % inpt, '-xsl:%s' % xslt, '-o:%s' % outpt])

def main():
	ontology_path = file_path("../ontology")

	# ttl to rdf
	ttl_files = glob.glob(os.path.join(ontology_path, "*.ttl"))

	success = []
	error = {}

	for ttl in ttl_files:
		# The transformation also validates the ttl file
		try: 
			ttl2rdf(ttl)
			success.append(ttl)



		except Exception as e:
			error[ttl] = str(e)

	print("")
	print("Successfully converted %d turtle files to rdf:" % len(success))
	print("")
	print(*success, sep="\n")
	print("")
	print("%d error(s) found:" % len(error))
	print("")
	if error:
		for k,v in error.items():
			print(k)
			print("##############################")
			print(v)
			print("")

	# rdf to html
	xsl_path = file_path("resources/rdf2html.xsl")
	saxon_jar_path = file_path("resources/saxon9he.jar")
	html_path = file_path("../_includes/ontologies")
	rdf_files = glob.glob(os.path.join(ontology_path, "*.rdf"))

	for rdf in rdf_files:
		print("Converting " + rdf + " to html")

		destination = os.path.join(html_path, (os.path.basename(rdf)).replace(".rdf", ".html")) # rdf.replace(".rdf", ".html"))
		xsl_transform(saxon_jar_path, rdf, xsl_path, destination)

if __name__ == "__main__":
	main()