import os
import glob
import subprocess

# Get file paths
def file_path(relative_path):
    folder = os.path.dirname(os.path.abspath(__file__))
    path_parts = relative_path.split("/")
    new_path = os.path.join(folder, *path_parts)
    return new_path

# Xsl transformation
def xsl_transform(jar_file, xml_file, xsl_file, output_file):
	jar = file_path(jar_file)
	inpt = file_path(xml_file)
	outpt = file_path(output_file)
	xslt = file_path(xsl_file)

	# Add "-t" to display version and timing information to the standard error output
	subprocess.call(['java', '-cp', '%s' % jar, 'net.sf.saxon.Transform', '-s:%s' % inpt, '-xsl:%s' % xslt, '-o:%s' % outpt])

# Turtle file conversion
def rdf2rdf(jar_file, ttl_file):
	jar = file_path(jar_file)
	inpt = file_path(ttl_file)

	subprocess.call(['java', '-jar', jar, inpt, ".rdf"])


ttl_path = "../ontology/ttl/"
rdf_path = "../ontology/rdf/"
html_path = "../ontology/html/"

xsl = "rdf2html.xsl"
saxon_jar = "saxon9he.jar"
rdf2rdf_jar = "rdf2rdf.jar"

##############
# .ttl to .rdf
##############
# ttl_files = glob.glob("%s/*.ttl" % ttl_path)

# for ttl in ttl_files:
# 	new_name = ttl.replace(".ttl", ".rdf")
# 	rdf2rdf(rdf2rdf_jar, ttl)


# rdf to html
rdf_files = glob.glob("%s/*.rdf" % rdf_path)

for rdf in rdf_files:
	xsl_transform(saxon_jar, rdf, xsl, rdf.replace(".rdf", ".html"))

