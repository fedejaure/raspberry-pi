Raspberry Pi Playbook
=====================

Raspberry Pi setup and configuration via Ansible.

Quickstart
----------

1. Clone this repository.
2. Install dependencies:
    ```shell
    $ pipenv sync
    Creating a virtualenv for this project…
    ...
    To activate this project's virtualenv, run pipenv shell.
    Alternatively, run a command inside the virtualenv with pipenv run.
    All dependencies are now up-to-date!
    $ pipenv shell
    Launching subshell in virtual environment…
    ...
    (raspberry-pi-playbook)$ ansible-galaxy install -r requirements.yml
    ```
3. Run the playbook:
    ```shell
    (raspberry-pi-playbook)$ ansible-playbook main.yml
    ```
