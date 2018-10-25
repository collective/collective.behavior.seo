Changelog
=========


1.0a2 (unreleased)
------------------

- Incorporate metarobots based on sc.seo package as extra SEO field. Use AjaxMultiSelectField for easy entry. [fredvd]

- Fix implementer decorator on SEOFields behavior in python. The zcml registration was correct though. [fredvd]


1.0a1 (2018-10-12)
------------------

- Override update method on TitleViewlet instead of page_title, otherwise Site title still gets
  appended to the overriden title.
  [fredvd]
  
- Basic version, only for Title and Description
  [fredvd]
