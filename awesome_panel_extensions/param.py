"""This module contains functionality to improve the param module"""
from typing import Tuple, Union

import param
from param.parameterized import Watcher


def link(
    source: param.Parameter, target: param.Parameter, bidirectionally: bool = True
) -> Union[Watcher, Tuple[Watcher, Watcher]]:
    """If bidirectionally is True (default) then links the target Parameter to the source Parameter
    and vice versa. Returns the (source Watcher, target Watcher).

    If bidirectionally is False then links the target Parameter to the source Parameter and
    returns the Watcher.

    Args:
        source (param.Parameter): The source Parameter
        target (param.Parameter): The target Parameter
        bidirectionally (bool, optional): Whether or not to link bidirectionally. Defaults to True.

    Returns:
        Union[Tuple[Watcher, Watcher], Watcher]: The (source Watcher, target Watcher) or
            source Watcher
    """

    def update_target(*_):
        source_value = getattr(source.owner, source.name)
        target_value = getattr(target.owner, target.name)
        if source_value != target_value:
            setattr(target.owner, target.name, source_value)

    source_watcher = source.owner.param.watch(update_target, source.name)
    if bidirectionally:
        target_watcher = link(source=target, target=source, bidirectionally=False)
        return (source_watcher, target_watcher)
    return source_watcher
