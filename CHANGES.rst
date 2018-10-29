Changelog
=========


1.0a2 (unreleased)
------------------

- Don't generate robots vocabulary on every request. [fredvd, mauritsvanrees]

- Add meta robots as extra SEO field, based on sc.seo package. Use AjaxMultiSelectField for easy entry. [fredvd]

- Fix implementer decorator on SEOFields behavior in python. The zcml registration was correct though. [fredvd]

- Revert name changes.  [jladage]


1.0a1 (2018-10-12)
------------------

- Override update method on TitleViewlet instead of page_title, otherwise Site title still gets
  appended to the overriden title.
  [fredvd]
  
- Basic version, only for Title and Description
  [fredvd]
