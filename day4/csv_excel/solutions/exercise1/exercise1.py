import csv
import jinja2


def main():
    template_file = "exercise1.j2"
    with open(template_file) as f:
        bgp_template = f.read()
    template = jinja2.Template(bgp_template)

    file_name = "exercise1.csv"
    with open(file_name) as f:
        read_csv = csv.DictReader(f)
        for entry in read_csv:
            print("\n")
            print(entry["device_name"])
            print("*" * 80)
            print(template.render(entry))
            print("*" * 80)
            print("\n")


if __name__ == "__main__":
    main()
