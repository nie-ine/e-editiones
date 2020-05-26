import os
import glob
import rdflib
import subprocess

# Get file paths
def file_path(relative_path):
    folder = os.path.dirname(os.path.abspath(__file__))
    path_parts = relative_path.split("/")
    new_path = os.path.join(folder, *path_parts)
    return new_path

# Turtle file conversion
def ttl2rdf(ttl):
	graph = rdflib.Graph()
	graph.parse(ttl, format="turtle")
	new_graph = graph.serialize(destination=ttl.replace(".ttl",".rdf"), format="pretty-xml")

# Xsl transformation
def xsl_transform(jar_file, rdf_file, xsl_file, output_file):
	jar = file_path(jar_file)
	inpt = file_path(rdf_file)
	xslt = file_path(xsl_file)
	outpt = file_path(output_file)

	# Add "-t" to display version and timing information to the standard error output
	subprocess.call(['java', '-cp', '%s' % jar, 'net.sf.saxon.Transform', '-s:%s' % inpt, '-xsl:%s' % xslt, '-o:%s' % outpt])

#######
# Paths
#######

wd = os.getcwd()

files_path = "../ontology"

############
# ttl to rdf
############

os.chdir(files_path)

ttl_files = glob.glob("*.ttl")

success = []
error = {}

for ttl in ttl_files:
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

#############
# rdf to html
#############

xsl = "../file_conversions/resources/rdf2html.xsl"
saxon_jar = "../file_conversions/resources/saxon9he.jar"
html_path = "../_includes/ontologies/"
rdf_files = glob.glob("*.rdf")

for rdf in rdf_files:
	print("Converting " + rdf + " to html")
	path = html_path + rdf.replace(".rdf", ".html")
	xsl_transform(saxon_jar, rdf, xsl, path)

