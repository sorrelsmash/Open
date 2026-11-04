"""Expose Optional Load Image when this repository is cloned into custom_nodes."""

import importlib.util
from pathlib import Path

_node_path = Path(__file__).resolve().parent / "Nodes" / "ComfyUI-OptionalLoadImage" / "__init__.py"
_spec = importlib.util.spec_from_file_location("_open_optional_load_image", _node_path)
if _spec is None or _spec.loader is None:
    raise ImportError(f"Cannot load Optional Load Image from {_node_path}")
_node = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_node)

NODE_CLASS_MAPPINGS = _node.NODE_CLASS_MAPPINGS
NODE_DISPLAY_NAME_MAPPINGS = _node.NODE_DISPLAY_NAME_MAPPINGS

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
