from subprocess import check_call

def update_submodule(
    name: str|None = None,
    *,
    force: bool = False, 
    remote: bool = False,
    recurse: bool = True,
) -> None:
    
    args = ['git', 'submodule', 'update', '--init']

    if recurse: args += ['--recursive']
    if remote: args += ['--remote']
    if force:  args += ['--force']
    if name:   args += [name]

    check_call(args)

