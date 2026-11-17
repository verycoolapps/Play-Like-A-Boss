bl_info = {
    "name": "Building Room Viewer",
    "blender": (4, 0, 0),
    "version": (1, 0, 0),
    "location": "View3D > Sidebar > Room Viewer",
    "description": "Navigate and inspect building rooms with interactive camera control",
    "author": "VeryCoolApps - PLAB",
    "category": "3D View",
}

import bpy
from bpy.props import (
    StringProperty,
    BoolProperty,
    FloatProperty,
    EnumProperty,
)
from bpy.types import (
    Panel,
    Operator,
    PropertyGroup,
)

from . import room_detector, camera_controller, ui_panel

classes = (
    ui_panel.ROOM_VIEWER_PT_panel,
    ui_panel.ROOM_VIEWER_OT_refresh_rooms,
    ui_panel.ROOM_VIEWER_OT_goto_room,
    ui_panel.ROOM_VIEWER_OT_show_all_rooms,
    ui_panel.ROOM_VIEWER_OT_camera_orbit,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.room_viewer_props = bpy.props.PointerProperty(
        type=ui_panel.RoomViewerProperties
    )


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    if hasattr(bpy.types.Scene, "room_viewer_props"):
        del bpy.types.Scene.room_viewer_props


if __name__ == "__main__":
    register()
