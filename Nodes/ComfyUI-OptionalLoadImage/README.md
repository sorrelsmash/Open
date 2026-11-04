# ComfyUI Optional Load Image

Image loader with an explicit `(none)` option.

## Install

The node source is stored in `Nodes/ComfyUI-OptionalLoadImage` on `main`.
The installation branch contains only the node files at its root.

```bash
cd /workspace/ComfyUI/custom_nodes
git clone --depth 1 --single-branch -b codex/optional-load-image https://github.com/sorrelsmash/Open.git ComfyUI-OptionalLoadImage
```

Adjust the ComfyUI path if needed. Restart ComfyUI and search for **Optional Load Image**.
If installed manually, copy the entire `Nodes/ComfyUI-OptionalLoadImage` folder into `ComfyUI/custom_nodes`.

## Usage

- Select an image to output IMAGE and MASK tensors.
- Select `(none)` to return `None` on both ports.
- Missing files also return `None`.

Downstream nodes must support `None`; ordinary nodes expecting tensors may fail on an empty output. This node does not universally skip dependent workflow branches.

Uses ComfyUI's existing torch, numpy and Pillow dependencies. No additional packages needed.

## Update

Run `git pull --ff-only` from the installed node folder, then restart ComfyUI.
The installation branch must be updated separately when the source on main changes.
