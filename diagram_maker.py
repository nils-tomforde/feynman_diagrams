
import svg_high_level
import math
import latex_to_svg


def draw_diagram(width: int, height: int, commands: callable, file_path: str):
    ctx = svg_high_level.Context(width=width, height=height)

    commands(ctx)

    ctx.write(file_path=file_path)


def draw_formula(context: svg_high_level.Context, formula: str, x: float, y: float, fontsize: float = None, font_color: tuple[float, float, float] = None):
    # Use context defaults when not overwritten
    if fontsize is None:
        fontsize = context.fontsize

    if font_color is None:
        font_color = context.font_color

    x *= context.scaling_x
    y *= context.scaling_y

    latex_tag = latex_to_svg.latex_to_svg(formula, fontsize, color_rgb_256=font_color, x=x, y=y)

    context.svg.root_tag.append_child_tag(latex_tag)


def draw_text(context: svg_high_level.Context, text: str, x: float, y: float, fontsize: float = None, font_color: tuple[float, float, float] = None):
    # Use context defaults when not overwritten
    if fontsize is None:
        fontsize = context.fontsize

    if font_color is None:
        font_color = context.font_color

    x *= context.scaling_x
    y *= context.scaling_y

    context.draw_text(text_string=text, x=x, y=y, font_size=fontsize)
    # TODO: Add fontcolor to text


def set_background(context: svg_high_level.Context, r: float, g: float, b: float, a: float):
    context.draw_rectangle(0, 0, context.width, context.height, fill_color_rgb=(r, g, b), fill_opacity=a)


def _draw_line(context, x1: float, y1: float, x2: float, y2: float, line_width=None, line_color=None):
    if line_width is None:
        line_width = context.line_width
    if line_color is None:
        line_color = context.line_color

    context.path_init(stroke_color_rgb=line_color, stroke_width=line_width, fill_opacity=0)
    context.path_move_to(x1, y1)
    context.path_line_to(x2, y2)
    context.path_close()
    context.path_finish()


def _draw_full_circle(context: svg_high_level.Context, cx: float, cy: float, r: float, line_width: float = None,
                      line_color: tuple[float, float, float] = None, fill_color: tuple[float, float, float] = None,
                      fill_opacity: float = None, line_opacity: float = None):
    if line_width is None:
        line_width = context.line_width
    if line_color is None:
        line_color = context.line_color

    context.draw_circle(cx, cy, r, fill_color_rgb=fill_color, stroke_color_rgb=line_color, fill_opacity=fill_opacity, opacity=line_opacity, stroke_width=line_width)


def _draw_triangle(context: svg_high_level.Context, xm: float, ym: float, angle: float, is_anti_particle: bool):
    size = context.line_width * 4

    if not is_anti_particle:
        p1 = (size / 2, 0)
        p2 = (- size / 2, size / 2)
        p3 = (- size / 2, -size / 2)
    else:
        p1 = (- size / 2, 0)
        p2 = (size / 2, - size / 2)
        p3 = (size / 2, size / 2)

    p1_rotated = rotate_vector_2d(p1, angle)
    p2_rotated = rotate_vector_2d(p2, angle)
    p3_rotated = rotate_vector_2d(p3, angle)

    context.path_init(fill_color_rgb=context.line_color)
    context.path_move_to(xm + p1_rotated[0], ym + p1_rotated[1])
    context.path_line_to(xm + p2_rotated[0], ym + p2_rotated[1])
    context.path_line_to(xm + p3_rotated[0], ym + p3_rotated[1])
    context.path_close()

    context.path_finish()


def _draw_cross(context: svg_high_level.Context, xm: float, ym: float, angle: float):
    # TODO: Maybe do it like in Peskin and Schroeder and make a circle around the cross and dont show the underlying line

    size = context.line_width * 6

    p1 = (- size / 2, - size / 2)
    p2 = (+ size / 2, + size / 2)
    p3 = (- size / 2, + size / 2)
    p4 = (+ size / 2, - size / 2)

    p1_rotated = rotate_vector_2d(p1, angle)
    p2_rotated = rotate_vector_2d(p2, angle)
    p3_rotated = rotate_vector_2d(p3, angle)
    p4_rotated = rotate_vector_2d(p4, angle)

    context.path_init(stroke_color_rgb=context.line_color, stroke_width=context.line_width)
    context.path_move_to(xm + p1_rotated[0], ym + p1_rotated[1])
    context.path_line_to(xm + p2_rotated[0], ym + p2_rotated[1])

    context.path_move_to(xm + p3_rotated[0], ym + p3_rotated[1])
    context.path_line_to(xm + p4_rotated[0], ym + p4_rotated[1])

    context.path_finish()


class Point:
    def __init__(self, context: svg_high_level.Context, x: float, y: float):
        self.x = x * context.scaling_x
        self.y = y * context.scaling_y


class Vertex(Point):
    def __init__(self, context: svg_high_level.Context, x: float, y: float):
        super().__init__(context, x, y)


class ExtPoint(Point):
    def __init__(self, context: svg_high_level.Context, x: float, y: float):
        super().__init__(context, x, y)


def vertex(context: svg_high_level.Context, p: Point, is_counterterm=False):
    x, y = p.x, p.y

    size = context.line_width * 1.5

    if not is_counterterm:
        _draw_full_circle(context=context, cx=x, cy=y, r=size)
    else:
        _draw_cross(context=context, xm=x, ym=y, angle=0)


def fermion_line(context: svg_high_level.Context, p1: Point, p2: Point, is_anti_particle=False, draw_arrow=True, is_counterterm=False):
    x1, y1, x2, y2 = p1.x, p1.y, p2.x, p2.y

    _draw_line(context, x1, y1, x2, y2)

    xm = (x1 + x2) / 2
    ym = (y1 + y2) / 2

    angle = -math.atan2(y2 - y1, x2 - x1)

    if draw_arrow:
        _draw_triangle(context, xm, ym, angle, is_anti_particle)

    if is_counterterm:
        _draw_cross(context, xm, ym, angle)

    # TODO: shift the triangle if cross is placed


def boson_line(context: svg_high_level.Context, p1: Point, p2: Point, is_anti_particle=False, draw_arrow=False, is_counterterm=False):
    x1, y1, x2, y2 = p1.x, p1.y, p2.x, p2.y
    # TODO: Make wave density constant
    # TODO: Add possibility to change whether wave starts with hill or dale

    number_of_waves = 6
    shift_size = 5 * context.line_width

    distance = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
    step_size = distance / (2 * number_of_waves)

    angle = -math.atan2(y2 - y1, x2 - x1)

    context.path_init(stroke_color_rgb=context.line_color, stroke_width=context.line_width, fill_opacity=0)
    context.path_move_to(x1, y1)

    for i in range(2 * number_of_waves):
        if i % 2 == 0:
            shift = - shift_size
        else:
            shift = shift_size

        p1 = (step_size / 3, shift)
        p2 = (2 * step_size / 3, shift)
        p3 = (step_size, 0)

        p1_rotated = rotate_vector_2d(p1, angle)
        p2_rotated = rotate_vector_2d(p2, angle)
        p3_rotated = rotate_vector_2d(p3, angle)

        context.path_rel_cubic_bezier(p1_rotated[0], p1_rotated[1],
                                      p2_rotated[0], p2_rotated[1],
                                      p3_rotated[0], p3_rotated[1])

    context.path_finish()

    if draw_arrow or is_counterterm:
        xm = (x1 + x2) / 2
        ym = (y1 + y2) / 2

    if draw_arrow:
        _draw_triangle(context, xm, ym, angle, is_anti_particle)

    if is_counterterm:
        _draw_cross(context, xm, ym, angle)


def gluon_line(context: svg_high_level.Context, p1: Point, p2: Point, center=True, is_anti_particle=False, draw_arrow=False, is_counterterm=False):
    # TODO: Make loops density continuous
    x1, y1, x2, y2 = p1.x, p1.y, p2.x, p2.y

    number_of_loops = 8

    distance = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
    if center:
        step_size = distance / (number_of_loops + 2)
    else:
        step_size = distance / number_of_loops

    loop_width = step_size  # 0.05 ist ein guter Wert
    loop_height = 8 * context.line_width

    angle = -math.atan2(y2 - y1, x2 - x1)

    context.path_init(stroke_color_rgb=context.line_color, stroke_width=context.line_width, fill_opacity=0)
    context.path_move_to(x1, y1)

    if center:
        # starting connection
        ps1 = (loop_width, 0)
        ps2 = (0, - loop_height / 2)
        ps3 = (loop_width, - loop_height / 2)

        # ending connection
        pe1 = (loop_width, 0)
        pe2 = (0, loop_height / 2)
        pe3 = (loop_width, loop_height / 2)

        ps1_rotated = rotate_vector_2d(ps1, angle)
        ps2_rotated = rotate_vector_2d(ps2, angle)
        ps3_rotated = rotate_vector_2d(ps3, angle)

        pe1_rotated = rotate_vector_2d(pe1, angle)
        pe2_rotated = rotate_vector_2d(pe2, angle)
        pe3_rotated = rotate_vector_2d(pe3, angle)

    # loop first half
    pa1 = (loop_width, 0)
    pa2 = (loop_width, loop_height)
    pa3 = (loop_width / 2, loop_height)

    # loop second half
    pb1 = (- loop_width / 2, 0)
    pb2 = (- loop_width / 2, - loop_height)
    pb3 = (loop_width / 2, - loop_height)

    pa1_rotated = rotate_vector_2d(pa1, angle)
    pa2_rotated = rotate_vector_2d(pa2, angle)
    pa3_rotated = rotate_vector_2d(pa3, angle)

    pb1_rotated = rotate_vector_2d(pb1, angle)
    pb2_rotated = rotate_vector_2d(pb2, angle)
    pb3_rotated = rotate_vector_2d(pb3, angle)

    if center:
        context.path_rel_cubic_bezier(ps1_rotated[0], ps1_rotated[1],
                                      ps2_rotated[0], ps2_rotated[1],
                                      ps3_rotated[0], ps3_rotated[1])

    for i in range(number_of_loops):
        context.path_rel_cubic_bezier(pa1_rotated[0], pa1_rotated[1],
                                      pa2_rotated[0], pa2_rotated[1],
                                      pa3_rotated[0], pa3_rotated[1])
        context.path_rel_cubic_bezier(pb1_rotated[0], pb1_rotated[1],
                                      pb2_rotated[0], pb2_rotated[1],
                                      pb3_rotated[0], pb3_rotated[1])

    if center:
        context.path_rel_cubic_bezier(pe1_rotated[0], pe1_rotated[1],
                                      pe2_rotated[0], pe2_rotated[1],
                                      pe3_rotated[0], pe3_rotated[1])

    context.path_finish()

    if draw_arrow or is_counterterm:
        xm = (x1 + x2) / 2
        ym = (y1 + y2) / 2

    if draw_arrow:
        _draw_triangle(context, xm, ym, angle, is_anti_particle)

    if is_counterterm:
        _draw_cross(context, xm, ym, angle)


def scalar_line(context: svg_high_level.Context, p1: Point, p2: Point, is_anti_particle=False, draw_arrow=False, is_counterterm=False):
    # TODO: Maybe use stroke dasharray instead
    x1, y1, x2, y2 = p1.x, p1.y, p2.x, p2.y

    number_of_dashes = 6

    distance = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
    step_size = distance / (2 * number_of_dashes - 1)

    angle = -math.atan2(y2 - y1, x2 - x1)

    context.path_init(stroke_color_rgb=context.line_color, stroke_width=context.line_width, fill_opacity=0)
    context.path_move_to(x1, y1)

    for i in range(2 * number_of_dashes - 1):
        p = (step_size, 0)

        p_rotated = rotate_vector_2d(p, angle)

        if i % 2 == 1:
            context.path_rel_move_to(p_rotated[0], p_rotated[1])
        else:
            context.path_rel_line_to(p_rotated[0], p_rotated[1])

    context.path_finish()

    if draw_arrow or is_counterterm:
        xm = (x2 + x1) / 2
        ym = (y2 + y1) / 2

    if draw_arrow:
        _draw_triangle(context, xm, ym, angle, is_anti_particle)
    if is_counterterm:
        _draw_cross(context, xm, ym, angle)


def ghost_line(context: svg_high_level.Context, p1: Point, p2: Point, is_anti_particle=False, draw_arrow=True, is_counterterm=False):
    x1, y1, x2, y2 = p1.x, p1.y, p2.x, p2.y

    number_of_dots = 20

    distance = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
    step_size = distance / number_of_dots

    angle = -math.atan2(y2 - y1, x2 - x1)

    current_position_x = x1
    current_position_y = y1

    for i in range(number_of_dots):
        p = (step_size, 0)

        p_rotated = rotate_vector_2d(p, angle)

        current_position_x += p_rotated[0]
        current_position_y += p_rotated[1]

        _draw_full_circle(context, current_position_x, current_position_y, context.line_width * 0.5)

    if draw_arrow or is_counterterm:
        xm = (x1 + x2) / 2
        ym = (y1 + y2) / 2

    if draw_arrow:
        _draw_triangle(context, xm, ym, angle, is_anti_particle=is_anti_particle)

    if is_counterterm:
        _draw_cross(context, xm, ym, angle)


def double_line(context: svg_high_level.Context, p1: Point, p2: Point, is_anti_particle=False, draw_arrow=False, is_counterterm=False):
    x1, y1, x2, y2 = p1.x, p1.y, p2.x, p2.y

    shift = 1.5 * context.line_width

    # TODO: Shift is here hardcoded in y !!! this must also respect the angle of the line!

    _draw_line(context, x1, y1 + shift / 2, x2, y2 + shift / 2)
    _draw_line(context, x1, y1 - shift / 2, x2, y2 - shift / 2)

    if draw_arrow or is_counterterm:
        angle = -math.atan2(y2 - y1, x2 - x1)

        xm = (x1 + x2) / 2
        ym = (y1 + y2) / 2

    if draw_arrow:
        _draw_triangle(context, xm, ym, angle, is_anti_particle)

    if is_counterterm:
        _draw_cross(context, xm, ym, angle)


def rotate_vector_2d(vec_in, angle):
    x_out = math.cos(angle) * vec_in[0] + math.sin(angle) * vec_in[1]
    y_out = - math.sin(angle) * vec_in[0] + math.cos(angle) * vec_in[1]

    vec_out = (x_out, y_out)

    return vec_out


def draw_arrow(context: svg_high_level.Context, p1: Point, p2: Point):
    x1, y1, x2, y2 = p1.x, p1.y, p2.x, p2.y
    angle = -math.atan2(y2 - y1, x2 - x1)

    _draw_line(context, x1, y1, x2, y2)
    _draw_triangle(context, x2, y2, angle=angle, is_anti_particle=False)


def draw_circle(context: svg_high_level.Context, p: Point, radius: float, line_width: float = None,
                line_color: tuple[float, float, float] = None, fill_color: tuple[float, float, float] = None,
                fill_opacity: float = None, line_opacity: float = None):
    cx, cy = p.x, p.y

    _draw_full_circle(context, cx=cx, cy=cy, r=radius, line_width=line_width, line_color=line_color,
                      fill_color=fill_color, fill_opacity=fill_opacity, line_opacity=line_opacity)


def grid(context: svg_high_level.Context):
    # vertical lines
    for x in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
        _draw_line(context,
                   x * context.scaling_x, 0 * context.scaling_y,
                   x * context.scaling_x, 1 * context.scaling_y,
                   line_color=(100, 100, 100),
                   line_width=1)

        draw_text(context, str(x), x=x+0.01, y=0.04, fontsize=8)

    # horizontal lines
    for y in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
        _draw_line(context,
                   0 * context.scaling_x, y * context.scaling_y,
                   1 * context.scaling_x, y * context.scaling_y,
                   line_color=(100, 100, 100),
                   line_width=1)

        draw_text(context, str(y), x=0.01, y=y+0.02, fontsize=8)
