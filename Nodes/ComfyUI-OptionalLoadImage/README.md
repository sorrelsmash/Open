# ComfyUI Optional Load Image

An image loader with an explicit `(none)` option.

## Install

Run in your ComfyUI custom_nodes directory:

```bash
cd /workspace/ComfyUI/custom_nodes
git clone https://github.com/sorrelsmash/Open.git ComfyUI-OptionalLoadImage
```

If ComfyUI is installed elsewhere, adjust the first path. Restart ComfyUI and search for **Optional Load Image**.

The repository root loader exposes the node stored in `Nodes/ComfyUI-OptionalLoadImage`. The clone also includes the repository's other files. Additional Python packages are not required; the node uses ComfyUI's torch, numpy and Pillow.

## Usage

- Select an image to output IMAGE and MASK tensors.
- Select `(none)` to return `None` on both ports.
- Missing files also return `None`.

Downstream nodes must support `None`. Standard nodes expecting image tensors may fail if connected to an empty output. This node does not universally skip dependent workflow branches.

## Update

From the cloned repository directory, run:

```bash
git pull --ff-only
```

Restart ComfyUI after updating.
