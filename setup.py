"""Installer for the collective.behavior.seo package."""

from setuptools import setup

long_description = "\n\n".join(
    [
        open("README.md").read(),
        open("CONTRIBUTORS.md").read(),
        open("CHANGES.md").read(),
    ]
)


setup(
    name="collective.behavior.seo",
    version="2.0.2.dev0",
    description="An add-on for Plone",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: 6.1",
        "Framework :: Plone :: 6.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone",
    author="Zest Software",
    author_email="info@zestsoftware.nl",
    url="https://github.com/collective/collective.behavior.seo",
    license="GPL version 2",
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "setuptools",
        "Products.CMFPlone",
        "Products.GenericSetup",
        "plone.api",
        "plone.app.layout",
        "plone.app.registry",
        "plone.app.upgrade",
        "plone.autoform",
        "plone.base",
        "plone.behavior",
        "plone.dexterity",
        "plone.schema",
        "plone.supermodel",
        "zope.component",
        "zope.i18nmessageid",
        "zope.interface",
        "zope.publisher",
        "zope.schema",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            "plone.app.robotframework[debug]",
            "plone.browserlayer",
            "plone.testing>=5.0.0",
            "zest.releaser[recommended]",
            "zestreleaser.towncrier",
            "zest.pocompile",
        ],
    },
)
