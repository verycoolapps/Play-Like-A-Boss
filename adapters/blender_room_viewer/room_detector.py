"""
Room detection from Blender scene structure.
Supports multiple naming conventions:
- Collections: "Room.Kitchen", "Room.Bedroom", etc
- Objects with "room_" prefix
- Collections named directly: "Kitchen", "Bedroom", etc
"""

import bpy
from mathutils import Vector
from typing import List, Dict, Tuple


class Room:
    """Represents a single room/space in the building."""

    def __init__(self, name: str, objects: List[bpy.types.Object], collection=None):
        self.name = name
        self.objects = objects
        self.collection = collection
        self._bounds = None
        self._center = None

    @property
    def bounds(self) -> Tuple[Vector, Vector]:
        """Get min/max bounds of all objects in room."""
        if self._bounds is None:
            if not self.objects:
                self._bounds = (Vector((0, 0, 0)), Vector((0, 0, 0)))
            else:
                min_coords = [float("inf")] * 3
                max_coords = [float("-inf")] * 3

                for obj in self.objects:
                    if obj.type in ("MESH", "CURVE", "SURFACE"):
                        for vertex in obj.data.vertices if hasattr(obj.data, "vertices") else []:
                            world_pos = obj.matrix_world @ vertex.co
                            for i in range(3):
                                min_coords[i] = min(min_coords[i], world_pos[i])
                                max_coords[i] = max(max_coords[i], world_pos[i])

                self._bounds = (Vector(min_coords), Vector(max_coords))

        return self._bounds

    @property
    def center(self) -> Vector:
        """Get center of room bounds."""
        if self._center is None:
            min_b, max_b = self.bounds
            self._center = (min_b + max_b) / 2
        return self._center

    @property
    def size(self) -> Vector:
        """Get dimensions of room."""
        min_b, max_b = self.bounds
        return max_b - min_b

    def __repr__(self):
        return f"<Room '{self.name}' center={self.center} size={self.size}>"


class RoomDetector:
    """Detects and manages rooms in a Blender scene."""

    def __init__(self, scene: bpy.types.Scene):
        self.scene = scene
        self.rooms: Dict[str, Room] = {}
        self.detect_rooms()

    def detect_rooms(self):
        """Detect rooms from scene structure."""
        self.rooms.clear()

        # Method 1: Collections starting with "Room."
        for collection in self.scene.collection.children:
            if collection.name.startswith("Room."):
                room_name = collection.name[5:]  # Remove "Room." prefix
                self._add_room_from_collection(room_name, collection)
            elif collection.name[0].isupper() and not collection.name.startswith("Room"):
                # Method 2: Capitalized collections (Room names)
                self._add_room_from_collection(collection.name, collection)

        # Method 3: Objects with "room_" prefix in root collection
        for obj in self.scene.collection.objects:
            if obj.name.startswith("room_"):
                room_name = obj.name[5:]
                if room_name not in self.rooms:
                    self.rooms[room_name] = Room(room_name, [obj])

    def _add_room_from_collection(self, room_name: str, collection: bpy.types.Collection):
        """Create a room from a collection."""
        objects = self._get_collection_objects(collection)
        if objects:  # Only add if collection has objects
            self.rooms[room_name] = Room(room_name, objects, collection)

    def _get_collection_objects(self, collection: bpy.types.Collection, recursive=True) -> List[bpy.types.Object]:
        """Get all objects in a collection."""
        objects = list(collection.objects)
        if recursive:
            for sub_collection in collection.children:
                objects.extend(self._get_collection_objects(sub_collection))
        return objects

    def get_room_names(self) -> List[str]:
        """Get sorted list of room names."""
        return sorted(self.rooms.keys())

    def get_room(self, name: str) -> Room:
        """Get room by name."""
        return self.rooms.get(name)

    def get_all_rooms(self) -> List[Room]:
        """Get all rooms sorted by name."""
        return [self.rooms[name] for name in self.get_room_names()]

    def get_building_bounds(self) -> Tuple[Vector, Vector]:
        """Get bounds of entire building."""
        if not self.rooms:
            return Vector((0, 0, 0)), Vector((0, 0, 0))

        all_min = [float("inf")] * 3
        all_max = [float("-inf")] * 3

        for room in self.rooms.values():
            min_b, max_b = room.bounds
            for i in range(3):
                all_min[i] = min(all_min[i], min_b[i])
                all_max[i] = max(all_max[i], max_b[i])

        return Vector(all_min), Vector(all_max)

    def get_building_center(self) -> Vector:
        """Get center of entire building."""
        min_b, max_b = self.get_building_bounds()
        return (min_b + max_b) / 2


def detect_rooms(scene: bpy.types.Scene) -> RoomDetector:
    """Convenience function to detect rooms in scene."""
    return RoomDetector(scene)
