import bpy
import os
import bpy_extras


def convertFileNameToPanda(filename):
    """
    (Get from Chicken) Converts Blender filenames to Panda 3D filenames.
    """
    path = filename.replace('//', './').replace('\\', '/')
    if os.name == 'nt' and path.find(':') != -1:
        path = '/' + path[0].lower() + path[2:]
    return path


def save_image(img, file_path, text_path):
    # If we don't have any data for our image there is no point trying to save it
    # Happens when there are broken image paths in file somewhere
    if not img.has_data:
        return

    if img.filepath:
        old_path = bpy.path.abspath(img.filepath)
        old_dir, old_file = os.path.split(convertFileNameToPanda(old_path))
        filenames = [s.lower() for s in old_file.split('.')]
        if not filenames[-1] in ('jpg', 'png', 'tga', 'tiff', 'dds', 'bmp') and img.is_dirty:
            old_file += ('.' + bpy.context.scene.render.image_settings.file_format.lower())
    else:
        old_path = ''
        old_file = img.name + '.' + bpy.context.scene.render.image_settings.file_format.lower()

    rel_path = os.path.join(text_path, old_file)
    if os.name == 'nt':
        rel_path = rel_path.replace(r"\\", r"/").replace('\\', '/')

    new_dir, eg_f = os.path.split(file_path)
    new_dir = os.path.abspath(os.path.join(new_dir, text_path))
    render_path = os.path.abspath(os.path.join(new_dir, old_file))

    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
        img.save_render(render_path)

    if not os.path.exists(new_dir) and img.is_dirty or bool(img.packed_file):
        try:
            bpy.context.scene.render.image_settings.color_mode = 'RGBA'
        except:
            bpy.context.scene.render.image_settings.color_mode = 'RGB'
        render_path = os.path.abspath(os.path.join(new_dir, old_file))

        img.save_render(render_path)
        print('RENDER IMAGE to %s; rel path: %s' % (render_path, rel_path))
    else:
        new_path = os.path.join(new_dir, old_file)
        if old_path != new_path:
            bpy_extras.io_utils.path_reference_copy(((old_path.replace(r"\\", r"/"), new_path),), report = print)
            print('COPY IMAGE %s to %s; rel path %s' % (old_path, new_path, rel_path))
    return rel_path


def get_active_uv(obj):
    auv = [uv for uv in obj.data.uv_layers if uv.active]
    if auv:
        return auv[0]


def eggSafeName(s):
    """
    (Get from Chicken) Function that converts names into something
    suitable for the egg file format - simply puts quotations around names that
    contain spaces and prunes bad characters, replacing them with an
    underscore.
    """
    s = str(s).replace('"', '_')  # Sure there are more bad characters, but this will do for now.
    if ' ' in s:
        return '"' + s + '"'
    else:
        return s


def node_debugger(anylist):
    if anylist and isinstance(anylist, list):
        print("Links:\n")
        print([iterator.to_node.name for iterator in anylist.links])
        print("AND\n")
        print("Nodes:\n")
        print([iterator.to_node.name for iterator in anylist.nodes])
