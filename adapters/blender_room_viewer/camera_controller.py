"""
Camera automation for room navigation.
Provides smooth camera movement to rooms with configurable viewing angles.
"""

import bpy
from mathutils import Vector
from . import room_detector


class CameraController:
    """Controls camera movement and positioning."""

    def __init__(self, scene: bpy.types.Scene):
        self.scene = scene
        self.camera = scene.camera
        if not self.camera:
            # Create default camera if none exists
            cam_data = bpy.data.cameras.new("Camera")
            self.camera = bpy.data.objects.new("Camera", cam_data)
            self.scene.collection.objects.link(self.camera)
            self.scene.camera = self.camera

    def focus_on_room(self, room: room_detector.Room, zoom_factor: float = 1.5, elevation: float = 45):
        """
        Move camera to focus on a room.

        Args:
            room: Room object to focus on
            zoom_factor: How far to zoom out (1.5 = 50% farther than bounds)
            elevation: Camera elevation angle in degrees
        """
        center = room.center
        size = room.size
        max_dim = max(size.x, size.y, size.z)

        # Calculate camera distance based on room size and zoom factor
        distance = max_dim * zoom_factor

        # Set camera position (45 degree angle)
        import math

        rad_elev = math.radians(elevation)
        rad_azim = math.radians(45)

        cam_x = center.x + distance * math.cos(rad_azim) * math.cos(rad_elev)
        cam_y = center.y + distance * math.sin(rad_azim) * math.cos(rad_elev)
        cam_z = center.z + distance * math.sin(rad_elev)

        self.camera.location = Vector((cam_x, cam_y, cam_z))

        # Point camera at room center
        direction = center - self.camera.location
        self.camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()

    def focus_on_building(self, detector: room_detector.RoomDetector, zoom_factor: float = 2.0):
        """
        Move camera to show entire building.

        Args:
            detector: RoomDetector instance
            zoom_factor: How far to zoom out from building bounds
        """
        center = detector.get_building_center()
        min_b, max_b = detector.get_building_bounds()
        size = max_b - min_b
        max_dim = max(size.x, size.y, size.z)

        distance = max_dim * zoom_factor

        import math

        rad_elev = math.radians(35)
        rad_azim = math.radians(45)

        cam_x = center.x + distance * math.cos(rad_azim) * math.cos(rad_elev)
        cam_y = center.y + distance * math.sin(rad_azim) * math.cos(rad_elev)
        cam_z = center.z + distance * math.sin(rad_elev)

        self.camera.location = Vector((cam_x, cam_y, cam_z))

        direction = center - self.camera.location
        self.camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()

    def orbit_camera(self, angle_degrees: float, speed: float = 0.5):
        """
        Rotate camera around current target in horizontal plane.

        Args:
            angle_degrees: Angle to rotate in degrees
            speed: Animation speed factor
        """
        import math

        # Get current camera position relative to world origin
        cam_pos = self.camera.location
        rot_euler = self.camera.rotation_euler

        # For now, just rotate around world Z axis
        # TODO: Calculate actual target and orbit around it
        rad = math.radians(angle_degrees)
        x = cam_pos.x * math.cos(rad) - cam_pos.y * math.sin(rad)
        y = cam_pos.x * math.sin(rad) + cam_pos.y * math.cos(rad)

        self.camera.location.x = x
        self.camera.location.y = y

    def set_view_top(self):
        """Set camera to top-down orthographic view."""
        self.camera.type = "ORTHO"
        self.camera.ortho_scale = 50
        self.camera.location = (0, 0, 100)
        self.camera.rotation_euler = (0, 0, 0)

    def set_view_front(self):
        """Set camera to front view."""
        self.camera.type = "PERSP"
        self.camera.location = (0, -50, 10)
        self.camera.rotation_euler = (1.57, 0, 0)  # 90 degrees pitch

    def set_view_side(self):
        """Set camera to side view."""
        self.camera.type = "PERSP"
        self.camera.location = (50, 0, 10)
        self.camera.rotation_euler = (1.57, 0, 1.57)


def get_camera_controller(scene: bpy.types.Scene) -> CameraController:
    """Get or create camera controller for scene."""
    return CameraController(scene)
