import yaml

yaml_file = "yaml1.yaml"
with open(yaml_file) as f:
    output = yaml.load(f)

print(output)
