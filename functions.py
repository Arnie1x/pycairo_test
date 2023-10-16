import cairo


def color(ctx, fill, red, green, blue, alpha):
    ctx.set_source_rgba(0.4, 0.6, 1, 1)
    if fill is True:
        ctx.fill()
    else:
        ctx.stroke()


def gradient(ctx, fill, gradient_):
    ctx.set_source(gradient_)
    if fill is True:
        ctx.fill()
    else:
        ctx.stroke()


def rectangle(ctx, x, y, length, width):
    ctx.rectangle(x, y, length, width)

