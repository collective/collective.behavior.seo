Design decisions
================

As with every software project, Plone add'ons have many design decisions which are trade offs between complexity, end
user friendliness, webmaster/integrator flexibility and configurations, etc.etc. If you wonder "Why didn't they ..."
it might be answered here.

Fields:

The first implementation of the seo_robots field was a copy from the sc.seo implementation, where the editor could
pick and choose from individual tags mentioned in robots documentation. We even figured out how to use select2 in
Plone 5.1 with look-ahead typing.

Problem is: most content editors don't know exactly which fields do what, editors will have to multiple click their
selection togeter, robot tags can get outdated (a few from sc.seo were not best practice anymore). It depends on your
audience, but the webmaster can now create sets of tags for every individual site. And there are probably 3 - 6  sane
combinations, which are easy to select by content editors.


