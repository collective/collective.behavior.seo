Changelog
=========


1.0a2 (unreleased)
------------------

- Fix implementer decorator on SEOFields behavior in python. The zcml registration was correct and seems to override. [fredvd]



1.0a1 (2018-10-12)
------------------

- Override update method on TitleViewlet instead of page_title, otherwise Site title still gets
  appended to the overriden title.
  [fredvd]
  
- Basic version, only for Title and Description
  [fredvd]
