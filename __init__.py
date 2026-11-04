import os
import numpy as np
import torch
from PIL import Image, ImageOps

import folder_paths


class OptionalLoadImage:
    """Image loader that returns None when no image is selected."""

    @classmethod
    def INPUT_TYPES(cls):
        # ComfyUI's standard input folder is not a registered model folder.
        files = []
        input_dir = folder_paths.get_input_directory()
        for root, _, names in os.walk(input_dir):
            for name in names:
                if name.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.bmp', '.gif')):
                    files.append(os.path.relpath(os.path.join(root, name), input_dir).replace('\\', '/'))
        return {'required': {'image': (['(none)'] + sorted(files), {'image_upload': True})}}

    RETURN_TYPES = ('IMAGE', 'MASK')
    RETURN_NAMES = ('image', 'mask')
    FUNCTION = 'load_image'
    CATEGORY = 'image'

    def load_image(self, image):
        if not image or image == '(none)':
            return (None, None)
        path = folder_paths.get_annotated_filepath(image)
        if not os.path.isfile(path):
            return (None, None)
        with Image.open(path) as source:
            frame = ImageOps.exif_transpose(source)
            rgb = frame.convert('RGB')
            image_tensor = torch.from_numpy(np.array(rgb).astype(np.float32) / 255.0)[None,]
            if 'A' in frame.getbands():
                mask = 1.0 - torch.from_numpy(np.array(frame.getchannel('A')).astype(np.float32) / 255.0)
            else:
                mask = torch.zeros((rgb.height, rgb.width), dtype=torch.float32)
            return (image_tensor, mask.unsqueeze(0))

    @classmethod
    def IS_CHANGED(cls, image):
        if not image or image == '(none)':
            return '(none)'
        path = folder_paths.get_annotated_filepath(image)
        if not os.path.isfile(path):
            return '(missing)'
        return os.path.getmtime(path)

    @classmethod
    def VALIDATE_INPUTS(cls, image):
        return True


NODE_CLASS_MAPPINGS = {'OptionalLoadImage': OptionalLoadImage}
NODE_DISPLAY_NAME_MAPPINGS = {'OptionalLoadImage': 'Optional Load Image'}
