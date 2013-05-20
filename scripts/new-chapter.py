#!/usr/bin/env python

import os
import re
import sys

templates_dirname = "/templates"
template_filename = "/chapter.tex"
chapters_dirname = "/chapters"

# get all absolute paths
current_path = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.join(current_path + '/..'))
templates_path = os.path.abspath(os.path.join(root_path + templates_dirname))
template_file = os.path.abspath(os.path.join(templates_path + template_filename))
chapters_path = os.path.abspath(os.path.join(root_path + chapters_dirname))

# get the last chapters number
chapters = [ chapter for chapter in os.listdir(chapters_path) if chapter.endswith('.tex')]

last_chapter = sorted(chapters)[-1]
chapter_number = last_chapter.split('.', 1)[0][-1]

# get title from the command line
if len(sys.argv) > 1:
    title = sys.argv[1].strip()
else:
    title = None

# put chapter title in template
with open(template_file) as f:
    tpl = f.read()

if title is not None:
    tpl = re.sub(r'title', title, tpl)

# create the new file with proper filename
new_chapter_number = int(chapter_number) + 1
new_chapter_filename = "/chapter{}.tex".format(new_chapter_number)
new_chapter = os.path.abspath(os.path.join(chapters_path + new_chapter_filename))

# to be on the safe side
if os.path.exists(new_chapter):
    print("File {} already exists".format(new_chapter_filename))
    sys.exit(1)

with open(new_chapter, 'w') as f:
    f.write(tpl)

print("Created new chapter: {}".format(new_chapter))
