# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- role `geerlingguy.docker`.

### Changed
- Update ansible requirements versions.
- Update `community.docker` to `3.7.0`.
- Update `community.general` to `8.3.0`.
- Upgrade Otacon/Ocelot `mdns-beacon` to `0.7.1`.
- Otacon/Ocelot `nginxproxy/nginx-proxy` to `1.2.1`.
- Otacon/Ocelot `netdata/netdata` to `v1.37.1`.
- Ocelot `octoprint/octoprint` to `1.8.6`.
- Otacon `pihole/pihole` to `2023.01.10`.

### Removed
- role `geerlingguy.docker_arm`

## [0.5.0] - 2022-10-15
### Added
- Otacon/Ocelot jump start page.

### Changed
- Otacon/Ocelot `nginxproxy/nginx-proxy` to `1.0.1`.
- Otacon/Ocelot `traefik/whoami` to `v1.8.7`.
- Otacon/Ocelot `netdata/netdata` to `v1.36.1`.
- Otacon `pihole/pihole` to `2022.10`.
- Ocelot `octoprint/octoprint` to `1.8.4`.

### Removed
- molecule lint step.

## [0.4.0] - 2022-03-13
### Added
- Ocelot.

### Changed
- Move playbooks into playbooks dir.
- Pipenv by poetry.
- Otacon/Ocelot `nginxproxy/nginx-proxy` to `1.0.0`.
- Otacon/Ocelot `traefik/whoami` to `v1.8.0`.
- Otacon/Ocelot `netdata/netdata` to `v1.33.1`.
- Otacon `pihole/pihole` to `2022.02.1`.

## [0.3.0] - 2022-02-02
### Changed
- Upgrade Otacon mdns-beacon version to `0.6.1`.
- Otacon `tecnativa/docker-socket-proxy` to `0.1.1`.
- Otacon `netdata/netdata` to `v1.33.0`.
- Otacon `pihole/pihole` to `2022.01.1`.
- Otacon `traefik/whoami` to `v1.7.1`.
- Otacon `nginxproxy/nginx-proxy` to `0.10.0`.
- Tasks `docker-compose.yml` by `services.yml`.
- Restart services only if they are modified.

### Added
- Invoke task playbook `skip-tag` option.
- Invoke task playbook `list-tags` option.
- Debian 11 "bullseye" support.
- Raspbian swap config.

### Fixed
- Set wifi country.
- Use collections.

## [0.2.1] - 2021-07-14
### Changed
- Updated deps.

## [0.2.0] - 2021-04-11
### Changed
- Refactor tasks modules.

### Added
- Molecule tests.

## [0.1.0] - 2021-03-29
### Added
- First `otacon` release.

[Unreleased]: https://github.com/fedejaure/raspberry-pi/compare/v0.5.0...develop
[0.5.0]: https://github.com/fedejaure/raspberry-pi/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/fedejaure/raspberry-pi/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/fedejaure/raspberry-pi/compare/v0.2.1...v0.3.0
[0.2.1]: https://github.com/fedejaure/raspberry-pi/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/fedejaure/raspberry-pi/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/fedejaure/raspberry-pi/compare/releases/tag/v0.1.0
