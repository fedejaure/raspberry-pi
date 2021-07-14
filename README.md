Raspberry Pi Playbook
=====================

<div align="center">

[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/fedejaure/raspberry-pi-playbook?logo=github)](https://github.com/fedejaure/raspberry-pi-playbook/releases)
[![tests](https://github.com/fedejaure/raspberry-pi-playbook/actions/workflows/tests.yml/badge.svg)](https://github.com/fedejaure/raspberry-pi-playbook/actions/workflows/tests.yml)
[![License](https://img.shields.io/badge/license-MIT-brightgreen)](https://opensource.org/licenses/MIT)

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](https://www.contributor-covenant.org/version/2/0/code_of_conduct/)

</div>

Setup and configuration of my own Raspberry Pi fleet via Ansible (use by your own risk).


Fleet Members ([Metal Gear Characters][metal-gear-characters])
-------------

* [Otacon][otacon]
    
    > Pi-hole DNS sinkhole instance.
    
    - services:
        
        + [pihole][pihole]: The Pi-hole DNS sinkhole instance. Available at [pihole.otacon.local](http://pihole.otacon.local)
        
        + [whoami][whoami]: Tiny Go webserver that prints os information and HTTP request to output. Available at [whoami.otacon.local](http://whoami.otacon.local)

        + [netdata][netdata]: Monitor everything in real time. Available at [netdata.otacon.local](http://netdata.otacon.local)

    - variables:
        
        + `rpi_locale`: Raspberry Pi locale config. (Default: `en_US.UTF-8`)
        
        + `rpi_layout`: Raspberry Pi keyboard layout config. (Default: `us`)
        
        + `rpi_dist_upgrade`: If Raspberry Pi should do a dist-upgrade. (Default: `no`)
        
        + `rpi_tz`: Raspberry Pi Time Zone config. (Default: `'Europe/Amsterdam'`)

        + `rpi_pihole_password`: [pihole.otacon.local](http://pihole.otacon.local) `Admin password`. (Default: `random`)

* more coming ...

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

7. Enjoy!

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

To display available tasks run:

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

This playbook was created in 2020 by [Federico Jaureguialzo][fedejaure].

[fedejaure]: https://github.com/fedejaure
[metal-gear-characters]: https://en.wikipedia.org/wiki/List_of_Metal_Gear_characters
[otacon]: https://en.wikipedia.org/wiki/Otacon
[pihole]: https://pi-hole.net/
[whoami]: https://github.com/traefik/whoami
[netdata]: https://www.netdata.cloud/
