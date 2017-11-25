PyDashie port to MicroPython/Picoweb
####################################

This is quick and dirty port of PyDashie to MicroPython and Picoweb
micro-framework. It's quick and dirty, because it doesn't create
JavaScript/CSS bundles out of Coffee/SCSS files, but serves precreated
bundle (as produced by original PyDashie).

Fairly speaking, all this bundling-at-runtime, coffees and scsses of the
original PyDashie aren't too clean either...

This port is proof of concept, before embarking on a project to create
a decent, unbloated web dashboard for MicroPython.

To run, go to ``pydashie/`` directory and run ``micropython main_picoweb.py``
(picoweb should be installed first of course, ``micropython -m upip picoweb``).

What follows is the original PyDashie README.

PyDashie
########

This project is mostly dormant now.

`Main Documentation <http://evolvedlight.github.com/pydashie/>`_

PyDashy is a port of `Dashing <https://github.com/Shopify/dashing>`_ by `Shopify <http://www.shopify.com/>`_ to Python 2.7

.. image:: http://evolvedlight.github.com/pydashie/images/mainscreen.png

Installation
############

For development purposes,

    python setup.py develop

OR

    python setup.py install

And you can run the application by

    pydashie

Goto localhost:5000 to view the sample application in action.
