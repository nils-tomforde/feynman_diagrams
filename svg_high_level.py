
import svg_handler


class Context:
    def __init__(self,
                 width: float,
                 height: float) -> None:
        self.svg = svg_handler.SVG(width=str(width), height=str(height))

        self.width = width
        self.height = height

        self.line_width = 2
        self.line_color = (0, 0, 0)
        self.fontsize = 12
        self.font_color = (0, 0, 0)

        # TODO: Allow different scaling, make it possible to flip y axis
        self.scaling_x = self.width
        self.scaling_y = self.height

        self.path = {}

    def set_line_width(self,
                       line_width: float) -> None:
        self.line_width = line_width

    def set_line_color(self,
                       line_color: tuple[float, float, float]) -> None:
        self.line_color = line_color

    def set_fontsize(self,
                     fontsize: float) -> None:
        self.fontsize = fontsize

    def set_font_color(self,
                       font_color: tuple[float, float, float]) -> None:
        self.font_color = font_color

    def draw_circle(self,
                    cx: float,
                    cy: float,
                    r: float,
                    fill_color_rgb: tuple[float, float, float] = None,
                    stroke_color_rgb: tuple[float, float, float] = None,
                    fill_opacity: float = None,
                    opacity: float = None,
                    stroke_width: float = None) -> None:

        fill = None if fill_color_rgb is None else f"rgb({fill_color_rgb[0]}, {fill_color_rgb[1]}, {fill_color_rgb[2]})"
        stroke = None if stroke_color_rgb is None else f"rgb({stroke_color_rgb[0]}, {stroke_color_rgb[1]}, {stroke_color_rgb[2]})"

        circle = svg_handler.Circle(cx=str(cx),
                                    cy=str(cy),
                                    r=str(r),
                                    fill=fill,
                                    stroke=stroke,
                                    fill_opacity=str(fill_opacity),
                                    opacity=str(opacity),
                                    stroke_width=str(stroke_width))

        self.svg.root_tag.append_child_tag(circle)

    def draw_ellipse(self,
                     cx: float,
                     cy: float,
                     rx: float,
                     ry: float) -> None:
        ellipse = svg_handler.Ellipse(cx=str(cx),
                                      cy=str(cy),
                                      rx=str(rx),
                                      ry=str(ry))

        self.svg.root_tag.append_child_tag(ellipse)

    def draw_rectangle(self,
                       x: float,
                       y: float,
                       width: float,
                       height: float,
                       fill_color_rgb: tuple[float, float, float] = None,
                       fill_opacity: float = None) -> None:

        fill = None if fill_color_rgb is None else f"rgb({fill_color_rgb[0]}, {fill_color_rgb[1]}, {fill_color_rgb[2]})"

        rectangle = svg_handler.Rectangle(x=str(x),
                                          y=str(y),
                                          width=str(width),
                                          height=str(height),
                                          fill=fill,
                                          fill_opacity=None if fill_opacity is None else str(fill_opacity))

        self.svg.root_tag.append_child_tag(rectangle)

    def draw_line(self,
                  x1: float,
                  y1: float,
                  x2: float,
                  y2: float) -> None:
        line = svg_handler.Line(x1=str(x1),
                                y1=str(y1),
                                x2=str(x2),
                                y2=str(y2))

        self.svg.root_tag.append_child_tag(line)

    def draw_polyline(self,
                      *args: float) -> None:
        points = f''

        for index, arg in enumerate(args):
            if index % 2 == 0:
                # x coordinate
                points += f'{arg},'
            else:
                # y coordinate
                points += f'{arg} '

        polyline = svg_handler.Polyline(points=points)

        self.svg.root_tag.append_child_tag(polyline)

    def draw_polygon(self,
                     *args: float) -> None:
        points = f''

        for index, arg in enumerate(args):
            if index % 2 == 0:
                # x coordinate
                points += f'{arg},'
            else:
                # y coordinate
                points += f'{arg} '

        polygon = svg_handler.Polygon(points=points)

        self.svg.root_tag.append_child_tag(polygon)

    def draw_text(self,
                  text_string: str,
                  x: float,
                  y: float,
                  text_anchor: str = None,
                  writing_mode: str = None,
                  glyph_orientation_vertical: str = None,
                  font_size: float = None) -> None:

        text = svg_handler.Text(text_string=text_string,
                                x=str(x),
                                y=str(y),
                                text_anchor=text_anchor,
                                writing_mode=writing_mode,
                                glyph_orientation_vertical=glyph_orientation_vertical,
                                font_size=str(font_size))

        self.svg.root_tag.append_child_tag(text)

    def path_init(self,
                  fill_color_rgb: tuple[float, float, float] = None,
                  stroke_color_rgb: tuple[float, float, float] = None,
                  stroke_width: float = None,
                  stroke_linecap: str = None,
                  stroke_linejoin: str = None,
                  stroke_dasharray: tuple[float, float] = None,
                  stroke_dashoffset: float = None,
                  fill_rule: str = None,
                  fill_opacity: float = None,
                  transform: str = None,
                  opacity: float = None,
                  clip_path: str = None,
                  marker_start: str = None,
                  marker_mid: str = None,
                  marker_end: str = None) -> None:

        self.path = {
            "d": "",
            "fill": None if fill_color_rgb is None else f"rgb({fill_color_rgb[0]}, {fill_color_rgb[1]}, {fill_color_rgb[2]})",
            "stroke": None if stroke_color_rgb is None else f"rgb({stroke_color_rgb[0]}, {stroke_color_rgb[1]}, {stroke_color_rgb[2]})",
            "stroke_width": stroke_width if stroke_width is None else str(stroke_width),
            "stroke_linecap": stroke_linecap,
            "stroke_linejoin": stroke_linejoin,
            "stroke_dasharray": None if stroke_dasharray is None else f"{stroke_dasharray[0]},{stroke_dasharray[1]}",
            "stroke_dashoffset": None if stroke_dashoffset is None else str(stroke_dashoffset),
            "fill_rule": fill_rule,
            "fill_opacity": None if fill_opacity is None else str(fill_opacity),
            "transform": transform,
            "opacity": None if opacity is None else str(opacity),
            "clip_path": clip_path,
            "marker_start": marker_start,
            "marker_mid": marker_mid,
            "marker_end": marker_end
        }

    def path_move_to(self,
                     x: float,
                     y: float) -> None:
        self.path["d"] += f"M {x},{y} "

    def path_line_to(self,
                     x: float,
                     y: float) -> None:
        self.path["d"] += f"L {x},{y} "

    def path_horizontal_line(self,
                             x: float) -> None:
        self.path["d"] += f"H {x} "

    def path_vertical_line(self,
                           y: float) -> None:
        self.path["d"] += f"V {y} "

    def path_close(self):
        self.path["d"] += f"Z "

    def path_elliptic_arc(self,
                          rx: float,
                          ry: float,
                          phi: float,
                          lf: int,
                          sf: int,
                          x: float,
                          y: float) -> None:
        # rx, ry: radii of ellipse
        # phi: angle for ellipse
        # lf "long bow flag", 0 or 1, use short (0) or long (1) bow
        # sf "sweep flag", 0 or 1, left (0) or right (1) curvature
        # x, y: target point

        # TODO: can produce impossible path! x y could be unreachable. Check this

        self.path["d"] += f"A {rx},{ry},{phi},{lf},{sf},{x},{y} "

    def path_quadratic_bezier(self,
                              xc: float,
                              yc: float,
                              x: float,
                              y: float) -> None:
        # xc, yc: control point
        # x, y: target point

        self.path["d"] += f"Q {xc},{yc},{x},{y} "

    def path_smooth_quadratic_bezier(self,
                                     x: float,
                                     y: float) -> None:
        # x, y target points. uses the point reflection of the previous control point on the previous enpoint as the new control point

        self.path["d"] += f"T {x},{y} "

    def path_cubic_bezier(self,
                          xc1: float,
                          yc1: float,
                          xc2: float,
                          yc2: float,
                          x: float,
                          y: float) -> None:
        # xc1, yc1: control point 1
        # xc2, yc2: control point 2
        # x, y: target point

        self.path["d"] += f"C {xc1},{yc1},{xc2},{yc2},{x},{y} "

    def path_smooth_cubic_bezier(self,
                                 xc2: float,
                                 yc2: float,
                                 x: float,
                                 y: float) -> None:
        # uses the point reflectoin of the previous second control point on the previous end point as the new first control point
        # xc2, yc2: control point 2
        # x, y: target point

        self.path["d"] += f"S {xc2},{yc2},{x},{y} "

    def path_rel_move_to(self,
                         x: float,
                         y: float) -> None:
        self.path["d"] += f"m {x},{y} "

    def path_rel_line_to(self,
                         x: float,
                         y: float) -> None:
        self.path["d"] += f"l {x},{y} "

    def path_rel_horizontal_line(self, x: float) -> None:
        self.path["d"] += f"h {x} "

    def path_rel_vertical_line(self, y: float) -> None:
        self.path["d"] += f"v {y} "

    def path_rel_elliptic_arc(self,
                              rx: float,
                              ry: float,
                              phi: float,
                              lf: int,
                              sf: int,
                              x: float,
                              y: float) -> None:
        # rx, ry: radii of ellipse
        # phi: angle for ellipse
        # lf "long bow flag", 0 or 1, use short (0) or long (1) bow
        # sf "sweep flag", 0 or 1, left (0) or right (1) curvature
        # x, y: target point

        # TODO: can produce impossible path! x y could be unreachable. Check this

        self.path["d"] += f"a {rx},{ry},{phi},{lf},{sf},{x},{y} "

    def path_rel_quadratic_bezier(self,
                                  xc: float,
                                  yc: float,
                                  x: float,
                                  y: float) -> None:
        # xc, yc: control point
        # x, y: target point

        self.path["d"] += f"q {xc},{yc},{x},{y} "

    def path_rel_smooth_quadratic_bezier(self,
                                         x: float,
                                         y: float) -> None:
        # x, y target points. uses the point reflection of the previous control point on the previous enpoint as the new control point

        self.path["d"] += f"t {x},{y} "

    def path_rel_cubic_bezier(self,
                              xc1: float,
                              yc1: float,
                              xc2: float,
                              yc2: float,
                              x: float,
                              y: float) -> None:
        # xc1, yc1: control point 1
        # xc2, yc2: control point 2
        # x, y: target point

        self.path["d"] += f"c {xc1},{yc1},{xc2},{yc2},{x},{y} "

    def path_rel_smooth_cubic_bezier(self,
                                     xc2: float,
                                     yc2: float,
                                     x: float,
                                     y: float) -> None:
        # uses the point reflectoin of the previous second control point on the previous end point as the new first control point
        # xc2, yc2: control point 2
        # x, y: target point

        self.path["d"] += f"s {xc2},{yc2},{x},{y} "

    def path_finish(self) -> None:
        path = svg_handler.Path(d=self.path["d"],
                                fill=self.path["fill"],
                                stroke=self.path["stroke"],
                                stroke_width=self.path["stroke_width"],
                                stroke_linecap=self.path["stroke_linecap"],
                                stroke_linejoin=self.path["stroke_linejoin"],
                                stroke_dasharray=self.path["stroke_dasharray"],
                                stroke_dashoffset=self.path["stroke_dashoffset"],
                                fill_rule=self.path["fill_rule"],
                                fill_opacity=self.path["fill_opacity"],
                                transform=self.path["transform"],
                                opacity=self.path["opacity"],
                                clip_path=self.path["clip_path"],
                                marker_start=self.path["marker_start"],
                                marker_mid=self.path["marker_mid"],
                                marker_end=self.path["marker_end"])

        self.svg.root_tag.append_child_tag(path)

        # reset path
        self.path = {}

    def write(self, file_path: str) -> None:
        self.svg.write(file_path=file_path)
