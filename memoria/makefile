memoria.pdf: memoria.tex datos-informe/INFORME/informe-WPA.pdf datos-informe/INFORME/informe_WEP.pdf 

%.pdf: %.tex
	rubber --pdf $<


clean:
	$(RM) *~ *.aux *.toc *.log memoria.pdf


