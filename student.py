import utils
from slugify import slugify, Slugify

users = [
    [
        "Username",
        "First name",
        "Last name",
        "Display name",
        "Job title",
        "Department",
        "Office number",
        "Office phone",
        "Mobile phone",
        "Fax",
        "Alternate email address",
        "Address",
        "City",
        "State or province",
        "ZIP or postal code",
        "Country or region"
    ]
]

class Student(object):
    def __init__(self, sheet, index):
        self.user = [sheet.cell_value(index, cIndex).strip()
                     for cIndex in [0, 1, 5]]
        self.user[0] = utils.removeChar(self.user[0]).capitalize()
        self.user[1] = utils.removeChar(self.user[1]).capitalize()
        self.suffix = "@"

    def getUsername(self):
        email_slug = Slugify()
        email_slug.to_lower = True
        email_slug.pretranslate = {"ə": "e"}
        return f"{email_slug(self.getFullName(),to_lower = True,separator = '.')}.{self.user[3].lower()}{self.suffix}"

    def clear(self):
        for k, v in enumerate(self.user[:1]):
            self.user[k] = utils.removeChar(v)

    def getFullName(self):
        return f"{self.user[0]} {self.user[1]}"

    def getData(self):
        self.user.insert(2, self.getFullName())
        self.user.insert(0, self.getUsername())
        return self.user
