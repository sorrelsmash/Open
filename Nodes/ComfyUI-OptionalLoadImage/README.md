# ComfyUI Optional Load Image

A standard-style image loader with an explicit `(none)` option.

- Select an image to output regular `IMAGE` and `MASK` tensors.
- Select `(none)` to output `None` on both ports, without a loader error.
- Missing files also return `None`.
- Independent branches continue to execute.

**Important:** Downstream nodes must support `None` or skip the optional branch. A standard node that expects an actual tensor may fail when receiving `None`. ComfyUI does not provide a universal mechanism for skipping an arbitrary connected node while continuing its dependent outputs.

## Install

```bash
cd /path/to/ComfyUI/custom_nodes
git clone https://github.com/YOUR_USERNAME/ComfyUI-OptionalLoadImage.git
```

Restart ComfyUI. Search for **Optional Load Image**.

## Dependencies

Uses ComfyUI's existing `torch`, `numpy`, and `Pillow` dependencies. No additional packages needed.
