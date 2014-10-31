Ripper
======

An elegant Image Ripper. The Pythonic Way.

Ideas
-----

- Allow elegant Image Ripping from websites.
- Ability to Save in a Particular Directory.
- Specify Format of the Image.

Usage
-----

Simple Usage::

    >>> import ripper

    >>> r = ripper.get('http://website.com', type=('jpg','png'))
    >>> r.urls
    ['http://website.com/image.jpg','http://website.com/hello.jpg']
    >>> r.ok
    True
    >>> r.save('/home/directory')
    Successfully Saved 30 Images.
