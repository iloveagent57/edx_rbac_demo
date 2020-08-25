edx_rbac_demo
=============================
This repository demonstrates how to make use of `edx-rbac <https://github.com/edx/edx-rbac>`_
to control resource access in Django applications.

Startup Guide
-------------

First, clone this repository.  Then:

#. Create (or use an existing) python virtual environment.  Run ``pip install -r requirements/pip-tools.txt``
   to install local python dependency tools.

#. ``make upgrade`` to compile the requirements ``*.txt`` files.

#. ``make docker_build`` to build the docker images.
   This will install the requirements/dependencies.

#. ``docker-compose up`` to start the containers

#. ``./provision-demo.sh`` to set up databases, run migrations, etc.

#. Authenticate against the LMS (our central authentication service)
   at http://localhost:18000/login

#. Login to this demo service at http://localhost:8000/login - make sure that the request sends
   the `use-jwt-cookie` header (there are browser extensions to help you easily do this).

#. Visit one of the API endpoints like http://localhost:8000/api/v1/users/1/


License
-------

The code in this repository is licensed under the AGPL 3.0 unless
otherwise noted.

Please see `LICENSE.txt <LICENSE.txt>`_ for details.
