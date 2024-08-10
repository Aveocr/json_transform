import json


def funds(word, amount):
    return {
        "type":word.split("_balance")[0],
        "amount":amount,
    }


def update_json(orig_json):
    n_json = {}
    _sum = 0
    for key, item in orig_json.items():
        if key.find("_balance") != -1:
            if n_json.get("funds") is None:
                n_json.update({"funds": []})
            n_json["funds"].append(funds(key, item))
            _sum += item
        else:
            n_json.update(
                {key:item}
            )
    n_json.update({"total": _sum})
    return n_json


if __name__ == '__main__':
    with open("input.json", encoding='utf-8') as js:
        file_content = js.read()
        templates = json.loads(file_content)

    # print(templates.JSONDecoder())
    print(templates)

    output = []
    for elem in templates:
        output.append(update_json(elem))

    for i in output:
        for key, item in i.items():
            print(key, ":", item)

    with open("output.json", 'w', encoding="utf-8") as fp:
        json.dump(output, fp)
