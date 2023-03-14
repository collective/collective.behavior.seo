import os
import pkg_resources
import subprocess


domain = "collective.behavior.seo"
os.chdir(pkg_resources.resource_filename(domain, ""))
os.chdir("../../../")
target_path = "src/collective/seo/"
locale_path = target_path + "locales/"
i18ndude = "./bin/i18ndude"


def locale_folder_setup():
    os.chdir(locale_path)
    languages = [d for d in os.listdir(".") if os.path.isdir(d)]
    for lang in languages:
        folder = os.listdir(lang)
        if "LC_MESSAGES" in folder:
            continue
        else:
            lc_messages_path = lang + "/LC_MESSAGES/"
            os.mkdir(lc_messages_path)
            cmd = "msginit --locale={} --input={}.pot --output={}/LC_MESSAGES/{}.po".format(  # NOQA: E501
                lang,
                domain,
                lang,
                domain,
            )
            subprocess.call(
                cmd,
                shell=True,
            )

    os.chdir("../../../../")


def _rebuild():
    cmd = "{} rebuild-pot --pot {}/{}.pot --create {} {}".format(
        i18ndude,
        locale_path,
        domain,
        domain,
        target_path,
    )
    subprocess.call(
        cmd,
        shell=True,
    )


def _sync():
    cmd = "{} sync --pot {}/{}.pot {}*/LC_MESSAGES/{}.po".format(
        i18ndude,
        locale_path,
        domain,
        locale_path,
        domain,
    )
    subprocess.call(
        cmd,
        shell=True,
    )


def update_locale():
    locale_folder_setup()
    _sync()
    _rebuild()
