import cairo
import math


def color(ctx: cairo.Context, fill: bool, red: float, green: float, blue: float, alpha: float):
    ctx.set_source_rgba(red, green, blue, alpha)
    if fill is True:
        ctx.fill()
    else:
        ctx.stroke()


def gradient(ctx: cairo.Context, fill: bool, pattern: cairo.Pattern):
    ctx.set_source(pattern)
    if fill is True:
        ctx.fill()
    else:
        ctx.stroke()


def rectangle(ctx: cairo.Context, x: float, y: float, width: float, height: float):
    ctx.rectangle(x, y, width, height)


def circle(ctx: cairo.Context, x:  float, y: float, radius: float, angle1: float, angle2: float):
    ctx.arc(x, y, radius, math.radians(angle1), math.radians(angle2))

# def polygon(ctx: cairo.Context, x: float, y: float, sides: int, edge_length: float):
#     ctx.move_to(x, y)
#     for i in range(0, sides):
#         ctx.line_to()
#
# def rotate(origin, point, angle):
#     """
#     Rotate a point counterclockwise by a given angle around a given origin.
#
#     The angle should be given in radians.
#     """
#     ox, oy = origin
#     px, py = point
#
#     qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
#     qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
#     return qx, qy