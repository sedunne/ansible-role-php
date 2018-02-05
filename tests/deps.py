import yaml

with open('meta/main.yml','r') as f:
    meta = yaml.safe_load(f.read())

if meta["dependencies"]:
    with open('tests/requirements.yml', 'w') as requirements:
        yaml.safe_dump(meta["dependencies"], requirements, default_flow_style=False)
