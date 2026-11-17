"""
UI Panel for Room Viewer add-on.
Provides interface to select and navigate between rooms.
"""

import bpy
from bpy.types import Panel, Operator, PropertyGroup
from bpy.props import StringProperty, BoolProperty, FloatProperty, EnumProperty

from . import room_detector, camera_controller


class RoomViewerProperties(PropertyGroup):
    """Properties for room viewer state."""

    current_room: StringProperty(
        name="Current Room",
        description="Currently selected room",
        default="",
    )

    show_all_rooms: BoolProperty(
        name="Show All Rooms",
        description="Display overview of all rooms",
        default=False,
    )

    zoom_factor: FloatProperty(
        name="Zoom Factor",
        description="How far to zoom out from room",
        default=1.5,
        min=0.5,
        max=5.0,
    )

    camera_elevation: FloatProperty(
        name="Camera Elevation",
        description="Camera elevation angle in degrees",
        default=45,
        min=-90,
        max=90,
    )


class ROOM_VIEWER_PT_panel(Panel):
    """Main room viewer panel."""

    bl_label = "Room Viewer"
    bl_idname = "VIEW3D_PT_room_viewer"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Room Viewer"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        props = scene.room_viewer_props

        # Refresh button
        layout.operator("wm.room_viewer_refresh_rooms", text="Refresh Rooms", icon="FILE_REFRESH")

        # Title
        layout.label(text="Building Navigation", icon="OUTLINER")

        # Show all rooms button
        col = layout.column(align=True)
        col.operator("wm.room_viewer_show_all_rooms", text="📍 View All Rooms", icon="CAMERA_DATA")

        # Rooms list
        layout.label(text="Select Room:", icon="BOOKMARKS")

        # Get rooms
        detector = room_detector.detect_rooms(scene)
        rooms = detector.get_room_names()

        if rooms:
            col = layout.column(align=True)
            for room_name in rooms:
                is_selected = props.current_room == room_name
                icon = "CHECKMARK" if is_selected else "BLANK1"
                col.operator(
                    "wm.room_viewer_goto_room",
                    text=f"{icon} {room_name}",
                    depress=is_selected,
                ).room_name = room_name
        else:
            layout.label(text="No rooms detected", icon="ERROR")
            layout.label(text='Create collections named "Room.Name"', icon="INFO")

        # Camera settings
        layout.separator()
        layout.label(text="Camera Settings:", icon="CAMERA_DATA")
        layout.prop(props, "zoom_factor")
        layout.prop(props, "camera_elevation")

        # View options
        layout.separator()
        layout.label(text="Quick Views:", icon="WINDOW")
        col = layout.column(align=True)
        col.operator("wm.room_viewer_camera_orbit", text="Orbit Left").angle = -45
        col.operator("wm.room_viewer_camera_orbit", text="Orbit Right").angle = 45

        # Info
        if rooms:
            layout.separator()
            layout.label(text=f"Total rooms: {len(rooms)}", icon="INFO")
            if props.current_room and props.current_room in rooms:
                room = detector.get_room(props.current_room)
                if room:
                    layout.label(text=f"Room size: {room.size.length:.2f}m", icon="RULER")


class ROOM_VIEWER_OT_refresh_rooms(Operator):
    """Refresh room list from scene."""

    bl_idname = "wm.room_viewer_refresh_rooms"
    bl_label = "Refresh Rooms"

    def execute(self, context):
        scene = context.scene
        detector = room_detector.detect_rooms(scene)
        rooms = detector.get_room_names()

        if rooms:
            self.report({"INFO"}, f"Found {len(rooms)} rooms: {', '.join(rooms)}")
        else:
            self.report({"WARNING"}, "No rooms detected in scene")

        return {"FINISHED"}


class ROOM_VIEWER_OT_goto_room(Operator):
    """Navigate to a specific room."""

    bl_idname = "wm.room_viewer_goto_room"
    bl_label = "Go to Room"
    bl_options = {"REGISTER", "UNDO"}

    room_name: StringProperty(name="Room Name", default="")

    def execute(self, context):
        scene = context.scene
        props = scene.room_viewer_props

        detector = room_detector.detect_rooms(scene)
        room = detector.get_room(self.room_name)

        if not room:
            self.report({"ERROR"}, f"Room '{self.room_name}' not found")
            return {"CANCELLED"}

        # Move camera to room
        cam_controller = camera_controller.CameraController(scene)
        cam_controller.focus_on_room(room, props.zoom_factor, props.camera_elevation)

        # Update current room
        props.current_room = self.room_name
        props.show_all_rooms = False

        self.report({"INFO"}, f"Navigated to room: {self.room_name}")
        return {"FINISHED"}


class ROOM_VIEWER_OT_show_all_rooms(Operator):
    """Show overview of all rooms."""

    bl_idname = "wm.room_viewer_show_all_rooms"
    bl_label = "Show All Rooms"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        scene = context.scene
        props = scene.room_viewer_props

        detector = room_detector.detect_rooms(scene)

        if not detector.rooms:
            self.report({"ERROR"}, "No rooms found in scene")
            return {"CANCELLED"}

        # Move camera to show entire building
        cam_controller = camera_controller.CameraController(scene)
        cam_controller.focus_on_building(detector, zoom_factor=2.0)

        props.show_all_rooms = True
        props.current_room = ""

        self.report({"INFO"}, f"Showing all {len(detector.rooms)} rooms")
        return {"FINISHED"}


class ROOM_VIEWER_OT_camera_orbit(Operator):
    """Orbit camera around current view."""

    bl_idname = "wm.room_viewer_camera_orbit"
    bl_label = "Orbit Camera"
    bl_options = {"REGISTER", "UNDO"}

    angle: FloatProperty(
        name="Angle",
        description="Rotation angle in degrees",
        default=45,
    )

    def execute(self, context):
        scene = context.scene
        cam_controller = camera_controller.CameraController(scene)
        cam_controller.orbit_camera(self.angle)

        direction = "left" if self.angle < 0 else "right"
        self.report({"INFO"}, f"Orbited camera {direction}")
        return {"FINISHED"}
