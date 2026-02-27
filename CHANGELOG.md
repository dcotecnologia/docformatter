# Changelog

All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.8.0] - 2026-02-27

### Changed

- migrate project metadata from deprecated `[tool.poetry]` keys to PEP 621 `[project]`
- make production dependency constraints more flexible (`charset_normalizer`, `tomli` extra)
- refresh development, testing, and linting dependency versions
- add root `Makefile` with common development tasks (`install`, `test-*`, `lint`, `format`, `docs`, `clean`)
- expand tox/CI Python matrix to include Python 3.14

## [1.7.7] - 2025-05-11

### Changed

- chore\(deps-dev\): bump black from 22.12.0 to 24.3.0 [\#311](https://github.com/PyCQA/docformatter/pull/311) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump jinja2 from 3.1.4 to 3.1.6 [\#310](https://github.com/PyCQA/docformatter/pull/310) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump requests from 2.31.0 to 2.32.2 [\#309](https://github.com/PyCQA/docformatter/pull/309) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump virtualenv from 20.21.1 to 20.26.6 [\#308](https://github.com/PyCQA/docformatter/pull/308) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump zipp from 3.15.0 to 3.19.1 [\#307](https://github.com/PyCQA/docformatter/pull/307) ([dependabot[bot]](https://github.com/apps/dependabot))
- chore\(deps-dev\): bump urllib3 from 2.0.7 to 2.2.2 [\#306](https://github.com/PyCQA/docformatter/pull/306) ([dependabot[bot]](https://github.com/apps/dependabot))

## [1.7.6] - 2025-05-07

### Added

- prefer new unittest.mock from the standard library [\#280](https://github.com/PyCQA/docformatter/pull/280) ([a-detiste](https://github.com/a-detiste))
- Handle abbreviation 'etc.' \(et cetera\) [\#273](https://github.com/PyCQA/docformatter/pull/273) ([knedlsepp](https://github.com/knedlsepp))

### Fixed

- Do not double-process urls [\#284](https://github.com/PyCQA/docformatter/pull/284) ([lilatomic](https://github.com/lilatomic))

### Changed

- Fix pre-commit syntax [\#266](https://github.com/PyCQA/docformatter/pull/266) ([jonashaag](https://github.com/jonashaag))
- Update version listed in documentation's Pre-Commit example [\#262](https://github.com/PyCQA/docformatter/pull/262) ([korverdev](https://github.com/korverdev))
- Add missing comma in requirements table [\#261](https://github.com/PyCQA/docformatter/pull/261) ([EFord36](https://github.com/EFord36))

## [1.7.5] - 2023-07-12

### Added

- fix: not recognizing `yield` as a sphinx field name [\#254](https://github.com/PyCQA/docformatter/pull/254) ([weibullguy](https://github.com/weibullguy))

## [1.7.4] - 2023-07-10

### Fixed

- fix: summary with back ticks and sphinx field names with periods [\#248](https://github.com/PyCQA/docformatter/pull/248) ([weibullguy](https://github.com/weibullguy))

### Changed

- chore: update documentation link for metadata [\#247](https://github.com/PyCQA/docformatter/pull/247) ([icp1994](https://github.com/icp1994))
- test: split format tests into multiple files [\#246](https://github.com/PyCQA/docformatter/pull/246) ([weibullguy](https://github.com/weibullguy))

## [1.7.3] - 2023-06-23

### Fixed

- fix: removing newline between Sphinx field lists [\#237](https://github.com/PyCQA/docformatter/pull/237) ([weibullguy](https://github.com/weibullguy))

### Changed

- chore: move changelog to tag workflow [\#233](https://github.com/PyCQA/docformatter/pull/233) ([weibullguy](https://github.com/weibullguy))

## [1.7.2] - 2023-06-07

### Fixed

- fix: wrapping issues with reST directives, quoted URLs, and Sphinx field lists [\#219](https://github.com/PyCQA/docformatter/pull/219) ([weibullguy](https://github.com/weibullguy))

## [1.7.1] - 2023-05-19

### Added

- feat: support epytext style [\#211](https://github.com/PyCQA/docformatter/pull/211) ([weibullguy](https://github.com/weibullguy))
- feat: use tomllib for Python 3.11+ [\#208](https://github.com/PyCQA/docformatter/pull/208) ([weibullguy](https://github.com/weibullguy))
- feat: wrap Sphinx style long parameter descriptions [\#201](https://github.com/PyCQA/docformatter/pull/201) ([weibullguy](https://github.com/weibullguy))

### Fixed

- fix: improper wrapping of short anonymous hyperlnks [\#213](https://github.com/PyCQA/docformatter/pull/213) ([weibullguy](https://github.com/weibullguy))

### Changed

- chore: update version strings [\#214](https://github.com/PyCQA/docformatter/pull/214) ([weibullguy](https://github.com/weibullguy))
- chore: update pre-commit-config [\#209](https://github.com/PyCQA/docformatter/pull/209) ([weibullguy](https://github.com/weibullguy))

## [1.7.0] - 2023-05-15

### Added

- feat: add option to format compatible with black [\#196](https://github.com/PyCQA/docformatter/pull/196) ([weibullguy](https://github.com/weibullguy))
- feat: add option for user to provide list of words not to capitalize [\#195](https://github.com/PyCQA/docformatter/pull/195) ([weibullguy](https://github.com/weibullguy))

### Changed

- chore: update workflows [\#206](https://github.com/PyCQA/docformatter/pull/206) ([weibullguy](https://github.com/weibullguy))

## [1.6.5] - 2023-05-03

### Fixed

- fix: removing blank line after import section [\#204](https://github.com/PyCQA/docformatter/pull/204) ([weibullguy](https://github.com/weibullguy))

### Changed

- chore: add GH release badge [\#200](https://github.com/PyCQA/docformatter/pull/200) ([weibullguy](https://github.com/weibullguy))
- chore: update workflows to create release [\#198](https://github.com/PyCQA/docformatter/pull/198) ([weibullguy](https://github.com/weibullguy))
- chore: update GH actions to generate CHANGELOG [\#194](https://github.com/PyCQA/docformatter/pull/194) ([weibullguy](https://github.com/weibullguy))

## [1.6.4] - 2023-04-26

## [1.6.3] - 2023-04-23

## [1.6.2] - 2023-04-22

## [1.6.1] - 2023-04-21

## [1.6.0] - 2023-04-04

## [1.5.1] - 2022-12-16

## [1.5.0] - 2022-08-19

## [1.4] - 2020-12-27

[Unreleased]: https://github.com/arquitt/docformatter/compare/v1.8.0...HEAD
[1.8.0]: https://github.com/arquitt/docformatter/compare/v1.7.7...v1.8.0
[1.7.7]: https://github.com/arquitt/docformatter/compare/v1.7.6...v1.7.7
[1.7.6]: https://github.com/arquitt/docformatter/compare/v1.7.5...v1.7.6
[1.7.5]: https://github.com/arquitt/docformatter/compare/v1.7.4...v1.7.5
[1.7.4]: https://github.com/arquitt/docformatter/compare/v1.7.3...v1.7.4
[1.7.3]: https://github.com/arquitt/docformatter/compare/v1.7.2...v1.7.3
[1.7.2]: https://github.com/arquitt/docformatter/compare/v1.7.1...v1.7.2
[1.7.1]: https://github.com/arquitt/docformatter/compare/v1.7.0...v1.7.1
[1.7.0]: https://github.com/arquitt/docformatter/compare/v1.6.5...v1.7.0
[1.6.5]: https://github.com/arquitt/docformatter/compare/v1.6.4...v1.6.5
[1.6.4]: https://github.com/arquitt/docformatter/compare/v1.6.3...v1.6.4
[1.6.3]: https://github.com/arquitt/docformatter/compare/v1.6.2...v1.6.3
[1.6.2]: https://github.com/arquitt/docformatter/compare/v1.6.1...v1.6.2
[1.6.1]: https://github.com/arquitt/docformatter/compare/v1.6.0...v1.6.1
[1.6.0]: https://github.com/arquitt/docformatter/compare/v1.5.1...v1.6.0
[1.5.1]: https://github.com/arquitt/docformatter/compare/v1.5.0...v1.5.1
[1.5.0]: https://github.com/arquitt/docformatter/compare/v1.4...v1.5.0
[1.4]: https://github.com/arquitt/docformatter/releases/tag/v1.4
