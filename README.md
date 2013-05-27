Thesis Template
---------------

These are the files I used while writing my master thesis. It uses [latex-mk][2]. To
generate the sample pdf file run `make` at the project's root directory.


Generate glossaries with latex-mk
---------------------------------

To generate glossaries with latex-mk add the following snippet to your `~/.latexmkrc` file:

    add_cus_dep('glo', 'gls', 0, 'makeglo2gls');
    sub makeglo2gls {
                system("makeindex -s '$_[0]'.ist -t '$_[0]'.glg -o '$_[0]'.gls '$_[0]'.glo");
    }


Structure
---------

The main file is the `thesis.tex` which in turn includes the `thesis.sty` file. All
commands, environments and packages are defined in the `thesis.sty` file, while the
`thesis.tex` includes the chapters, the references and defines a basic structure.

Chapters are included from the `chapters` folder. The term definitions reside in the 
`glossary` folder. For images figures etc I prefer the `img` folder using a flat layout, 
but that's more of a personal taste. Finally frontmatter and
backmatter are in the `frontmatter` and `endmatter` folders respectively.

Scripts
-------

The `img2eps.sh` scripts in an imagemagick wrapper which converts image files to the
eps format. The `new-chapter.py` is a script to quickly generate a scaffold of the next
chapter. It accepts an optional parameter with the chapter's title. It creates the
chapter file in the `chapter` folder using the appropriate filename.


What it looks like
------------------

Check out the pdf output [here][1].


[1]: https://dl.kodama.gr/docs/thesis-template-sample.pdf
[2]: http://latex-mk.sourceforge.net/
