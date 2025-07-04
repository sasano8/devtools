from io import StringIO
import yaml
from jinja2 import Environment, FileSystemLoader

class TemplateEnginBase:
    def __init__(self, **kwargs):
        self._kwargs = kwargs
        self._validate()

    def _validate(self):
        ...

    def render(self, path):
        jinja_loader = Environment(loader=FileSystemLoader('.'))
        template = jinja_loader.get_template(path)
        rendered = template.render(self._kwargs)
        return rendered
    
    def load_yml(self, path):
        rendered = self.render(path)
        with StringIO(rendered) as f:
            data = yaml.safe_load(f)
            return data
        
    def dump_str(self, data, path):
        with open(path, "w") as f:
            f.write(data)
        
    def dump_yml(self, data, path):
        with open(path, "w") as f:
            yaml.dump(data, f)


class AuthConfig(TemplateEnginBase):
    def _validate(self):
        kwargs = self._kwargs
        domain = kwargs.get("domain")
        kwargs.setdefault("authelia_url", "https://auth." + domain)
        kwargs.setdefault("default_redirection_url", "https://webdav." + domain)
        kwargs.setdefault("displayname", "admin")
        if "hashed_password" not in kwargs:
            raise Exception()
        kwargs.setdefault("email", "admin@example.com")
        kwargs.setdefault("groups", ["admins", "dev"])


def generate(**kwargs):
    conf = AuthConfig(**kwargs)

    auth_configuration = conf.render("templates/configuration.yml")
    auth_users = conf.render("templates/users_database.yml")
    compose = conf.render("templates/docker-compose.yml")

    conf.dump_str(auth_configuration, ".volumes/authelia/configuration.yml")
    conf.dump_str(auth_users, ".volumes/authelia/users_database.yml")
    conf.dump_str(compose, "docker-compose.override.yml")


def generate_from_json(path):
    import json
    with open(path) as f:
        conf = json.load(f)
    generate(**conf["auth"])

generate_from_json("seed.json")
