import jinja2
import sys, os
from jinja2 import Template
latex_jinja_env = jinja2.Environment(
	block_start_string = '\BLOCK{',
	block_end_string = '}',
	variable_start_string = '\VAR{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)
template = latex_jinja_env.get_template('INFORME/SECWPA1-Template.tex')
output = file('INFORME/INF-WPA.tex', 'w')
output.write(template.render(sbssid=sys.argv[1],sessid=sys.argv[2],scanal=sys.argv[3],sinterfaz=sys.argv[4]).encode("iso-8859-1"))
output.close()
