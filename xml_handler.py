import xml.etree.ElementTree as ET

from typing import Self


class Tag:  # maybe call this an element instead
    def __init__(self, tag_name: str, attributes: dict[str, str], content: str, children: list[Self] = None, is_empty=False):
        self.tag_name = tag_name
        self.attributes = attributes
        self.content = content
        if children is None:
            self.children = []
        else:
            self.children = children
        self.is_empty = is_empty

        # self.start_tag = f'<{self.tag_name}>'
        # self.end_tag = f'</{self.tag_name}>'
        # self.empty_tag = f"<{self.tag_name}/>"

    def append_child_tag(self, child: Self):
        self.children.append(child)

    def get_string_representation(self):
        if self.is_empty:
            string_representation = f'<{self.tag_name} '
            for key, value in self.attributes.items():
                if value is None:
                    continue
                string_representation += f'{key}="{value}" '
            string_representation += f'/>\n'
        else:
            string_representation = f'<{self.tag_name} '
            for key, value in self.attributes.items():
                if value is None:
                    continue
                string_representation += f'{key}="{value}" '
            string_representation += f'>'
            if self.content is not None:
                string_representation += self.content
            if len(self.children) > 0:
                string_representation += '\n'
            for child in self.children:
                string_representation += child.get_string_representation()
            string_representation += f'</{self.tag_name}>\n'

        return string_representation


# TODO: Every child element has a "child order" or "degree" and is indented by tabs in the number of the order

def read_xml(content_string: str):
    root = ET.fromstring(content_string)

    root_tag = create_tag_from_et_element(root)

    return root_tag


def create_tag_from_et_element(element: ET.Element) -> Tag:
    tag_name = clean_string_namespace(element.tag)
    attributes = clean_attributes_namespace(element.attrib)

    content = "" if element.text is None else element.text.strip("\n")

    children = []

    for child in element:
        children.append(create_tag_from_et_element(child))

    is_empty = (content == "" and len(children) == 0)  # n tag is considered empty if it has not content or child tags

    tag = Tag(tag_name=tag_name, attributes=attributes, content=content, children=children, is_empty=is_empty)

    return tag


def clean_attributes_namespace(attributes: dict[str, str]) -> dict[str, str]:
    new_attributes = {}

    for key in attributes:
        new_key = clean_string_namespace(key)

        new_attributes[new_key] = attributes[key]

    return new_attributes


def clean_string_namespace(string: str) -> str:
    new_string = string[string.find("}") + 1:]
    return new_string


def remove_children_by_tag_name_recursive(tag: Tag, tag_names: list[str]) -> None:
    new_children = []

    for child in tag.children:
        if child.tag_name not in tag_names:
            new_children.append(child)

        remove_children_by_tag_name_recursive(child, tag_names)

    tag.children = new_children

    # TODO: Make method


def remove_completely_empty_children_recursive(tag: Tag) -> None:
    new_children = []

    for child in tag.children:
        remove_completely_empty_children_recursive(tag=child)

        if not (child.attributes == {} and child.content.strip() == "" and child.children == []):
            new_children.append(child)

    tag.children = new_children

    # TODO: Make method
