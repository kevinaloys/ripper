Ripper
======

.. image:: https://readthedocs.org/projects/ripper/badge/?version=latest
:target: https://readthedocs.org/projects/ripper/?badge=latest
:alt: Documentation Status

Rip Images. The Pythonic Way.

Ideas
-----

- Allow elegant Image Ripping from websites.
- Ability to Save in a Particular Directory.
- Default get. Rip Images of Type 'jpg' and 'jpeg'
- For more, Specify Format of the Image.
- Simple Save. Images Saved to Folder defaulting to Title of the Web Page.


Usage
-----

Simple Usage::

    >>> import ripper

    >>> r = ripper.get('http://website.com')
    >>> r.url
    ['http://website.com/image.jpg','http://website.com/hello.jpg']
    >>> r.save
    Successfully Saved 2 Images.


Advanced Usage::

	>>> import ripper

	>>> r = ripper.get('http://website.com',type=(jpg,png,gif))
	>>> r.url
	['http://website.com/img.jpg','http://website.com/hello.png','http://website.com/hello.gif']
	>>> r.save('/home/directory')
	Successfully Saved 3 Images to /home/directory
