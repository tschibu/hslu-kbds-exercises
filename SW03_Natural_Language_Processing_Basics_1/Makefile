PDFPARAMS=-s -t latex --pdf-engine=xelatex -f markdown-implicit_figures -V documentclass=scrartcl -V papersize=a4 -V lang=de -V urlcolor=blue -V linkcolor=blue -V geometry:margin=2.54cm
FONTS=-V mainfont='DejaVu Serif' -V sansfont='DejaVu Sans' -V monofont='DejaVu Sans Mono' -V fontsize=10pt
DATE=-V date="`date +'%Y-%m-%d'`"

all: clean pdf

pdf: *.md
	pandoc $(PDFPARAMS) $(FONTS) $(DATE) *.md -o gruppe_01_sw03_natural_language_processing_basics_1.pdf
	
clean:
	rm -f gruppe_01_sw03_natural_language_processing_basics_1.pdf
