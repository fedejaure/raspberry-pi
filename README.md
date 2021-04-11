Raspberry Pi Playbook
=====================

Setup and configuration of my own Raspberry Pi fleet via Ansible (use by your own risk).


Fleet Members ([Metal Gear Characters][metal-gear-characters])
-------------

* [Otacon][otacon]

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
    ```

3. Activate the virtual environment:

    ```shell
    $ pipenv shell
    Launching subshell in virtual environment…
    ...
    (raspberry-pi-playbook)$
    ```

4.  Install required Ansible roles:

    ```shell
    (raspberry-pi-playbook)$ ansible-galaxy install -r requirements.yml
    ```

    or

    ```shell
    (raspberry-pi-playbook)$ inv galaxy-install
    ```

5. Configure the `inventory` file, e.g.:

    ```
    [otacon]
    127.0.0.1 ansible_python_interpreter=/usr/bin/python3 ansible_user=pi ansible_password=somepassword ansible_become_password=somepassword
    ```

6. Run the playbook:

    ```shell
    (raspberry-pi-playbook)$ ansible-playbook main.yml -i inventory
    ```

    or

    ```shell
    (raspberry-pi-playbook)$ inv playbook
    ```

7. Enjoy

Running a specific set of tagged tasks
--------------------------------------

The tags available are:

* `always`
* `docker`
* `docker-compose`
* `firewall`
* `git`
* `init`
* `lcd`
* `mdns-beacon`
* `pip`
* `security`
* `ssh`
* `supervisor`

Overriding Defaults
-------------------

You can override the defaults configured in `default.config.yml` by creating a `config.yml` file and setting the overrides in that file. e.g.:

```yaml
security_ssh_password_authentication: "yes"
security_ssh_permit_root_login: "yes"
security_autoupdate_mail_to: example@example.com
```

Any variable can be overridden in `config.yml`; see the supporting roles documentation for a complete list of available variables.

Development
-----------

To know all invoke tasks run:

```shell
(raspberry-pi-playbook)$ inv --list
Available tasks:

ansible-lint     Run ansible linter.
galaxy-install   Install ansible-galaxy requirements.
hooks            Run pre-commit hooks.
install-hooks    Install pre-commit hooks.
lint             Run all linting.
playbook         Runs Ansible playbooks, executing the defined tasks on the targeted hosts.
version          Bump version.
yamllint         Run yamllint, a linter for YAML files.
```

License
-------

MIT / BSD

Author Information
------------------

This role was created in 2020 by [Federico Jaureguialzo][fedejaure].

[fedejaure]: https://github.com/fedejaure
[metal-gear-characters]: https://en.wikipedia.org/wiki/List_of_Metal_Gear_characters
[otacon]: https://en.wikipedia.org/wiki/Otacon
