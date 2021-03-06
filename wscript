# -*- python -*-

import waflib.Logs as msg

PACKAGE = {
    'name': 'pkg-ac',
    'author': 'hwaf collaboration',
}

def pkg_deps(ctx):
    ctx.use_pkg('pkg-aa')
    ctx.use_pkg('pkg-ab')
    return

def configure(ctx):
    return

def build(ctx):
    ctx(
        features="cxx cxxprogram",
        name="pkg-ac",
        source="src/pkg-ac.cxx",
        target="pkg-ac",
        use="ROOT pkg-aa pkg-ab",
        )

    return

def install(ctx):
    return
