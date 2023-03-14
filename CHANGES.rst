Changelog
=========


1.0.3 (unreleased)
------------------

- Nothing changed yet.


1.0.2 (2023-03-14)
------------------

- Removed English locale.  I think there used to be a need for this long time ago, but not anymore, as far as I know.
  [maurits]

- Changed ``<head>`` to ``'head'`` in help text and translations.
  ``<head>`` gets swallowed:
  you got "the section of a page" and now "the 'head' section of a page".
  [maurits]

- Fixed broken html in edit form on Plone 6 due to Dutch typo.
  We used ``<head`` and this made the Save/Cancel buttons show only on the SEO fieldset.
  And this fieldset showed an extra footer.
  [maurits]


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
