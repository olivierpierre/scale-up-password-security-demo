all:
	pandoc --pdf-engine=xelatex -t beamer slides.md -o slides.pdf

spellcheck:
	aspell -c slides.md -p ./.aspell.txt

show: all
	# install rust + cargo install watchexec-cli
	xdg-open slides.pdf && watchexec -e md,tex,yaml 'pandoc -t beamer slides.md -o slides.pdf'

clean:
	rm slides.pdf