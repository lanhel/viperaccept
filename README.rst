***********
viperaccept
***********

This is an application that will perform content negotiation of static
files based on the ``Accept*`` HTTP headers either as a library or as a
stand alone WSGI application.

This will allow websites to deliver static files without the requirement
of exposing the file extension, language identification, etc. This is
recommended by Sir Tim Berners-Lee in `Cool URIs don't change <http://www.w3.org/Provider/Style/URI>`_.

Dynamically generated files content negotiation should occur before this
application is reached.

It is highly recommended that this be placed behind a Cache proxy to
reduce the call cost as much as possible.



.. |date| date:: %Y-%m-%d %H:%M:%S %Z
.. footer::
    | Copyright © 2014 Lance Finn Helsten
    | Licensed under Apache License, Version 2.0.
    | Document generated: |date|.

