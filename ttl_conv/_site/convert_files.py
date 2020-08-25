import os
import sys
import glob
import rdflib
import subprocess
from pathlib import Path

# Turtle to rdf conversion
def serializeTtl(ttl, target, suffix):
	graph = rdflib.Graph()
	graph.parse(ttl, format="turtle")
	new_graph = graph.serialize(destination=ttl.replace(".ttl",".{}".format(suffix)), format=target)

# Xsl transformation
def xsl_transform(jar, inpt, xslt, outpt):
	subprocess.call(['java', '-cp', '%s' % jar, 'net.sf.saxon.Transform', '-s:%s' % inpt, '-xsl:%s' % xslt, '-o:%s' % outpt])

def main():
	ontology_path = Path("../ontology").resolve()

	# ttl to rdf
	ttl_files = glob.glob(str(ontology_path / "*.ttl"))

	success = []
	error = {}

	for ttl in ttl_files:
		ttl = Path(ttl)
		# The transformation also validates the ttl file
		try: 
			serializeTtl(str(ttl.resolve()), "pretty-xml", "rdf")
			success.append(ttl.name)

		except Exception as e:
			error[ttl.name] = str(e)

	if error:
		for k,v in error.items():
			print("")
			print(k)
			print("=================================")
			print(v)
			print("")
		sys.exit("Damn! Exited with error(s): {} invalid turtle file(s) found...see above".format(len(error)))

	else: 
		for ttl in ttl_files:
			ttl = Path(ttl)

			serializeTtl(str(ttl.resolve()), "nt", "nt")
			serializeTtl(str(ttl.resolve()), "json-ld", "jsonld")

		print("Converted turtle files to RDF/XML, N-Triples, JSON-LD")
		print("")
		# rdf to html
		xsl_path = Path("resources/rdf2html.xsl").resolve()
		saxon_jar_path = Path("resources/saxon9he.jar").resolve()
		html_path = Path("../_includes/ontologies").resolve()
		rdf_files = glob.glob(str(ontology_path / "*.rdf"))

		for rdf in rdf_files:
			rdf = Path(rdf)
			print("Converting " + rdf.name + " to html")

			destination = html_path / (rdf.name).replace(".rdf", ".html")
			xsl_transform(saxon_jar_path, rdf, xsl_path, destination)

		success.sort()
		print("")
		print(*success, sep="\n")
		print("")
		print("Horray! Successfully converted {} turtle files...see above".format(len(success)))

if __name__ == "__main__":
	main()