#!/usr/bin/env python

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
template = latex_jinja_env.get_template('INFORME/SUBSWPA1-Template.tex')
output = file('INFORME/INF-SUBSWPA1.tex', 'w')
output.write(template.render(x1=sys.argv[1],x2=sys.argv[2],x3=sys.argv[3]).encode("iso-8859-1"))
output.close()
