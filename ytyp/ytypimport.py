import bpy
from ..cwxml import ytyp as ytypxml, ymap as ymapxml
from ..sollumz_properties import ArchetypeType, AssetType, EntityLodLevel, EntityPriorityLevel
from .properties.ytyp import CMapTypesProperties, ArchetypeProperties, TimecycleModifierProperties, RoomProperties, PortalProperties, MloEntityProperties


def create_mlo_tcm(tcm_xml: ytypxml.TimeCycleModifier, archetype: ArchetypeProperties):
    """Create an mlo timecycle modifier from an xml for the provided archetype data-block."""

    tcm: TimecycleModifierProperties = archetype.new_tcm()
    tcm.name = tcm_xml.name
    tcm.sphere = tcm_xml.sphere
    tcm.percentage = tcm_xml.percentage
    tcm.range = tcm_xml.range
    tcm.start_hour = tcm_xml.start_hour
    tcm.end_hour = tcm_xml.end_hour


def create_mlo_portal(portal_xml: ytypxml.Portal, archetype: ArchetypeProperties):
    """Create an mlo portal from an xml for the provided archetype data-block."""

    portal: PortalProperties = archetype.new_portal()
    for index, corner in enumerate(portal_xml.corners):
        setattr(portal, f"corner{index + 1}", corner.value)
    portal.room_from_id = archetype.rooms[portal_xml.room_from].id
    portal.room_to_id = archetype.rooms[portal_xml.room_to].id
    portal.flags.total = str(portal_xml.flags)
    portal.mirror_priority = portal_xml.mirror_priority
    portal.opacity = portal_xml.opacity
    portal.audio_occlusion = str(
        portal_xml.audio_occlusion)
    for index in portal_xml.attached_objects:
        archetype.entities[index].attached_portal_id = portal.id


def create_mlo_room(room_xml: ytypxml.Room, archetype: ArchetypeProperties):
    """Create an mlo room from an xml for the provided archetype data-block."""

    room: RoomProperties = archetype.new_room()
    room.name = room_xml.name
    room.bb_min = room_xml.bb_min
    room.bb_max = room_xml.bb_max
    room.blend = room_xml.blend
    room.timecycle = room_xml.timecycle_name
    room.secondary_timecycle = room_xml.secondary_timecycle_name
    room.flags.total = str(room_xml.flags)
    room.floor_id = room_xml.floor_id
    room.exterior_visibility_depth = room_xml.exterior_visibility_depth
    for index in room_xml.attached_objects:
        archetype.entities[index].attached_room_id = room.id


def find_and_link_entity_object(entity_xml: ymapxml.EntityItem, entity: MloEntityProperties):
    """Atempt to find an existing entity object in the scene and link it to the entity data-block."""

    for obj in bpy.context.collection.all_objects:
        if entity_xml.archetype_name == obj.name and obj.name in bpy.context.view_layer.objects:
            entity.linked_object = obj


def create_mlo_entity(entity_xml: ymapxml.EntityItem, archetype: ArchetypeProperties):
    """Create an mlo entity from an xml for the provided archetype data-block."""

    entity: MloEntityProperties = archetype.new_entity()
    entity.position = entity_xml.position
    entity.rotation = entity_xml.rotation.inverted()
    entity.scale_xy = entity_xml.scale_xy
    entity.scale_z = entity_xml.scale_z

    find_and_link_entity_object(entity_xml, entity)

    entity.archetype_name = entity_xml.archetype_name
    entity.flags.total = str(entity_xml.flags)
    entity.guid = entity_xml.guid
    entity.parent_index = entity_xml.parent_index
    entity.lod_dist = entity_xml.lod_dist
    entity.child_lod_dist = entity_xml.child_lod_dist
    entity.lod_level = EntityLodLevel[entity_xml.lod_level]
    entity.priority_level = EntityPriorityLevel[entity_xml.priority_level]
    entity.num_children = entity_xml.num_children
    entity.ambient_occlusion_multiplier = entity_xml.ambient_occlusion_multiplier
    entity.artificial_ambient_occlusion = entity_xml.artificial_ambient_occlusion
    entity.tint_value = entity_xml.tint_value


def create_mlo_archetype_children(archetype_xml: ytypxml.MloArchetype, archetype: ArchetypeProperties):
    """Create entities, rooms, portals, and timecylce modifiers for an mlo archetype."""

    for entity_xml in archetype_xml.entities:
        create_mlo_entity(entity_xml, archetype)

    for room_xml in archetype_xml.rooms:
        create_mlo_room(room_xml, archetype)

    for portal_xml in archetype_xml.portals:
        create_mlo_portal(portal_xml, archetype)

    for tcm_xml in archetype_xml.timecycle_modifiers:
        create_mlo_tcm(tcm_xml, archetype)


def find_and_set_archetype_asset(archetype: ArchetypeProperties):
    """Atempt to find an existing archetype asset in the scene and set it as the current asset."""

    for obj in bpy.context.scene.collection.all_objects:
        if obj.name == archetype.asset_name:
            archetype.asset = obj


def get_asset_type_enum(xml_asset_type: str) -> str:
    """Get asset type enum based on xml asset type string."""

    if xml_asset_type == "ASSET_TYPE_UNINITIALIZED":
        return AssetType.UNITIALIZED
    elif xml_asset_type == "ASSET_TYPE_FRAGMENT":
        return AssetType.FRAGMENT
    elif xml_asset_type == "ASSET_TYPE_DRAWABLE":
        return AssetType.DRAWABLE
    elif xml_asset_type == "ASSET_TYPE_DRAWABLE_DICTIONARY":
        return AssetType.DRAWABLE_DICTIONARY

    return AssetType.ASSETLESS


def create_archetype(archetype_xml: ytypxml.BaseArchetype, ytyp: CMapTypesProperties):
    """Create a ytyp archetype given an archetype cwxml and a Blender ytyp data-block."""

    archetype: ArchetypeProperties = ytyp.new_archetype(bpy.context)

    archetype.name = archetype_xml.name
    archetype.flags.total = str(archetype_xml.flags)
    archetype.special_attribute = archetype_xml.special_attribute
    archetype.hd_texture_dist = archetype_xml.hd_texture_dist
    archetype.texture_dictionary = archetype_xml.texture_dictionary
    archetype.clip_dictionary = archetype_xml.clip_dictionary
    archetype.drawable_dictionary = archetype_xml.drawable_dictionary
    archetype.physics_dictionary = archetype_xml.physics_dictionary
    archetype.bb_min = archetype_xml.bb_min
    archetype.bb_max = archetype_xml.bb_max
    archetype.bs_center = archetype_xml.bs_center
    archetype.bs_radius = archetype_xml.bs_radius
    archetype.asset_name = archetype_xml.asset_name
    archetype.asset_type = get_asset_type_enum(archetype_xml.asset_type)

    find_and_set_archetype_asset(archetype)

    if archetype_xml.type == "CBaseArchetypeDef":
        archetype.type = ArchetypeType.BASE
    elif archetype_xml.type == "CTimeArchetypeDef":
        archetype.type = ArchetypeType.TIME
        archetype.time_flags.total = str(archetype_xml.time_flags)
    elif archetype_xml.type == "CMloArchetypeDef":
        archetype.type = ArchetypeType.MLO
        archetype.mlo_flags.total = str(archetype_xml.mlo_flags)
        create_mlo_archetype_children(archetype_xml, archetype)


def ytyp_to_obj(ytyp_xml: ytypxml.CMapTypes):
    """Create a ytyp data-block in the Blender scene given a ytyp cwxml."""

    ytyp: CMapTypesProperties = bpy.context.scene.ytyps.add()
    ytyp.name = ytyp_xml.name

    for arch_xml in ytyp_xml.archetypes:
        create_archetype(arch_xml, ytyp)
