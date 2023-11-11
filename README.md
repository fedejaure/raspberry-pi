Raspberry Pi
============

<div align="center">

[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/fedejaure/raspberry-pi?logo=github)](https://github.com/fedejaure/raspberry-pi/releases)
[![tests](https://github.com/fedejaure/raspberry-pi/actions/workflows/tests.yml/badge.svg)](https://github.com/fedejaure/raspberry-pi/actions/workflows/tests.yml)
[![License](https://img.shields.io/badge/license-MIT-brightgreen)](https://opensource.org/licenses/MIT)

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](https://www.contributor-covenant.org/version/2/0/code_of_conduct/)

</div>

Setup and configuration of my own Raspberry Pi fleet via Ansible Collection (use by your own risk).


Fleet Members ([Metal Gear Characters][metal-gear-characters])
-------------

* [Otacon][otacon]
    
    > Pi-hole DNS sinkhole instance.
    
    - services:

        + [jump][jump]: Simple startpage. [otacon.local](http://otacon.local)
        
        + [pihole][pihole]: The Pi-hole DNS sinkhole instance. Available at [pihole.otacon.local](http://pihole.otacon.local)
        
        + [whoami][whoami]: Tiny Go webserver that prints os information and HTTP request to output. Available at [whoami.otacon.local](http://whoami.otacon.local)

        + [netdata][netdata]: Monitor everything in real time. Available at [netdata.otacon.local](http://netdata.otacon.local)

    - variables:
        
        + `rpi_locale`: Raspberry Pi locale config. (Default: `en_US.UTF-8`)
        
        + `rpi_layout`: Raspberry Pi keyboard layout config. (Default: `us`)
        
        + `rpi_dist_upgrade`: If Raspberry Pi should do a dist-upgrade. (Default: `no`)
        
        + `rpi_tz`: Raspberry Pi Time Zone config. (Default: `'Europe/Amsterdam'`)

        + `rpi_wifi_country`: Raspberry Pi Wifi Country config. (Default: `NL`)

        + `rpi_pihole_password`: [pihole.otacon.local](http://pihole.otacon.local) `Admin password`. (Default: `random`)

        + `rpi_swap_config`: Raspberry Pi swap config. (Default: `CONF_SWAPSIZE: 100`)

        + `rpi_open_weather_map_key`: An API key for Open Weather Map, LATLONG (below) must also be defined.

        + `rpi_latlong`: A latitude and longitude for the default location. (Default: `51.9812,5.6584`)

* Ocelot ([Revolver Ocelot][ocelot])

    > OctoPrint an snappy web interface for my 3D printer.

    - services:

        + [jump][jump]: Simple startpage. [ocelot.local](http://ocelot.local)

        + [octoprint][octoprint]: The snappy web interface for your 3D printer! [octoprint.ocelot.local](http://octoprint.ocelot.local)

        + [whoami][whoami]: Tiny Go webserver that prints os information and HTTP request to output. Available at [whoami.ocelot.local](http://whoami.ocelot.local)

        + [netdata][netdata]: Monitor everything in real time. Available at [netdata.ocelot.local](http://netdata.ocelot.local)

    - variables:

        + `rpi_locale`: Raspberry Pi locale config. (Default: `en_US.UTF-8`)

        + `rpi_layout`: Raspberry Pi keyboard layout config. (Default: `us`)

        + `rpi_dist_upgrade`: If Raspberry Pi should do a dist-upgrade. (Default: `no`)

        + `rpi_tz`: Raspberry Pi Time Zone config. (Default: `'Europe/Amsterdam'`)

        + `rpi_wifi_country`: Raspberry Pi Wifi Country config. (Default: `NL`)

        + `rpi_swap_config`: Raspberry Pi swap config. (Default: `CONF_SWAPSIZE: 100`)

        + `rpi_open_weather_map_key`: An API key for Open Weather Map, LATLONG (below) must also be defined.

        + `rpi_latlong`: A latitude and longitude for the default location. (Default: `51.9812,5.6584`)

* more coming ...

Quickstart
----------

1. Clone this repository.

2. Install dependencies:

    ```shell
    $ poetry install --no-root
    Creating virtualenv raspberry-pi in .venv
    Using virtualenv: .venv
    Installing dependencies from lock file

    Package operations: 95 installs, 0 updates, 0 removals

    ...
    ```

3. Activate the virtual environment:

    ```shell
    $ poetry shell
    Spawning shell within .venv
    (raspberry-pi)$
    ```

4.  Install required Ansible roles:

    ```shell
    (raspberry-pi)$ ansible-galaxy install -r requirements.yml
    ```

    or

    ```shell
    (raspberry-pi)$ inv galaxy-install
    ```

5. Configure the `inventory` file, e.g.:

    ```
    [otacon]
    127.0.0.1 ansible_python_interpreter=/usr/bin/python3 ansible_user=pi ansible_password=somepassword ansible_become_password=somepassword
    ```

6. Run the playbook:

    ```shell
    (raspberry-pi)$ ansible-playbook main.yml -i inventory
    ```

    or

    ```shell
    (raspberry-pi)$ inv playbook
    ```

7. Enjoy!

Running a specific set of tagged tasks
--------------------------------------

The tags available are:

* `always`
* `docker`
* `firewall`
* `git`
* `init`
* `lcd`
* `mdns-beacon`
* `pip`
* `security`
* `services`
* `ssh`
* `supervisor`

Overriding Defaults
-------------------

You can override the defaults configured in `default.<fleet-member>.config.yml` by creating a `<fleet-member>.config.yml` file and setting the overrides in that file. e.g.:

```yaml
security_ssh_password_authentication: "yes"
security_ssh_permit_root_login: "yes"
security_autoupdate_mail_to: example@example.com
```

Any variable can be overridden in `<fleet-member>.config.yml`; see the supporting roles documentation for a complete list of available variables.

Development
-----------

To display available tasks run:

```shell
(raspberry-pi)$ inv --list
Available tasks:

  ansible-lint     Run ansible linter.
  clean            Run all clean sub-tasks.
  clean-python     Clean up python file artifacts.
  flake8           Run flake8.
  format           Format code.
  galaxy-install   Install ansible-galaxy requirements.
  hooks            Run pre-commit hooks.
  install-hooks    Install pre-commit hooks.
  lint             Run all linting.
  mypy             Run mypy.
  playbook         Run Ansible playbooks, executing the defined tasks on the targeted hosts.
  safety           Run safety.
  tests            Run ansible molecule test.
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
[ocelot]: https://en.wikipedia.org/wiki/Revolver_Ocelot
[octoprint]: https://octoprint.org/
[jump]: https://github.com/daledavies/jump
