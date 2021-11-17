# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Changed
- Upgrade Otacon mdns-beacon version.
- Otacon `tecnativa/docker-socket-proxy` to `0.1.1`.
- Otacon `netdata/netdata` to `v1.31.0`.
- Otacon `pihole/pihole` to `2021.10.1`.
- Otacon `traefik/whoami` to `v1.6.1`.
- Otacon `nginxproxy/nginx-proxy` to `0.9.3`.
- Tasks `docker-compose.yml` by `services.yml`.

### Added
- Invoke task playbook `skip-tag` option.
- Invoke task playbook `list-tags` option.
- Debian 11 "bullseye" support.

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

[Unreleased]: https://github.com/fedejaure/raspberry-pi-playbook/compare/v0.2.1...develop
[0.2.1]: https://github.com/fedejaure/raspberry-pi-playbook/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/fedejaure/raspberry-pi-playbook/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/fedejaure/raspberry-pi-playbook/compare/releases/tag/v0.1.0
