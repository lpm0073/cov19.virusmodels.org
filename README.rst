cov19.virusmodels.org
=====================


Developers
----------
The dev environment depends on postgres in your local dev environment, so make sure that you have this.
It MIGHT be handled with the projects requirements/local.txt (i have not checked) -- please advise if you know.

* (lawrence) I am setting up .env for the project so that we can get CI working this morning. be aware you might 
need to "git checkout" often today as i get this working.

.. code:: bash


    git clone https://github.com/lpm0073/cov19.virusmodels.org.git
    cd cov19.virusmodels.org
    python3.7 -m venv venv
    source venv/bin/activate
    pip install -r cov19/requirements/local.txt


