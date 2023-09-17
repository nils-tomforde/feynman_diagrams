
import file_handler
import xml_handler


class SVG:
    def __init__(self,
                 version: str = "1.1",
                 base_profile: str = "full",
                 width: str = "800",
                 height: str = "600") -> None:
        root_attributes = {
            "xmlns": "http://www.w3.org/2000/svg",
            "xmlns:xlink": "http://www.w3.org/1999/xlink",
            "version": version,
            "baseProfile": base_profile,
            "width": width,
            "height": height,
            "viewBox": f'0 0 {width} {height}'
        }

        self.root_tag = xml_handler.Tag(tag_name="svg", attributes=root_attributes, content="")

        self.content_string = ""

    def generate_content_string(self) -> None:
        xml_handler.remove_completely_empty_children_recursive(self.root_tag)

        content_string = ""

        content_string += '<?xml version="1.0" encoding="UTF-8"?>\n'
        content_string += '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n'
        content_string += self.root_tag.get_string_representation()

        self.content_string = content_string

    def write(self, file_path: str) -> None:
        self.generate_content_string()

        file_handler.write_to_file(self.content_string, file_path)


def check_xml_well_formed():
    # check for all xml rules
    # (incomplete list)

    # exactly one root element
    # all elements with content have a start and an end tag
    # all child elements must be closed before a parent element is closed
    # an element cant have more than one attribute with the same name
    # attribute values must be enclosed in "" or ''
    # start and end tags must have the same case

    pass


class Path(xml_handler.Tag):
    def __init__(self, d: str, fill: str = None, stroke: str = None, stroke_width: str = None,
                 stroke_linecap: str = None, stroke_linejoin: str = None, stroke_dasharray: str = None,
                 stroke_dashoffset: str = None, fill_rule: str = None, fill_opacity: str = None, transform: str = None,
                 opacity: str = None, clip_path: str = None, marker_start: str = None, marker_mid: str = None,
                 marker_end: str = None) -> None:

        attributes = {
            "d": d,
            "fill": fill,
            "stroke": stroke,
            "stroke-width": stroke_width,
            "stroke-linecap": stroke_linecap,  # butt, round, square
            "stroke-linejoin": stroke_linejoin,  # miter, round, bevel
            "stroke-dasharray": stroke_dasharray,
            "stroke-dashoffset": stroke_dashoffset,
            "fill-rule": fill_rule,
            "fill-opacity": fill_opacity,
            "transform": transform,
            "opacity": opacity,
            "clip-path": clip_path,
            "marker-start": marker_start,
            "marker-mid": marker_mid,
            "marker-end": marker_end
        }

        super().__init__(tag_name="path", attributes=attributes, content="", is_empty=True)


class Circle(xml_handler.Tag):
    def __init__(self, cx: str, cy: str, r: str, fill: str, stroke: str, fill_opacity: str, opacity: str, stroke_width: str):
        attributes = {
            "cx": cx,
            "cy": cy,
            "r": r,
            "fill": fill,
            "stroke": stroke,
            "fill-opacity": fill_opacity,
            "opacity": opacity,
            "stroke-width": stroke_width
        }

        super().__init__(tag_name="circle", attributes=attributes, content="", is_empty=True)


class Ellipse(xml_handler.Tag):
    def __init__(self, cx: str, cy: str, rx: str, ry: str):
        attributes = {
            "cx": cx,
            "cy": cy,
            "rx": rx,
            "ry": ry
        }

        super().__init__(tag_name="ellipse", attributes=attributes, content="", is_empty=True)


class Rectangle(xml_handler.Tag):
    def __init__(self, x: str, y: str, width: str, height: str, fill: str = None, fill_opacity: str = None):
        attributes = {
            "x": x,
            "y": y,
            "width": width,
            "height": height,
            "fill": fill,
            "fill-opacity": fill_opacity
        }

        super().__init__(tag_name="rect", attributes=attributes, content="", is_empty=True)


class Line(xml_handler.Tag):
    def __init__(self, x1: str, y1: str, x2: str, y2: str):
        attributes = {
            "x1": x1,
            "y1": y1,
            "x2": x2,
            "y2": y2
        }

        super().__init__(tag_name="line", attributes=attributes, content="", is_empty=True)


class Polyline(xml_handler.Tag):
    def __init__(self, points: str):
        attributes = {
            "points": points
        }

        super().__init__(tag_name="polyline", attributes=attributes, content="", is_empty=True)


class Polygon(xml_handler.Tag):
    def __init__(self, points: str):
        attributes = {
            "points": points
        }

        super().__init__(tag_name="polygon", attributes=attributes, content="", is_empty=True)


class Text(xml_handler.Tag):
    def __init__(self, text_string: str, x: str, y: str, text_anchor: str, writing_mode: str, glyph_orientation_vertical: str, font_size: str):
        attributes = {
            "x": x,
            "y": y,
            "text-anchor": text_anchor,  # start, middle, end
            "writing-mode": writing_mode,  # lr-tb, rl-tb, tb-rl, lr, rl, tb, inherit
            "glyph-orientation-vertical": glyph_orientation_vertical,  # auto, inherit or an angle (0, 90, 180 or 270)
            "font-size": font_size
        }

        # TODO: Add font etc.

        super().__init__(tag_name="text", attributes=attributes, content=text_string, is_empty=False)


# TODO: Add tspan

class Image(xml_handler.Tag):
    pass


class Group(xml_handler.Tag):
    def __init__(self, transform: str):
        attributes = {
            "transform": transform
        }

        super().__init__(tag_name="g", attributes=attributes, content="", is_empty=False)


