LATEXMK	= latexmk
TITLE	= thesis

.PHONY: pdf

all: pdf

pdf:
	$(LATEXMK) -f -pdf -pdflatex="pdflatex -interactive=nonstopmode"

clean:
	$(LATEXMK) -CA

cleanall: clean
	rm -f *.fls
	rm -f chapters/*.fls
	rm -f $(TITLE).bbl
	rm -f $(TITLE).run.xml
	rm -f $(TITLE).glg
	rm -f $(TITLE).glo
	rm -f $(TITLE).gls
	rm -f $(TITLE).ist
