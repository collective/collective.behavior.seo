Changelog
=========


1.1.0 (unreleased)
------------------

- Support structured data as JSON-LD for articles and events via behavior.
  [agitator]


1.0.1 (2020-09-09)
------------------

- Make python3.8 compatible. [fredvd]


1.0.0 (2020-08-17)
------------------

- Make python3 compatible. [erral]

- Update uninstall profile. [fredvd]


1.0b1 (2018-10-30)
------------------

- Add robots field, Add control panel form with configurable list of robot tag preset combinations for editors to pick from. [fredvd]

- Don't generate robots vocabulary on every request. [fredvd, mauritsvanrees]

- Fix implementer decorator on SEOFields behavior in python. The zcml registration was correct though. [fredvd]

- Revert name changes.  [jladage]

- Improve description of robots field.  [jladage]

- Autopep8 and fix code-analysis feedback.  [jladage]
 

1.0a1 (2018-10-12)
------------------

- Override update method on TitleViewlet instead of page_title, otherwise Site title still gets
  appended to the overriden title.
  [fredvd]
  
- Basic version, only for Title and Description
  [fredvd]
