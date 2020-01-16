pytest-ligo
~~~~~~~~~~~

Py.test plugin which adds a tezos fixture to encapsulate boilerplate business
logic.

Install with pip, ie::

    pip install -e git+http://gitlab.com/jpic/pytest-ligo.git#egg=pytest-tezos
    pip install -e git+http://gitlab.com/jpic/pytest-ligo.git#egg=pytest-ligo

Test is example usage:

.. litteralinclude:: test_pytest_tezos.py

Along with .gitlab-ci.yml configuration to adapt to your own use:

.. litteralinclude:: test_pytest_tezos.py
